# 3. The AI Oversight Scale

The EU AI Act asks **what an AI system is used for**. That decides its risk tier. But two systems with the same risk tier can be very different in practice: one drafts a suggestion that a person reads and rewrites, the other acts on its own a thousand times a day.

The AI Oversight Scale adds the second question: **how much does the AI act on its own?**

## The five levels

| Level | Name | Who decides | Human role | Example |
|---|---|---|---|---|
| 1 | **Human-Only** | A person | Does the work | Manager writes a performance review without any AI |
| 2 | **AI-Assisted** | A person | Uses AI as a source, writes the result themselves | Employee asks a chatbot for ideas, then writes the email |
| 3 | **AI-Collaborative** | A person, on an AI proposal | Reviews **every** output before it takes effect | AI drafts a customer reply, an agent edits and sends it |
| 4 | **AI-Embedded** | The AI, inside set limits | Reviews **samples and exceptions** | AI routes incoming invoices, staff check flagged ones |
| 5 | **AI-Driven** | The AI | Sets the limits and **monitors outcomes** | AI agent adjusts prices or books resources by itself |

The level is a property of **how the AI is used**, not of the tool. The same language model can be level 2 in one team and level 4 in another.

### Controls that come with each level

| Control | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Listed in the AI register | ✓ | ✓ | ✓ | ✓ |
| Users trained on limits of the tool | ✓ | ✓ | ✓ | ✓ |
| Named human reviewer for outputs | | ✓ | ✓ | ✓ |
| Logging of AI outputs and human decisions | | ✓ | ✓ | ✓ |
| Defined limits the AI may not cross | | | ✓ | ✓ |
| Tool and data access limited to what the task needs | | | ✓ | ✓ |
| Written list of approval points for actions that cannot be undone | | | ✓ | ✓ |
| Usage and cost limits (budget, rate limit) | | | ✓ | ✓ |
| Sampling and exception review, with a set frequency | | | ✓ | ✓ |
| Stop switch and fallback to manual process | | | ✓ | ✓ |
| Outcome monitoring with alert thresholds | | | | ✓ |
| Council approval before go-live | | | | ✓ |

For AI agents that use tools and act on systems, see [agent-level controls](../docs/agent-level-controls.md), which maps these controls to the AI Act, GDPR, NIS2 and DORA.

## Governance intensity

Put the two questions together and you get the **governance intensity** of a use case. It decides how much of this framework applies.

| Risk tier ↓ / Oversight level → | 2 AI-Assisted | 3 AI-Collaborative | 4 AI-Embedded | 5 AI-Driven |
|---|---|---|---|---|
| **Minimal** | Light | Light | Standard | Enhanced |
| **Transparency** (Art. 50) | Light + disclosure | Standard + disclosure | Standard + disclosure | Enhanced + disclosure |
| **High risk** | Enhanced | Enhanced | Strict | **Redesign** |
| **Prohibited** | **Stop** | **Stop** | **Stop** | **Stop** |

- **Light.** Register entry, AI literacy, follow the AI policy. No formal approval.
- **Standard.** Intake form, risk classification on record, use case owner named, approval by the AI governance lead.
- **Enhanced.** Everything in Standard, plus a written assessment (DPIA where personal data is involved), council approval and a review at least every 12 months.
- **Strict.** Everything in Enhanced, plus all deployer obligations for high-risk systems (Art. 26), a fundamental rights impact assessment where required (Art. 27), and reviews at least every 6 months.
- **Redesign.** A high-risk system needs effective human oversight (Art. 14 and Art. 26(2)), which is very hard to show when the AI acts on its own. This framework therefore treats a high-risk use case at level 5 as a design problem: lower the oversight level before going further.
- **Stop.** Prohibited under Art. 5. Do not use.

Use the [EU AI Act Risk Check](https://ai-act-risk-check.streamlit.app) to find the risk tier, and the [use case intake template](../templates/use-case-intake.md) to record the oversight level. The [AI Use Case Register](https://ai-use-case-register.streamlit.app) calculates the intensity for you and flags entries where the recorded intensity is wrong.
