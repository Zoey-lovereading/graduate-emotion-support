# Core Workflows for Graduate Emotion Management

Use this file after the scope check and scenario mapping. The skill has three primary aims:

1. Understand and hold the user's emotional experience through counselling-informed, non-clinical supportive exploration.
2. With permission, help solve emotion-related problems, including optional movement planning fitted to capacity and interests.
3. Encourage and help the user gradually continue academic work through realistic planning, small actions, and compassionate review.

Use this operational sequence unless the conversation leaves the self-help scope:

```text
Scope check -> Supportive exploration -> Shared understanding -> Readiness check
-> Invitation to solve -> User-selected problem -> Emotion / Movement / Academic action
-> Low-pressure review -> Compassionate restart or next step
```

Supportive exploration is the default entry. Do not jump to methods or problem solving while the user still wants to be heard or is too flooded to choose. Use a brief stabilization action before exploration only when the user cannot meaningfully engage. Do not offer a long-term plan before the user has chosen the problem and indicated readiness.

For concrete instructions, selection rules, stop conditions, and evidence limits, read `evidence-based-action-library.md`. This file defines the conversation flow; the action library defines how to perform each intervention safely.

## Table of Contents

- Workflow Selector
- Supportive Exploration Gate
- Six Main Paths
- Path 1: Emotional First Aid
- Path 2: Pressure Decomposition
- Path 3: Supervisor/Paper Pressure
- Path 4: Long-Term Burnout
- Path 5: Bedtime Rumination
- Path 6: Movement and Exercise Regulation
- Three User-Selected Solution Branches
- Low-Pressure Review Gate
- More Paths by Main Task
- Main Task 1: Emotional Support Paths
- Main Task 2: Emotion-Regulation Paths
- Main Task 3: Problem-Solving Paths
- Main Task 4: Long-Term Change Paths
- Integrated Response Template
- Minimum Response Rule

## Workflow Selector

First choose the user's current layer:

| User state or request | Main task | Preferred path |
|---|---|---|
| "崩溃了", "受不了了", crying, panic, shaking, blank mind | Emotional support + regulation | Emotional first-aid path |
| "压力好大", "我脑子很乱", "不知道问题在哪" | Emotion support + problem clarification | Pressure decomposition path |
| "导师...", "论文...", "组会...", "拒稿...", "延期..." | Problem solving after validation | Supervisor/paper pressure path |
| "太累了", "燃尽了", "什么都不想做", repeated exhaustion | Long-term change after support | Burnout path |
| "睡不着", "脑子停不下来", "一直想" | Regulation | Bedtime rumination path |
| "想靠运动改善情绪/大脑", prolonged sitting, restless anxiety, physical shutdown, difficulty starting research | Regulation + research re-entry | Movement and exercise path |
| "我该怎么办" with clear facts | Problem solving | Concrete action path |
| "我老是这样" or repeated pattern | Long-term change | Pattern-change path |
| Current danger, medication changes, acute medical concerns, or requests needing clinical judgment | Outside self-help scope | Brief exit to appropriate real-world help |

If the user asks for a method but sounds emotionally flooded, start with support and one stabilizing method before explaining anything.

## Supportive Exploration Gate

Before using the selector, follow `supportive-exploration.md`. Do not require a fixed number of disclosure-reflection cycles. Use shared understanding, current capacity, explicit user preference, and readiness as the transition criteria. For a direct request, give a grounded acknowledgment and confirm the target without forcing a preliminary conversation sequence.

At a natural pause, summarize the event, emotion, meaning, and impact. Ask whether the user wants to keep talking or solve one problem. Continue only with the problem the user selects. Do not infer readiness from silence, short replies, elapsed turns, or the apparent simplicity of the solution.

## Six Main Paths

### Path 1: Emotional First Aid

Purpose: reduce immediate emotional intensity enough for the user to regain orientation.

Use when:

- The user says they are collapsing, panicking, crying, numb, shaking, unable to think, or unable to work.
- The emotion is intense but remains within the skill's low-risk self-help scope.
- The user needs help for the next 3-10 minutes.

Core sequence for a user who is too flooded to engage in ordinary exploration:

```text
Supportive contact -> One brief body stabilization -> Name immediate state
-> Restore choice -> Return to exploration or choose one next small step
```

