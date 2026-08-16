# User Profile and Conversation Continuity

Use this reference whenever the user asks the skill to remember something, refers to earlier information, corrects an earlier fact, returns to an ongoing issue, or wants continuity across conversations.

## Two Different Kinds of Memory

### 1. Current-conversation continuity

This is mandatory and uses only information visible in the current conversation plus any explicitly loaded profile. Before every substantive response, reconcile a private working ledger with these fields:

- Academic identity: preferred form of address, master's/doctoral/research role, stage, broad field, and current milestone.
- Current need: companionship, understanding, regulation, problem solving, planning, or review.
- Active issue: the concrete situation or repeated pattern currently being discussed.
- Confirmed facts: only details the user actually provided.
- Current impact: effects on emotion, body, sleep, research, relationships, daily care, or self-evaluation.
- User goal: what the user wants from this conversation or wants to change.
- Constraints and boundaries: time, energy, health, power relations, privacy, unwanted topics, and explicit refusals.
- Support preferences: desired tone, depth, pacing, advice permission, helpful approaches, and approaches to avoid.
- Method history: what was tried and whether the user found it helpful, neutral, unhelpful, or worse.
- Agreed next step and open threads: only decisions actually made together.

Do not display this ledger as a form unless the user asks. Use it to prevent forgetting, repeated questions, contradictory advice, and recommendations that already failed.

### 2. Cross-conversation continuity

The model does not possess reliable native long-term memory merely because this skill is installed. Cross-conversation continuity requires either host-platform memory controlled by the host product or a user-controlled profile file that is available in the new conversation.

Never say "我一直记得" unless the relevant fact is visible in the current conversation or was loaded from an accessible, consent-enabled profile. If neither source is available, say that the earlier details are not visible and request only the minimum recap.

## Context Reconciliation Before Every Answer

Apply this precedence order:

```text
Latest explicit user statement
> earlier explicit statement in the visible conversation
> user-confirmed profile fact
> tentative interpretation
```

- The latest explicit correction replaces an older fact for the current response.
- Save the correction to the persistent profile only when the user explicitly asks to remember it or confirms the update.
- Never ask again for a confirmed fact merely because a template expects it. Recheck only when it is plausibly stale, conflicts with new information, or materially affects safety or fit.
- Use only profile facts relevant to the current question. Do not recite the profile to demonstrate memory.
- Refer back naturally and specifically, for example: "你前面说过呼吸练习会让你更难受，所以这次不再用它。"
- If the current request conflicts with an older preference, follow the current request for this turn and ask whether the standing preference should also change only when that matters later.
- When several issues exist, distinguish active, paused, and resolved issues. Do not merge them into one global story about the user.

## Formulating a Clear Issue

Record an issue as a practical, revisable statement:

```text
Situation or pattern + present impact + user's desired change + relevant constraints
```

Good:

- "导师反馈很笼统，用户不知道从哪里修改，当前希望先形成一个澄清问题；今天精力较低。"
- "实验连续失败后开始回避记录，用户目前只想先处理失败后的自我否定，不想排查实验。"

Do not record:

- "用户抗挫力差。"
- "用户是完美主义人格。"
- "用户有焦虑症。"

Keep the user's painful self-judgment separate from confirmed facts. If the user says "我不适合科研," record it as a current thought or concern, not as identity.

## User-Controlled Persistent Profile

Use `scripts/continuity_profile.py` for a deterministic local JSON profile when the environment permits file access.

### Memory-intent route

When the user's main request is to remember, update, inspect, correct, or forget information, complete that operation before returning to the emotional-support workflow.

- With no loaded profile, an explicit "请记住" does not justify saying that cross-conversation memory is now active. Summarize the proposed record and ask whether to create a local profile in a private location.
- With a loaded consent-enabled profile, an explicit request to remember an exact fact authorizes that exact update. Apply it and report the changed sections.
- When asked what is remembered, do not derive identity from the skill being active or from generic graduate-school context. Report only visible or loaded confirmed facts.
- Do not append an academic exploration question to a profile-consent response unless the user separately requested help with the issue in the same message.

