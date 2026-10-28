# What does this framework add to ISO/IEC 42001 and the NIST AI RMF?

A fair question. Both are respected, widely used, and ISO/IEC 42001 can be certified. This page says where this framework helps, where it does not, and how the three line up.

## Short answer

ISO/IEC 42001 tells you what an AI management system must contain. The NIST AI RMF tells you what good AI risk management looks like. Neither tells a 50 to 500 person company in the EU what to do on Monday, in what order, with which template, for which law. This framework does that, and it points back to both standards so you can grow into them.

| | ISO/IEC 42001 | NIST AI RMF 1.0 | This framework |
|---|---|---|---|
| Nature | Certifiable management system standard | Voluntary risk management guidance | Open, practical method with templates |
| Law-specific | No | No (US origin) | Yes: EU AI Act, GDPR, NIS2, DORA, Danish authorities |
| Tells you how much governance a use case needs | Leaves it to your risk assessment | Leaves it to you | Yes: risk tier plus oversight level give a governance intensity |
| Templates | No | Playbook with suggested actions | Policy, council charter, intake, register, incident report |
| Certification | Yes | No | No |
| Cost | Standard must be bought | Free | Free inside your own organisation (CC BY-NC-SA 4.0) |

## Where this framework is stronger

- **It starts from the law you are subject to.** A European company needs the AI Act tier first. The framework makes that the first question and links tools that answer it.
- **It scales effort to the use case.** A meeting summary and a CV screening tool should not get the same paperwork. The governance intensity does that explicitly.
- **It is usable in a week.** The 90-day plan and templates are meant to be copied, not studied.
- **It joins the neighbouring laws.** Incident deadlines under GDPR, NIS2, DORA and the AI Act sit in one view.

## Where it is weaker, or does not try

- **No certification.** If a customer demands an ISO/IEC 42001 certificate, you need the standard and an accredited auditor. This framework can give you a head start on the documents, not the certificate.
- **Thin on measurement.** The NIST AI RMF Measure function covers testing, metrics, bias and robustness evaluation in depth. This framework asks you to document and review them but does not teach the methods.
- **No AI security testing.** Out of scope on purpose. Bring a specialist.
- **A framework is not a system.** It does not run your approvals or keep your evidence. See the [AI Use Case Register](https://github.com/gifmaster/ai-use-case-register) for a light version, or a GRC platform for more.

## ISO/IEC 42001 crosswalk

Clauses 4 to 10 are mapped in the [regulatory map](../framework/06-regulatory-map.md). The Annex A control areas line up like this:

| Annex A area | Where to look in this framework |
|---|---|
| A.2 Policies related to AI | [AI policy template](../templates/ai-policy.md) |
| A.3 Internal organisation | [Roles and RACI](../framework/05-roles-and-raci.md), [AI council charter](../templates/ai-council-charter.md) |
| A.4 Resources for AI systems | [System record](../templates/ai-system-record.md) |
| A.5 Assessing impacts of AI systems | Assessment gate in the [lifecycle](../framework/04-use-case-lifecycle.md), DPIA and FRIA flags in the register |
| A.6 AI system life cycle | [Use case lifecycle](../framework/04-use-case-lifecycle.md), [oversight scale](../framework/03-oversight-scale.md) |
| A.7 Data for AI systems | System record (data section), intake form |
| A.8 Information for interested parties | Transparency items in the intake form and incident report |
| A.9 Use of AI systems | AI policy, human oversight levels |
| A.10 Third-party and customer relationships | Vendor checks, with the [Contract Clause Checker](https://github.com/gifmaster/contract-clause-checker) |

Treat this as a pointer to where evidence would live. Whether it satisfies a control is for the auditor to decide.

## NIST AI RMF crosswalk

| Function | What it asks | Where to look in this framework | Coverage |
|---|---|---|---|
| Govern | Policies, accountability, culture | [Principles](../framework/01-principles.md), [roles](../framework/05-roles-and-raci.md), policy and council templates | Good |
| Map | Understand context and purpose, classify risk | Intake form, EU AI Act classification, register | Good |
| Measure | Test, monitor and evaluate risks | Assessment gate, periodic review, incident report | Partial: documents the work, does not teach the methods |
| Manage | Prioritise and act on risks | Lifecycle gates, governance intensity, retirement | Good |

## Which should you use?

- **You only need to comply with EU law and want to start now:** this framework, plus the tools.
- **A customer asks for ISO/IEC 42001:** use this to get the documents in shape, then buy the standard and plan an audit.
- **You are a global group with US exposure:** keep the NIST AI RMF vocabulary alongside, and use this framework for the EU entities.