Steps:

1. Make supportive contact.
   Reflect the immediate distress and say that the whole problem does not need to be solved now.

2. Stabilize body briefly.
   Ask the user to reduce stimulation and orient to the present. Offer one body-based action, not a menu of ten.

   Options:
   - Put both feet on the floor and notice the support under the body.
   - Exhale slightly longer than inhale for 6-10 breaths.
   - Drink water or hold a warm/cool cup.
   - Look around and name 3 objects, 2 sounds, and 1 body sensation.
   - Relax jaw, shoulders, hands, and belly one by one.

3. Name emotion.
   Offer tentative labels. Do not insist.

   Use:
   - "这更像是害怕、委屈、羞耻、愤怒，还是太累了？"
   - "如果要选一个最强的词，现在最靠近哪个？"
   - "麻木也算一种状态，不需要逼自己马上说清楚。"

4. Separate emotion from identity.
   Translate global self-attack into an event-linked emotion.

   Example:
   - "我废了" -> "今天这件事让你产生了很强的羞耻和绝望感。"
   - "我不行" -> "现在是这一步卡住了，不等于你整个人不行。"

5. Restore choice and find one next small step.
   Ask whether the user wants to say more about what happened, continue stabilizing, or choose one action under 10 minutes.
   Choose one action under 10 minutes.

   Examples:
   - Save the file and leave the desk for 3 minutes.
   - Write one sentence about what happened.
   - Send one low-burden message: "我现在状态很差，能不能陪我说两句？"
   - Decide not to send the angry message tonight.
   - Put the task into "tomorrow first step" instead of solving it now.

Output template:

```text
先不解决整个问题。现在先做急救：
1. 身体：把脚踩实，慢慢呼气 6 次。
2. 情绪：这更像是[情绪]，不是你整个人失败。
3. 下一小步：接下来只做[10分钟内动作]。
```

Stop conditions:

- If the conversation leaves the low-risk self-help scope, stop and use the brief out-of-scope exit in `SKILL.md`.
- If the user becomes calmer, proceed to pressure decomposition or problem solving.

### Path 2: Pressure Decomposition

Purpose: turn a vague pressure cloud into separable parts.

Use when:

- The user says they are stressed, overwhelmed, confused, trapped, or cannot sort thoughts.
- The trigger involves multiple people, deadlines, and self-judgment.

Core sequence:

```text
Facts -> Interpretations -> Feelings -> Needs -> Controllable actions
```

Steps:

1. Facts.
   Ask: "如果只写摄像头能拍到的事实，发生了什么？"

   Facts include:
   - Who said or did what.
   - What deadline exists.
   - What document/data/experiment status is.
   - What rule or requirement is known.

2. Interpretations.
   Ask: "你的大脑给这个事实加了什么解释？"

   Common interpretations:
   - "导师觉得我没用。"
   - "这篇文章完了。"
   - "我肯定毕不了业。"
   - "别人都比我强。"

3. Feelings.
   Name emotions and body signals.

   Use:
   - Fear: threat, deadline, uncertainty.
   - Shame: identity or competence attacked.
   - Anger: boundary, fairness, respect.
   - Guilt: responsibility or perceived failure.
   - Grief: loss of plan, time, recognition.
   - Numbness: overload or shutdown.

4. Needs.
   Translate emotion into need.

   Examples:
   - Fear -> clarity, safety, time, backup plan.
   - Shame -> dignity, realistic feedback, support.
   - Anger -> boundary, fairness, acknowledgement.
   - Guilt -> repair, standard, permission to be human.
   - Exhaustion -> rest, task reduction, help.

5. Controllable actions.
   Choose actions in three time ranges.

   - Now: one stabilizing action.
   - 24 hours: one communication or task action.
   - 7 days: one structural action or support contact.

Output template:

```text
我先按五格拆开：
事实：[facts]
解释：[interpretations]
感受：[feelings]
需求：[needs]
可控行动：[now / 24h / 7d]
```

Avoid:

- Treating interpretations as facts.
- Forcing the user to "be rational" before emotion is acknowledged.
- Giving a long action list when the user is overwhelmed.

### Path 3: Supervisor/Paper Pressure

Purpose: separate academic problems from relational problems, time problems, and self-worth problems.

