# How intake requests are decided

> **How to use this template.** This is the decision path behind the [use case intake](use-case-intake.md): who answers, how fast, and what the possible answers are. It is gate G1 and, for most use cases, gate G2 of the [use case lifecycle](../framework/04-use-case-lifecycle.md). Replace the numbers in [brackets] with what your organisation can actually keep.

## 1. Triage, within [2] working days

The AI Governance Lead reads the intake form and answers three questions.

| Question | If yes |
|---|---|
| Is this an approved tool used for an approved purpose? | No new decision needed. Tell the requester, close the request. |
| Is anything ticked under *Quick screening* in the intake form? | Classify carefully with the [EU AI Act Risk Check](https://ai-act-risk-check.streamlit.app) before deciding. Never fast-track. |
| Is information missing that changes the answer? | Put the request on **hold** and ask for it. The clock stops until the answer comes back. |

## 2. Classify and set the intensity

Set the EU AI Act risk tier and the oversight level. Together they give the [governance intensity](../framework/03-oversight-scale.md#governance-intensity), and the intensity decides who decides.

| Intensity | Who decides | Answer within |
|---|---|---|
| light | AI Governance Lead | [2] working days |
| standard | AI Governance Lead, informs the AI Council | [5] working days |
| enhanced | AI Council | [10] working days, or the next meeting |
| strict | AI Council, after the assessments in the [AI system record](ai-system-record.md) | When the assessments are done |
| redesign | Back to the requester: reduce the AI's autonomy before it can be considered | [5] working days |
| stop | Rejected. Prohibited under the EU AI Act. | [2] working days |

## 3. The five possible answers

| Answer | Meaning | Record in the register |
|---|---|---|
| **Approved** | Go ahead as described. | status *assessment* or *live*, approved_by, approved_on, next_review |
| **Approved with conditions** | Go ahead, but only on the conditions written down. | As above, conditions in *notes* |
| **On hold** | We need more information, or an assessment (DPIA, contract review) must be done first. | status *intake* or *assessment*, what is missing in *notes* |
| **Sent to the AI Council** | The intensity is enhanced or strict, or the case is unclear. | status *assessment* |
| **Rejected** | Not allowed, or the risk is not worth the benefit. Give the reason. | status *retired*, reason in *notes* |

## 4. Common conditions

Pick the ones that fit. Write them in the decision so the requester knows exactly what to do.

- Only [these data categories] may be used. No special categories of personal data.
- A person reviews every output before it leaves the organisation.
- Users complete [module] of the [AI literacy plan](ai-literacy-plan.md) before getting access.
- The vendor's data processing agreement is signed and the contract is checked with the [AI Contract Clause Checker](https://contract-clause-checker.streamlit.app) before go-live.
- People affected are told that AI is involved.
- Use is limited to [team or number of users] until the review on [date].
- The tool may read [systems], and may not send, delete or pay without a person approving.

## 5. Tell the requester

Answer in writing, with the decision, the reason and any conditions. A short message is enough:

> Your request for **[use case]** is **[approved with conditions]**. Conditions: [list]. Owner: [name]. Next review: [date]. Questions: [AI Governance Lead].

## 6. Keep the promise

Count how many requests met the answer time each quarter and report it to the AI Council. If people wait too long, they stop asking and start using tools quietly. A fast "yes, with conditions" is better governance than a slow "maybe".
