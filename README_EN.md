# Graduate Student Emotion Support

English | [简体中文](README.md)

A low-risk, non-clinical emotional support plugin for master's students, doctoral students, and researchers aged 18 or older. It begins by understanding the user's specific experience and emotions, then lets the user decide whether to move into emotion regulation, research-problem decomposition, setback review, movement support, or a gradual return to academic work.

## Core Capabilities

- Grounded emotional support after supervisor criticism, failed experiments, manuscript rejection, burnout, self-doubt, or stalled research.
- Treats feedback processing, recovery choices, method iteration, help-seeking, and boundary protection as trainable research metacapabilities without romanticizing suffering.
- Does not organize responses around fixed character counts, support layers, or conversation turns.
- Can create a local continuity profile that the user may view, correct, or delete, but only after the user gives explicit consent.
- Moves into problem solving, exercise, or academic planning only with the user's permission. Missed actions do not accumulate as debt and never require catch-up work.

## Usage

Explicit invocation is currently recommended:

```text
$graduate-emotion-management My supervisor criticized me in front of the lab today. Please help me talk through what happened before offering advice.
```

Implicit activation from natural-language requests depends on platform routing. In current testing, implicit activation of the movement module remains inconsistent and is not presented as a guaranteed capability.

## Safety Boundaries

This plugin is not counselling, psychotherapy, diagnosis, medical care, crisis intervention, or an emergency service. It does not provide medication plans, clinical judgments, or regional or university crisis-resource matching. Anyone facing current risk of self-harm or harm to others, an acute medical danger, or another situation outside low-risk self-help should immediately contact a trusted person in real life and appropriate local emergency or professional support.

## Data and Continuity

The current version has no developer-operated server, user account system, analytics, or advertising component. An optional continuity profile is created only after the user confirms both what may be saved and a private storage location. It does not save complete conversations or every emotional change by default, and it is not automatically sent to the developer.

## Testing

Before the 0.4.2 release, the plugin completed 73 isolated behavioral tests: 72 passed, one documented non-blocking limitation involved implicit routing, and there were no release-blocking failures. All P0 safety, P1 core, movement safety, resource-boundary, and support-quality groups passed.

- [Behavioral test summary](docs/behavioral-test-summary.md)
- [Full test report](docs/test-report-0.4.2.md)

## Documentation

- [Support and contact](docs/support.md)
- [Privacy policy](docs/privacy-policy.md)
- [Terms of use](docs/terms-of-use.md)
- [Icon provenance and rights record](docs/icon-rights.md)

## License

Licensed under the [PolyForm Noncommercial License 1.0.0](LICENSE.md). Commercial use is not authorized. This license is not an OSI-approved open-source license.