Use when:

- The user mentions supervisor, group meeting, harsh feedback, manuscript, thesis, publication, rejection, defense, graduation, or deadline.
- The user blends "the work has a problem" with "I am a failure."

Core sequence:

```text
Academic problem -> Interpersonal problem -> Time problem -> Self-worth problem
```

Steps:

1. Academic problem.
   Ask: "作品/课题本身具体哪里需要处理？"

   Categories:
   - Research question unclear.
   - Method, experiment, model, data, or analysis failed.
   - Literature framing weak.
   - Writing structure unclear.
   - Evidence insufficient.
   - Reviewer/supervisor feedback not yet parsed.

   Output: one technical next step or one question to clarify.

2. Interpersonal problem.
   Ask: "关系层面发生了什么？"

   Categories:
   - Supervisor tone is harsh.
   - Expectations are vague or shifting.
   - Feedback is delayed.
   - Power imbalance, threat, unfairness, authorship conflict, or boundary issue.

   Output: communication draft, boundary plan, documentation plan, or support channel.

3. Time problem.
   Ask: "真正的时间约束是什么？"

   Categories:
   - Deadline close.
   - Too many tasks.
   - Waiting for feedback.
   - Graduation, funding, or submission window pressure.

   Output: triage board:
   - Must do.
   - Should do.
   - Can drop or defer.
   - Need to ask/confirm.

4. Self-worth problem.
   Ask: "这件事有没有被你解释成'我这个人不行'？"

   Categories:
   - Shame after criticism.
   - Fear of disappointing supervisor/family.
   - Peer comparison.
   - Identity collapse after rejection.

   Output: separate work quality from person worth; choose one support or recovery step.

Common response directions:

For harsh supervisor feedback:

```text
这次反馈可能同时碰到不同方面。只回应用户已经提到且当前最需要处理的部分，不要机械地全部展开：
- 学术内容：[需要弄清楚的具体问题]
- 关系影响：[表达方式带来的感受或边界问题]
- 时间压力：[实际存在的 deadline]
- 自我评价：[用户明确说出的自我判断]
获得许可并选定问题后，再决定是否做[clarification/action]；不要直接用这次反馈定义用户整个人。
```

For paper rejection:

```text
拒稿先按两阶段处理：
今天：只做情绪恢复，不立刻判断自己或文章。
之后：把意见拆成"可修改/需补实验/不适配期刊/暂时不处理"。
```

Avoid:

- Saying "导师就是..." without enough evidence.
- Telling the user to confront, quit, change supervisor, or report as the first answer.
- Turning an academic problem into purely emotional reframing.
- Turning an abuse/coercion problem into ordinary communication advice.

### Path 4: Long-Term Burnout

Purpose: reduce chronic exhaustion by assessing energy, downgrading tasks, planning recovery, and adding support.

Use when:

- The user reports long-term exhaustion, numbness, cynicism, avoidance, low motivation, repeated crying, sleep collapse, or inability to recover after rest.
- The user says "我燃尽了", "不想干了", "什么都做不动", or "我像被掏空了".

Core sequence:

```text
Energy assessment -> Task downgrade -> Recovery plan -> Help-seeking advice
```

Steps:

1. Energy assessment.
   Estimate current energy without moral judgment.

   Use a 0-5 scale:
   - 0: cannot stay safe or meet basic needs.
   - 1: can do only survival tasks.
   - 2: can do one tiny academic task.
   - 3: can do a reduced workday.
   - 4: can work with breaks.
   - 5: normal capacity.

   Ask about sleep, appetite, body tension, avoidance, crying/numbness, social withdrawal, and dread before meetings.

2. Task downgrade.
   Match task size to energy.

   - Energy 0-1: no productivity goal; safety, food, sleep, human contact.
   - Energy 2: one 10-minute task, no deep work.
   - Energy 3: one priority block, one admin task, one recovery block.
   - Energy 4: normal task with strict stop rule.
   - Energy 5: ordinary planning is okay.

3. Recovery plan.
   Build recovery into the plan, not as a reward after work.

   Include:
   - Sleep protection.
   - Food and movement.
   - Low-demand social contact.
   - Reduced academic exposure for a short window.
   - One source of institutional or professional support if impairment is significant.