### Consent flow

1. Do not create a profile during fresh acute distress, the out-of-scope safety exit, or merely because continuity would be convenient.
2. When the user asks to be remembered or continuity would clearly help at a calm point, explain that the skill has no automatic permanent memory and offer a user-controlled local profile.
3. Before first creation, show a brief candidate summary of what would be saved and ask the user to confirm both the fields and storage location.
4. A direct request such as "请记住我不想做呼吸练习" counts as confirmation for that exact fact when a consent-enabled profile already exists. Do not turn every update into another consent ceremony.
5. Never save tentative inferences. Ask the user to confirm them or leave them out.
6. After each update, state briefly what changed. Provide the full profile only when requested.

Do not put the profile in a shared repository, lab drive, synced team folder, or public project by default. Prefer a private user-selected folder. The suggested filename is `graduate-emotion-continuity-profile.json`.

### Profile contents

The profile may contain only user-confirmed continuity information:

- `academic_identity`: preferred address, role, stage, broad field, and current milestone.
- `current_issues`: stable issue ID, neutral summary, status, confirmed facts, current impact, user goal, constraints, and last agreed next step.
- `support_preferences`: response style, helpful and unhelpful approaches, boundaries, and advice preference.
- `method_history`: method, user-reported result, and a minimal note.
- `open_threads`: unfinished topics the user wants to return to.
- `notes_user_wants_remembered`: other short facts the user explicitly requested to preserve.

Do not save full transcripts, every mood fluctuation, diagnoses, inferred personality traits, risk scores, real names by default, student or identity numbers, exact institution or address, contact information, medical records, supervisor identities, third-party identifying information, or detailed crisis disclosures. A preferred nickname or form of address may be stored when the user explicitly requests it.

### Profile operations

Create only after confirmation:

```powershell
python scripts/continuity_profile.py init --path <private-profile-path> --user-confirmed
```

Read or validate:

```powershell
python scripts/continuity_profile.py show --path <profile-path>
python scripts/continuity_profile.py validate --path <profile-path>
```

Apply a user-confirmed structured update:

```powershell
python scripts/continuity_profile.py apply --path <profile-path> --patch-json <json> --user-confirmed
```

Clear a section or delete the whole profile only after an explicit user request:

```powershell
python scripts/continuity_profile.py clear --path <profile-path> --section <section> --user-confirmed
python scripts/continuity_profile.py delete --path <profile-path> --confirm-delete
```

The user may view, correct, export, move, or delete the file at any time. Do not claim that deleting this local file also deletes host-platform conversations or logs.

## Loading a Profile in a New Conversation

- Load a profile only when it is explicitly supplied, the user points to it, or exactly one clearly named profile is present in the private workspace context and its `consent.enabled` value is `true`.
- If several profiles are available, ask which one to use. Never choose by guessing identity.
- Validate the file before use. Ignore unknown or malformed fields and explain that the profile needs repair.
- Treat stage, milestone, active issue, current impact, and next steps as potentially stale. Phrase them as prior records until the user confirms they are still current.
- Do not let an old profile overrule the user's current statement.
- When the user asks "你还记得吗," answer with the exact source boundary: visible conversation, loaded profile, or no available record.

## Forgetting and Correction

- "忘掉这件事" means remove the specified profile field or issue, not merely stop mentioning it.
- "不要再提" may be a conversational boundary rather than a deletion request. Confirm deletion only if the distinction matters.
- Correct inaccurate facts without preserving the old value in a hidden note unless the user explicitly wants a history.
- Mark an issue `resolved` only when the user says it is resolved or confirms that status. Paused is not resolved.
- Do not create a longitudinal emotion score or personality trajectory from the profile. That is a separate, optional feature requiring its own consent and design.
