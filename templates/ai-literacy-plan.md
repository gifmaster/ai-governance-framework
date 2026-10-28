# AI literacy plan: [Organisation name]

| | |
|---|---|
| Version | 1.0 |
| Owner | [AI Governance Lead] |
| Approved by | [Management] |
| Next review | [Date, at most 12 months later] |

> **How to use this template.** Replace everything in [brackets] and delete these notes. The plan says who learns what, and the [training log](training-log.csv) proves it happened. Keep both: when a customer, auditor or authority asks what you do about AI literacy, they are your answer.

## 1. What the law asks

Providers and deployers of AI systems must **take measures to support** a sufficient level of AI literacy among their staff and others who operate AI systems on their behalf, taking into account their knowledge, experience, education and training, and the context the systems are used in. *(EU AI Act Art. 4, as amended by the Digital Omnibus on AI, Regulation (EU) 2026/1744)*

What that means in practice:

- It applies to every organisation that uses AI at work, whatever the risk tier. A meeting summary tool is enough.
- It asks for measures, not a guaranteed level of knowledge for each person. The amended text says so explicitly.
- Measures should fit the role and the tools. One generic e-learning for everyone is weak evidence.
- Keep a record. The law does not prescribe one, but without a record you cannot show what you did.

Related duties, where they apply:

- **High-risk AI systems:** deployers must give human oversight to people with the necessary competence, training and authority *(Art. 26(2), for Annex III systems from 2 December 2027)*.
- **NIS2 entities:** management must follow cybersecurity training *(NIS2 Art. 20(2))*. **DORA financial entities:** the management body keeps up to date on ICT risk *(DORA Art. 5(4))*. Combine these with AI literacy where you can.

## 2. Who learns what

| Group | Who | Topics | Format and length | When |
|---|---|---|---|---|
| **All staff** | Everyone who may use AI at work | What AI can and cannot do. Our [AI policy](ai-policy.md) and [acceptable use](acceptable-use.md). Data rules. Checking outputs. How to report a problem. | [Live session or e-learning, 45 to 60 min] | Within [4 weeks] of starting, refresh every [12 months] |
| **Frequent users** | People who use AI tools daily, or for customer-facing work | The tools they use: strengths, known failure modes, settings, what data may go in. Labelling AI content. | [Hands-on workshop, 1 to 2 hours, per tool] | Before access to the tool, refresh when the tool changes |
| **Overseers** | People who review, approve or can stop an AI system's output as part of their job | How the specific system works and fails. What to check, how often, when to intervene, how to stop it, how to record decisions. Automation bias. | [Briefing per system, 1 to 2 hours, with the use case owner] | Before go-live, refresh every [12 months] or when the system changes |
| **Management** | Management team and board | Where we use AI, our risk appetite, the regulatory map, their accountability. | [Briefing, 60 to 90 min] | Once a year |
| **AI Governance Lead and AI Council** | The people who classify and decide | The EU AI Act and related laws, classification, this framework, the tools. | [Course or external training] | Once a year, and after major legal changes |

## 3. Which systems need overseer training

Every use case with **enhanced** or **strict** [governance intensity](../framework/03-oversight-scale.md#governance-intensity) needs at least one named, trained overseer before go-live. Record the use case ID in the training log so the link can be checked.

## 4. Evidence to keep

| Evidence | Where |
|---|---|
| Who was trained, in what, when, by whom | [Training log](training-log.csv) |
| The material used, with version and date | [Folder or link] |
| Attendance lists or e-learning completion reports | [Folder or link], referenced in the log's *evidence* column |
| This plan, approved and dated | [Folder or link] |

The log's columns: *learner_group* (all_staff, frequent_user, overseer, management or governance), *audience* (who), *people* (how many), *module* (the topic), *use_case_id* (the use cases the training covers, separated by semicolons), *delivered_on*, *delivered_by*, *format*, *evidence* (where the proof is) and *next_refresh*. The same columns open in the [AI Use Case Register](https://ai-use-case-register.streamlit.app).

Log groups rather than individuals where that is enough ("Customer Service team, 14 people"). Individual records are personal data: keep them only as long as you need them, and follow your usual HR retention rules.

## 5. How we know it works

- Check the training log every quarter: missing groups, overdue refreshes, systems without trained overseers. The [AI Use Case Register](https://ai-use-case-register.streamlit.app) runs these checks on the log and the register together.
- Ask staff once a year how confident they feel using AI and where they need help.
- Look at incidents: if one was caused by someone not knowing a tool's limits, update the training.

## 6. Review

This plan is reviewed at least once a year, and when we add a new type of AI use, a tool changes significantly, or the law changes.
