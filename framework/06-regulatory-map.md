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

### Other law

- **GDPR.** Most AI use cases process personal data. Lawful basis, DPIA (Art. 35), rules on automated decisions (Art. 22) and transparency (Arts. 13 and 14) still apply in full.
- **Sector rules.** Financial services (DORA, consumer credit), medical devices (MDR), employment law and collective agreements can add requirements.

### Danish authorities

Under the Danish act supplementing the AI Act (in force 2 Aug 2025):

| Authority | Role |
|---|---|
| **Digitaliseringsstyrelsen** (Agency for Digital Government) | Notifying authority, market surveillance authority and single point of contact |
| **Datatilsynet** (Data Protection Authority) | Market surveillance authority, and the GDPR regulator |
| **Domstolsstyrelsen** (Court Administration) | Market surveillance authority for its area |

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

*Checked against the law as of October 2026. This is a practical map, not legal advice.*