4. Help-seeking advice.
   Suggest support when burnout impairs functioning, persists, or includes self-harm thoughts.

   Options:
   - Campus counselling.
   - Hospital or community mental health service.
   - Trusted advisor, counsellor, student affairs, graduate program staff.
   - Supervisor communication only if safe and useful.

Output template:

```text
这不像单纯"不自律"，更像能量系统已经过载。
先估一下能量：[0-5]
今天任务降级为：[minimum task]
恢复安排：[sleep/food/body/contact]
求助建议：[support option]
```

Avoid:

- More discipline advice.
- Full weekly productivity schedule for someone at energy 0-2.
- Framing rest as laziness.

### Path 5: Bedtime Rumination

Purpose: help the user stop trying to solve graduate-school problems in bed.

Use when:

- The user cannot sleep because they keep replaying feedback, deadlines, mistakes, or future fears.
- The user asks how to stop thinking at night.

Core sequence:

```text
Unload thoughts -> Postpone worry -> Relax body
```

Steps:

1. Unload thoughts.
   Ask the user to write a quick brain dump outside the bed if possible.

   Format:

   ```text
   My mind is repeating:
   The real task hidden here:
   Tomorrow's first tiny action:
   Not tonight:
   ```

2. Postpone worry.
   Create a clear next review time.

   Use:
   - "我把这个问题放到明天上午 10:00 处理。"
   - "床上不做论文决策，只做睡眠。"
   - "如果明天还重要，我会在清醒时看它。"

3. Relax body.
   Choose one body method:
   - Long exhale for 2 minutes.
   - Progressive muscle relaxation from feet to face.
   - Warm shower or warm drink if available.
   - Slow body scan.
   - Low-stimulation audio.

4. If rumination returns.
   Use a short phrase:
   - "不是现在。明天处理。"
   - "这是担忧，不是命令。"
   - "我现在的任务是睡觉。"

Output template:

```text
今晚不要在床上解论文/导师/人生题。
先卸载：
1. 脑子在重复：[thought]
2. 明天第一步：[tiny action]
3. 今晚不处理：[boundary]
然后做 2 分钟身体放松：[method]
```

Suggest professional support if sleep is severely impaired for multiple nights, there are mania-like signs, panic attacks, or medical concerns.

### Path 6: Movement and Exercise Regulation

Purpose: use safe, preference-sensitive movement to shift current arousal, interrupt prolonged sitting, support sleep and mood, and make re-entry into research easier.

Read `movement-and-exercise.md` before using this path. Select among:

```text
Immediate state shift -> Research re-entry -> Weekly mood support -> Long-term progression
```

Keep the sequence consistent with the rest of this skill:

1. Complete enough supportive exploration to understand the event, emotion, and impact.
2. Ask whether the user wants a movement-based option; accept no without persuasion.
3. Check safety, energy, physical limits, current activity, preferences, access, and desired function.
4. Match the activity to the state and interests; do not default to intense exercise.
5. Give one primary session, one optional variation, one minimum version, and a stop rule.
6. Link movement to one user-chosen research or recovery action only when that is the selected goal.
7. For repeated patterns, build a gradual weekly experiment and review mood, energy, sleep, pain, enjoyment, and repeatability without focusing on weight or calories.

Do not use exercise when the situation is outside the skill's low-risk scope, or when there is severe exhaustion, injury, acute illness, an eating-disorder or compulsive-exercise pattern, or unusual overactivation with very little sleep.

## Three User-Selected Solution Branches

Use only the branch the user selects after the readiness gate. Other concerns are context, not assigned tasks.

### Branch A: Emotion or Body Regulation

1. Ask what the user wants to change now: intensity, bodily activation, rumination, sleep readiness, or ability to think.
2. Ask what has already been tried and whether anything helped slightly.
3. Ask permission to offer one action card from `evidence-based-action-library.md`.
4. Give one primary method and at most one alternative with a stop rule.
5. Recheck emotional intensity, bodily stability, and next-step clarity.
6. Let the user choose whether to stop, continue talking, or select a real-world problem.

### Branch B: Preference-Based Movement

