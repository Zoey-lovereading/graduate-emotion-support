from __future__ import annotations

import argparse
import copy
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = 1
EDITABLE_SECTIONS = {
    "academic_identity",
    "current_issues",
    "support_preferences",
    "method_history",
    "open_threads",
    "notes_user_wants_remembered",
}
ISSUE_STATUSES = {"active", "paused", "resolved"}
METHOD_RESULTS = {"helpful", "neutral", "unhelpful", "worse", "unknown"}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def empty_profile() -> dict[str, Any]:
    timestamp = now_iso()
    return {
        "schema_version": SCHEMA_VERSION,
        "profile_purpose": "user-confirmed conversation continuity",
        "consent": {"enabled": True, "confirmed_at": timestamp},
        "created_at": timestamp,
        "updated_at": timestamp,
        "academic_identity": {
            "preferred_address": None,
            "role": None,
            "stage": None,
            "broad_field": None,
            "current_milestone": None,
        },
        "current_issues": [],
        "support_preferences": {
            "response_style": [],
            "helpful_approaches": [],
            "unhelpful_approaches": [],
            "boundaries": [],
            "advice_preference": None,
        },
        "method_history": [],
        "open_threads": [],
        "notes_user_wants_remembered": [],
    }


def require_confirmation(value: bool, operation: str) -> None:
    if not value:
        raise ValueError(f"{operation} requires explicit user confirmation")


def ensure_optional_string(value: Any, field: str) -> None:
    if value is not None and not isinstance(value, str):
        raise ValueError(f"{field} must be a string or null")


def ensure_string_list(value: Any, field: str) -> None:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{field} must be a list of strings")


def validate_profile(data: Any) -> None:
    if not isinstance(data, dict):
        raise ValueError("profile must be a JSON object")

    expected = set(empty_profile())
    unknown = set(data) - expected
    missing = expected - set(data)
    if unknown:
        raise ValueError(f"unknown top-level fields: {', '.join(sorted(unknown))}")
    if missing:
        raise ValueError(f"missing top-level fields: {', '.join(sorted(missing))}")
    if data["schema_version"] != SCHEMA_VERSION:
        raise ValueError(f"unsupported schema_version: {data['schema_version']}")
    if data["profile_purpose"] != "user-confirmed conversation continuity":
        raise ValueError("profile_purpose is invalid")

    consent = data["consent"]
    if not isinstance(consent, dict) or set(consent) != {"enabled", "confirmed_at"}:
        raise ValueError("consent must contain enabled and confirmed_at")
    if consent["enabled"] is not True or not isinstance(consent["confirmed_at"], str):
        raise ValueError("profile consent is not enabled or confirmed")

    for field in ("created_at", "updated_at"):
        if not isinstance(data[field], str):
            raise ValueError(f"{field} must be a string")

    identity = data["academic_identity"]
    identity_fields = {
        "preferred_address", "role", "stage", "broad_field", "current_milestone"
    }
    if not isinstance(identity, dict) or set(identity) != identity_fields:
        raise ValueError("academic_identity fields are invalid")
    for key, value in identity.items():
        ensure_optional_string(value, f"academic_identity.{key}")

    preferences = data["support_preferences"]
    preference_fields = {
        "response_style", "helpful_approaches", "unhelpful_approaches",
        "boundaries", "advice_preference",
    }
    if not isinstance(preferences, dict) or set(preferences) != preference_fields:
        raise ValueError("support_preferences fields are invalid")
    for key in ("response_style", "helpful_approaches", "unhelpful_approaches", "boundaries"):
        ensure_string_list(preferences[key], f"support_preferences.{key}")
    ensure_optional_string(preferences["advice_preference"], "support_preferences.advice_preference")

    if not isinstance(data["current_issues"], list):
        raise ValueError("current_issues must be a list")
    issue_fields = {
        "id", "summary", "status", "confirmed_facts", "current_impact",
        "user_goal", "constraints", "last_agreed_next_step", "updated_at",
    }
    seen_issue_ids: set[str] = set()
    for index, issue in enumerate(data["current_issues"]):
        prefix = f"current_issues[{index}]"
        if not isinstance(issue, dict) or set(issue) != issue_fields:
            raise ValueError(f"{prefix} fields are invalid")
        for key in ("id", "summary", "updated_at"):
            if not isinstance(issue[key], str) or not issue[key].strip():
                raise ValueError(f"{prefix}.{key} must be a non-empty string")
        if issue["id"] in seen_issue_ids:
            raise ValueError(f"duplicate issue id: {issue['id']}")
        seen_issue_ids.add(issue["id"])
        if issue["status"] not in ISSUE_STATUSES:
            raise ValueError(f"{prefix}.status must be active, paused, or resolved")
        for key in ("confirmed_facts", "current_impact", "constraints"):
            ensure_string_list(issue[key], f"{prefix}.{key}")
        ensure_optional_string(issue["user_goal"], f"{prefix}.user_goal")
        ensure_optional_string(issue["last_agreed_next_step"], f"{prefix}.last_agreed_next_step")

    if not isinstance(data["method_history"], list):
        raise ValueError("method_history must be a list")
    method_fields = {"method", "result", "note", "updated_at"}
    for index, item in enumerate(data["method_history"]):
        prefix = f"method_history[{index}]"
        if not isinstance(item, dict) or set(item) != method_fields:
            raise ValueError(f"{prefix} fields are invalid")
        for key in ("method", "note", "updated_at"):
            if not isinstance(item[key], str):
                raise ValueError(f"{prefix}.{key} must be a string")
        if item["result"] not in METHOD_RESULTS:
            raise ValueError(f"{prefix}.result is invalid")

    ensure_string_list(data["open_threads"], "open_threads")
    ensure_string_list(data["notes_user_wants_remembered"], "notes_user_wants_remembered")


