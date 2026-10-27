# 6. Regulatory map

This chapter connects the framework to its sources, so you can show an auditor, a customer or a regulator where each control comes from.

## Tier 1: Law and regulators (must)

### EU AI Act: deployer obligations

Regulation (EU) 2024/1689, as amended by the Digital Omnibus on AI, Regulation (EU) 2026/1744.

| Obligation | Article | Applies from | Where in this framework |
|---|---|---|---|
| AI literacy for staff and others using AI on your behalf | Art. 4 | 2 Feb 2025 | [AI policy](../templates/ai-policy.md) section 6, RACI |
| Do not use prohibited practices | Art. 5 | 2 Feb 2025 (new bans from 2 Dec 2026) | Policy section 4, gate G1 |
| Transparency: tell people about chatbots, emotion recognition, deepfakes, AI-written public text | Art. 50 | 2 Aug 2026 | Intensity matrix, intake form |
| Use high-risk systems according to instructions | Art. 26(1) | 2 Dec 2027 | Lifecycle stage 4 and 6 |
| Assign competent human oversight | Art. 26(2) | 2 Dec 2027 | Human Overseer role, oversight scale |
| Relevant and representative input data you control | Art. 26(4) | 2 Dec 2027 | AI system record |
| Monitor, report risks and serious incidents | Art. 26(5) | 2 Dec 2027 | Lifecycle stage 6 and 7, incident report |
| Keep logs for at least six months | Art. 26(6) | 2 Dec 2027 | AI system record, oversight controls |
| Inform workers before using high-risk AI at work | Art. 26(7) | 2 Dec 2027 | Intake form, go-live checklist |
| Inform people affected by high-risk decisions | Art. 26(11) | 2 Dec 2027 | AI system record |
| Fundamental rights impact assessment (public bodies, credit, life and health insurance) | Art. 27 | 2 Dec 2027 | Strict intensity, RACI |
| Explain individual decisions on request | Art. 86 | 2 Dec 2027 | AI system record |

If you **build** an AI system, or substantially modify one, or put your name on it, you may become a **provider** (Art. 25) with a much longer list of obligations (Arts. 9 to 17, 43, 49, 72, 73). Get legal advice before that happens.

Dates for high-risk systems listed in Annex III. High-risk AI in products covered by Annex I applies from 2 Aug 2028.

### Other law that meets AI