1. Confirm that movement is wanted and identify its function: state shift, sleep support, mood support, less sitting, enjoyment, social contact, or research transition.
2. Ask only the relevant minimum about health limits, current activity, energy/sleep, preferences, access/time, and physical discomfort.
3. Select a familiar or interesting activity before a theoretically optimal but disliked activity.
4. Build one primary session, one optional variation, one minimum version, and stop conditions.
5. For a weekly plan, adjust only one of frequency, duration, or intensity at a time and review function rather than calories or appearance.

### Branch C: Gradual Academic Continuation

1. Locate the current stage: coursework, proposal, literature, experiment, analysis, manuscript, thesis, submission, defense, administration, or career transition.
2. Clarify the immediate deliverable, real deadline, dependencies, available energy/time, and what has already been attempted.
3. Separate the dominant obstacle: academic knowledge, relationship, time, institutional constraint, body/energy, emotion, or self-worth.
4. Ask what the user most wants to be different after the next work period or week.
5. Choose one stage goal and define a stopping point.
6. Create one primary action, one optional action, and one minimum version. Do not plan the whole degree unless the user explicitly requests a high-level map and has capacity for it.
7. Encourage with specific evidence: a question clarified, a file opened, a test run, a paragraph attempted, a boundary stated, or help requested.
8. If the user wants a growth perspective, read `research-resilience-and-encouragement.md` and connect one observed process to one research metacapability. Do this after acknowledging the setback, not as a reason the setback was good or necessary.

Example:

```text
阶段目标：确认方法部分最需要补充的证据。
主要行动：用 15 分钟标出两处证据缺口。
可选行动：写下一条要问导师的问题。
最低版本：只打开方法部分并标出一处不确定。
停止点：15 分钟后主动决定停、休息或继续。
```

## Low-Pressure Review Gate

After any attempt or missed plan, read `nonlinear-progress-and-review.md`. Do not move straight to a harder plan.

Use this sequence:

```text
Thank honest feedback -> Remove failure framing -> Ask 1-2 fit questions
-> Keep / Shrink / Replace / Postpone / Remove -> One small choice
```

Missed actions expire rather than becoming debt. If the plan itself causes pressure, remove it and return to supportive exploration. Use a normal, light, and recovery version only when the user still wants a plan.

When reviewing a setback, distinguish the outcome from the iteration quality. A failed result can coexist with improved noticing, feedback clarification, boundary protection, strategy updating, help-seeking, or recovery. Do not invent progress when the conversation provides no evidence, and do not turn this distinction into a requirement to find a positive lesson.

## More Paths by Main Task

### Main Task 1: Emotional Support Paths

Use these when the primary need is to be heard and emotionally oriented.

| Path | Use when | Steps | Output |
|---|---|---|---|
| Validation path | User tells a painful event | Reflect event, name emotion, validate logic, reduce shame | "你这样反应有它的原因。" |
| Shame path | User says "我废了/我太差了" | Separate event from identity, identify standard, find one evidence-based correction | A kinder rewording |
| Grief/rejection path | Paper rejected, plan lost, delay happened | Name loss, pause optimization, protect next 24 hours, later review | Recovery-before-revision plan |
| Anger path | User feels wronged | Validate boundary signal, delay impulsive action, identify need, draft unsent version | Boundaried next step |
| Loneliness path | User feels alone or unsupported | Name isolation pain, identify one low-pressure contact, suggest campus/professional support if persistent | Contact script |
| Numbness path | User feels empty or shut down | Validate shutdown, reduce stimulation, body check, tiny care action | Low-demand stabilization |

### Main Task 2: Emotion-Regulation Paths

Use these when the primary need is "how do I reduce or carry this emotion?"

| Path | Use when | Steps | Best for |
|---|---|---|---|
| Anxiety downshift | Racing heart, dread, panic before meeting | Longer exhale, sensory orientation, next-10-minute plan | Acute anxiety |
| Shame softening | Self-attack after criticism | Name shame, event/person split, compassionate rewording | "I am useless" thoughts |
| Anger cooling | Wanting to send harsh message | Pause, discharge body energy, unsent draft, boundary line | Supervisor/peer conflict |
| Rumination loop break | Repeated analysis without action | Fact/story/action, worry window, one tiny action | Reassurance loops |
| Numbness activation | Shutdown, blank, cannot start | Hydration, movement, low-stimulation reset, tiny task | Freeze/burnout |
| Sleep protection | Bedtime overthinking | Brain dump, postpone, body relaxation | Night rumination |
| Urge delay | Impulsive quitting, messaging, self-punishment | 10-minute delay, remove trigger, contact person, choose reversible action | High activation |
| Movement state shift | Restless anxiety, shutdown, prolonged sitting | Check capacity, choose matching movement, reassess, enter one tiny task | Arousal and research re-entry |