def load_profile(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ValueError(f"profile does not exist: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"profile is not valid JSON: {exc}") from exc
    validate_profile(data)
    return data


def atomic_write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    handle, temp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(payload)
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def merge_known(current: Any, patch: Any, template: Any, field: str) -> Any:
    if isinstance(template, dict):
        if not isinstance(patch, dict):
            raise ValueError(f"{field} patch must be an object")
        unknown = set(patch) - set(template)
        if unknown:
            raise ValueError(f"unknown fields in {field}: {', '.join(sorted(unknown))}")
        merged = copy.deepcopy(current)
        for key, value in patch.items():
            merged[key] = merge_known(current[key], value, template[key], f"{field}.{key}")
        return merged
    if isinstance(template, list):
        if not isinstance(patch, list):
            raise ValueError(f"{field} patch must be a list")
        return copy.deepcopy(patch)
    return copy.deepcopy(patch)


def cmd_init(args: argparse.Namespace) -> None:
    require_confirmation(args.user_confirmed, "profile creation")
    path = Path(args.path).expanduser().resolve()
    if path.exists() and not args.replace:
        raise ValueError(f"profile already exists: {path}; use --replace only after user confirmation")
    atomic_write(path, empty_profile())
    print(f"Created consent-enabled continuity profile: {path}")


def cmd_show(args: argparse.Namespace) -> None:
    data = load_profile(Path(args.path).expanduser().resolve())
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_validate(args: argparse.Namespace) -> None:
    path = Path(args.path).expanduser().resolve()
    load_profile(path)
    print(f"Profile is valid: {path}")


def cmd_apply(args: argparse.Namespace) -> None:
    require_confirmation(args.user_confirmed, "profile update")
    path = Path(args.path).expanduser().resolve()
    current = load_profile(path)
    try:
        patch = json.loads(args.patch_json)
    except json.JSONDecodeError as exc:
        raise ValueError(f"patch is not valid JSON: {exc}") from exc
    if not isinstance(patch, dict) or not patch:
        raise ValueError("patch must be a non-empty JSON object")
    unknown = set(patch) - EDITABLE_SECTIONS
    if unknown:
        raise ValueError(f"non-editable or unknown sections: {', '.join(sorted(unknown))}")

    updated = copy.deepcopy(current)
    template = empty_profile()
    for section, value in patch.items():
        updated[section] = merge_known(current[section], value, template[section], section)
    updated["updated_at"] = now_iso()
    validate_profile(updated)
    atomic_write(path, updated)
    print(f"Updated sections: {', '.join(sorted(patch))}")


def cmd_clear(args: argparse.Namespace) -> None:
    require_confirmation(args.user_confirmed, "profile section deletion")
    if args.section not in EDITABLE_SECTIONS:
        raise ValueError(f"section is not editable: {args.section}")
    path = Path(args.path).expanduser().resolve()
    current = load_profile(path)
    current[args.section] = copy.deepcopy(empty_profile()[args.section])
    current["updated_at"] = now_iso()
    validate_profile(current)
    atomic_write(path, current)
    print(f"Cleared section: {args.section}")


def cmd_delete(args: argparse.Namespace) -> None:
    if not args.confirm_delete:
        raise ValueError("profile deletion requires --confirm-delete")
    path = Path(args.path).expanduser().resolve()
    if not path.is_file():
        raise ValueError(f"profile does not exist: {path}")
    path.unlink()
    print(f"Deleted continuity profile: {path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage a user-confirmed local continuity profile.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init")
    init.add_argument("--path", required=True)
    init.add_argument("--user-confirmed", action="store_true")
    init.add_argument("--replace", action="store_true")
    init.set_defaults(func=cmd_init)

    show = subparsers.add_parser("show")
    show.add_argument("--path", required=True)
    show.set_defaults(func=cmd_show)

    validate = subparsers.add_parser("validate")
    validate.add_argument("--path", required=True)
    validate.set_defaults(func=cmd_validate)

    apply_command = subparsers.add_parser("apply")
    apply_command.add_argument("--path", required=True)
    apply_command.add_argument("--patch-json", required=True)
    apply_command.add_argument("--user-confirmed", action="store_true")
    apply_command.set_defaults(func=cmd_apply)

    clear = subparsers.add_parser("clear")
    clear.add_argument("--path", required=True)
    clear.add_argument("--section", required=True)
    clear.add_argument("--user-confirmed", action="store_true")
    clear.set_defaults(func=cmd_clear)

    delete = subparsers.add_parser("delete")
    delete.add_argument("--path", required=True)
    delete.add_argument("--confirm-delete", action="store_true")
    delete.set_defaults(func=cmd_delete)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