Most organisations meet AI governance through several laws at once. Check which apply with the [Regulation Navigator](https://regulation-navigator.streamlit.app).

- **GDPR**, Regulation (EU) 2016/679. Most AI use cases process personal data. Lawful basis, DPIA (Art. 35), rules on automated decisions (Art. 22) and transparency (Arts. 13 and 14) still apply in full.
- **NIS2**, Directive (EU) 2022/2555, in Denmark implemented by Act No. 434 of 2025 (most sectors), Act No. 258 of 2025 (energy) and Act No. 435 of 2025 (telecom). Applies to medium-sized and large entities in the sectors in Annexes I and II, and to some entities regardless of size. In Denmark the size threshold does not apply to energy and telecom companies. Key duties: register with the authorities, management approval of and training in cybersecurity measures (Art. 20), minimum security measures including supply chain security (Art. 21(2)), and incident reporting (Art. 23). AI vendors are part of the supply chain.
- **DORA**, Regulation (EU) 2022/2554, applies from 17 January 2025 to financial entities such as banks, insurers, pension funds and investment firms, with some exemptions. For these entities DORA applies instead of NIS2. Every AI tool a financial entity buys is an ICT service: it belongs in the register of information (Art. 28(3)), its contract must contain the key provisions of Art. 30, there must be an exit strategy (Art. 28(8)), and major ICT-related incidents are reported to Finanstilsynet (Art. 19). Check contracts with the DORA pack in the [AI Contract Clause Checker](https://contract-clause-checker.streamlit.app).
- **Sector rules.** Consumer credit, medical devices (MDR), employment law and collective agreements can add requirements.

### Where the laws overlap

One piece of work can serve several laws. This is where most of the saving is for a small organisation.

| Overlap | What to do once | Sources |
|---|---|---|
| DPIA and high-risk AI | Do the DPIA with the AI provider's instructions for use in hand, not as a separate project | AI Act Art. 26(9); GDPR Art. 35 |
| FRIA and DPIA | Run the fundamental rights impact assessment and the DPIA as one piece of work | AI Act Art. 27(4); GDPR Art. 35 |
| AI vendor contracts | Review each AI contract once against DORA, GDPR and the AI Act | DORA Art. 30; GDPR Art. 28; AI Act Art. 26 |
| Supply chain | Keep one register of AI use cases and vendors for AI governance and NIS2 supply chain security | NIS2 Art. 21(2)(d); AI Act Art. 26 |
| Management training | Combine training on cyber and ICT risk with AI literacy | NIS2 Art. 20(2); DORA Art. 5(4); AI Act Art. 4 |
| Automated decisions | Design one human review step that meets GDPR Art. 22 and AI Act human oversight | GDPR Art. 22; AI Act Art. 14, 26(2), 86 |
| Log retention | Set and document one retention period: at least six months under the AI Act, no longer than necessary under GDPR | AI Act Art. 26(6); GDPR Art. 5(1)(e) |

### One incident, several clocks

An incident involving an AI system can be a personal data breach, a significant NIS2 incident, a major DORA incident and a serious AI incident at the same time. Each has its own deadline, counted from a different moment, and its own recipient. Agree in advance who reports what, and test it. The Incident Clock in the [Regulation Navigator](https://regulation-navigator.streamlit.app) lists every deadline that starts, in order.

| Regulation | Report | Deadline | To |
|---|---|---|---|
| GDPR | Personal data breach | 72 hours after becoming aware (Art. 33); people affected without undue delay if high risk (Art. 34) | Datatilsynet |
| NIS2 | Early warning, notification, final report | 24 hours, 72 hours, then one month after the notification (Art. 23(4)) | The Danish CSIRT, via the national reporting solution |
| DORA | Initial, intermediate, final report | 4 hours after classifying the incident as major and no later than 24 hours after becoming aware, then 72 hours, then one month (Art. 19; Delegated Regulation (EU) 2025/301 Art. 5) | Finanstilsynet |
| AI Act | Serious incident | Deployers inform the provider immediately (Art. 26(5)). The provider reports within 15 days, 2 days if widespread, 10 days on death (Art. 73). From 2 Dec 2027 for Annex III systems | Market surveillance authority |

### Danish authorities

Under the Danish act supplementing the AI Act (in force 2 Aug 2025):

| Authority | Role |
|---|---|
| **Digitaliseringsstyrelsen** (Agency for Digital Government) | Notifying authority, market surveillance authority and single point of contact |
| **Datatilsynet** (Data Protection Authority) | Market surveillance authority, and the GDPR regulator |
| **Domstolsstyrelsen** (Court Administration) | Market surveillance authority for its area |

Other Danish authorities you may meet:

| Authority | Role |
|---|---|
| **Styrelsen for Samfundssikkerhed** (Agency for Civil Protection and Emergency Management) | Central NIS2 authority, alongside sector authorities |
| **Finanstilsynet** (Financial Supervisory Authority) | DORA supervisor for financial entities |

## Tier 2: International standards (should)

How the framework lines up with **ISO/IEC 42001:2023** (AI management systems):

| ISO/IEC 42001 clause | Framework element |
|---|---|
| 4 Context of the organisation | Principles, AI register, role as deployer or provider |
| 5 Leadership | Management accountability, AI policy, roles and RACI |
| 6 Planning | Risk classification, governance intensity |
| 7 Support | AI literacy, competence of human overseers, documented information |
| 8 Operation | Use case lifecycle, assessments, vendor checks |
| 9 Performance evaluation | Monitoring, periodic review (G4), council's quarterly register review |
| 10 Improvement | Incident reports, annual framework review |

This mapping helps if you later want certification. It is not a substitute for the standard itself. Also relevant: ISO/IEC 23894 (AI risk management) and the OECD AI Principles.

## Tier 3: Research-based method (could)

The structure draws on the **AIGA Hourglass Model of Organizational AI Governance** (Mäntymäki et al., University of Turku), which connects the environmental layer (law, standards, stakeholders), the organisational layer (strategy, values, roles) and the AI system layer (lifecycle controls). In this framework, the environmental layer is the regulatory map, the organisational layer is the five dimensions and the roles, and the AI system layer is the lifecycle and the oversight scale.

## Tier 4: Industry practice (could)

| Source | Used for |
|---|---|
| NIST AI Risk Management Framework 1.0 (Govern, Map, Measure, Manage) | Cross-check of the lifecycle, risk vocabulary |
| OWASP Top 10 for LLM Applications and the agentic AI guidance | Security questions in the intake form and system record |

AI security testing itself is out of scope for this framework. Bring in a specialist for that.

---

*Checked against the law as of October 2026. Digital Omnibus proposals for GDPR and a single incident reporting point are not included until adopted. This is a practical map, not legal advice.*