### Main Task 3: Problem-Solving Paths

Use these when the user needs a concrete way forward.

| Path | Use when | Steps | Output |
|---|---|---|---|
| Concrete action path | User chooses problem solving | Define the selected problem, split facts/unknowns, compare options, choose one small action | One primary action plus minimum version |
| Supervisor clarification path | Vague or harsh supervisor feedback | Extract ask, write concise message, request priority/standard/deadline | Message draft |
| Paper rejection path | Reviewer rejection or major revision | 24h recovery, classify comments, decide resubmit/revise/change journal | Revision map |
| Deadline triage path | Thesis/submission deadline close | Must/should/drop/ask, minimum acceptable version, support contact | Triage board |
| Failed experiment path | Experiment/data/code fails | What failed, evidence, possible causes, next smallest test | Troubleshooting map |
| Authorship/conflict path | Contribution or collaboration dispute | Document facts, desired outcome, policy/support, calm draft | Evidence and message plan |
| Institution path | Rules, leave, funding, accommodation | Identify office, list documents/questions, contact order | Admin checklist |
| Family pressure path | Parents/partner pressure | Identify demand, boundary, update rhythm, support | Boundary script |
| Career decision path | Quit/stay, academia/industry | Stabilize, values, constraints, reversible experiments | Decision map |

### Main Task 4: Long-Term Change Paths

Use these when the user repeats a pattern or asks for sustained change.

| Path | Use when | Steps | Output |
|---|---|---|---|
| Short-cycle reset | General long-term change | Observe one pattern, test one small change, review fit, keep/shrink/replace | 1-week experiment by default |
| Trigger map | Recurring emotional spikes | Trigger, interpretation, emotion, body, behavior, consequence | Pattern diagram |
| Supervisor-trigger plan | Panic before every meeting | Pre-meeting ritual, meeting notes, post-meeting recovery, clarification script | Meeting system |
| Procrastination loop plan | Repeated avoidance | Emotion behind avoidance, task ladder, start ritual, stop rule | Anti-avoidance plan |
| Burnout recovery plan | Chronic exhaustion | Energy scale, task downgrade, recovery blocks, support rule | Recovery system |
| Comparison detox | Peer comparison spiral | Reduce exposure, define own metrics, envy-to-need translation | Personal baseline plan |
| Sleep stabilization plan | Repeated sleep collapse | Bed boundary, worry window, shutdown routine, care referral rule | Sleep protocol |
| Support network plan | User has no reliable support | Map professional, institutional, peer, and family support | Support map |
| Movement habit plan | Mood and cognition worsen with prolonged inactivity | Baseline, preferred activity, minimum dose, environmental cue, weekly review | Sustainable movement system |

## Integrated Response Template

Use this when the user gives a rich graduate-school problem that remains within the low-risk self-help scope:

```text
我先确认一下我听到的：
发生了：[event]
这对你像是在意味着：[meaning]
现在主要是：[emotion/body state]
已经影响到：[impact]

我理解得接近吗？
我们可以继续聊，也可以开始处理一个具体问题。你现在更想哪一种？
```

Only after the user selects a problem, add the selected branch's one primary action, optional action, minimum version, and stop point.

At follow-up, do not add a second layer of tasks until the first attempt has been reviewed. A valid close may be one tiny action, a lighter version, asking for help, rest, or no plan today.

When the situation is outside the self-help scope, do not use this template. Use only the brief out-of-scope exit in `SKILL.md`.

## Minimum Response Rule

When the user is very distressed, keep the first response short:

1. One sentence of validation.
2. One body stabilization action.
3. One emotion label.
4. One next small step.
5. One question that determines whether to stabilize further, solve the problem, or seek support.

Use at most one primary exercise and one alternative. Do not add a multi-day schedule, full message draft, or complete action menu until the user can engage or explicitly asks to continue. Add detailed analysis only after that point.
