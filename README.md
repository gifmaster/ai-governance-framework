# Practical AI Governance Framework

[![checks](https://github.com/gifmaster/ai-governance-framework/actions/workflows/checks.yml/badge.svg)](https://github.com/gifmaster/ai-governance-framework/actions/workflows/checks.yml)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**A fit-for-purpose AI governance framework for small and mid-sized organisations in the EU.** Built around the EU AI Act, made to work inside the way teams already work.

Most AI governance material is written for large enterprises with compliance departments. This framework is for the company with 20 to 250 people that uses AI every day, mostly through tools it buys, and needs to get it under control without building a bureaucracy.

[Dansk resumé længere nede](#dansk-resumé)

## What is inside

| | |
|---|---|
| **[Framework](framework/)** | The model: principles, five dimensions, the AI Oversight Scale, the use case lifecycle, roles and RACI, and a regulatory map covering the AI Act, GDPR, NIS2 and DORA, with overlaps and incident deadlines |
| **[Agile playbook](playbook/agile-governance.md)** | How to run AI governance inside Scrum and SAFe, instead of as a gate at the end |
| **[Templates](templates/)** | AI policy, AI Council charter, use case intake, AI register, AI system record, incident report, backlog items |
| **[What this adds to ISO/IEC 42001 and the NIST AI RMF](docs/what-this-adds.md)** | An honest comparison, with crosswalks to both |
| **[Agent-level controls](docs/agent-level-controls.md)** | Regulation first, then controls: what an AI agent that uses tools needs, and which law (if any) asks for each control |
| **[Getting started](docs/getting-started.md)** | A 90-day plan from "we use AI" to "we govern AI" |

## The framework in one page

**Two questions decide how much governance a use case needs.**

1. **What is the AI used for?** That gives the EU AI Act risk tier: prohibited, high risk, transparency or minimal. Check it with the [EU AI Act Risk Check](https://ai-act-risk-check.streamlit.app).
2. **How much does the AI act on its own?** That gives the level on the [AI Oversight Scale](framework/03-oversight-scale.md):

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Human-Only | AI-Assisted | AI-Collaborative | AI-Embedded | AI-Driven |

Put them together and you get the **governance intensity**: light, standard, enhanced, strict, or stop. A meeting summary tool gets a register entry. A CV screening tool gets the full set of controls. Nobody wastes time on paperwork that does not reduce risk.

**Five dimensions keep it complete.** Governance, People, Process, Technology and Culture. A policy without trained people, or an approval step without a place to record it, does not work. ([more](framework/02-dimensions.md))

**One lifecycle, five gates.** Every use case goes from idea through intake, classification, assessment and operation to retirement, with gates scaled to its intensity. ([more](framework/04-use-case-lifecycle.md))

**Clear about what is law.** Every requirement is tagged as law (must), international standard (should), research method or industry practice (could). ([more](framework/06-regulatory-map.md))

## Built on

- **EU AI Act**, Regulation (EU) 2024/1689, as amended by the Digital Omnibus on AI, Regulation (EU) 2026/1744
- **GDPR** and the Danish implementation of the AI Act
- **NIS2** (Danish implementation) and **DORA**, where they apply
- **ISO/IEC 42001** (mapped clause by clause)
- **AIGA Hourglass Model** of organisational AI governance (University of Turku)
- **NIST AI RMF** and **OWASP** guidance, where useful

## Part of a toolkit

| | |
|---|---|
| [EU AI Act Risk Check](https://github.com/gifmaster/ai-act-risk-check) | Classify an AI system with transparent, cited rules. Used at the classification step of the lifecycle. |
| [AI Contract Clause Checker](https://github.com/gifmaster/contract-clause-checker) | Review AI and SaaS vendor contracts before you buy, with a DORA pack for financial entities. Supports indicator *AI in procurement*. |
| [AI Use Case Register](https://github.com/gifmaster/ai-use-case-register) | The register template as a working tool: calculated governance intensity, health checks, AI Council review |
| [Regulation Navigator](https://github.com/gifmaster/regulation-navigator) | See which of the AI Act, GDPR, NIS2 and DORA apply, where they overlap, and every incident deadline in the Incident Clock |
| This framework | The organisation around it: policy, roles, process, evidence |

## What is not included

This repository is the open part of an advisory method. The scored maturity assessment, diagnostic interview guides and client-specific implementation playbooks are part of advisory engagements and are not published here.

## Using it

Copy what you need. Adapt it. You are free to use, change and share this material inside your own organisation, as long as you credit the source. Using it in paid services or products, such as consulting, training, audits or software, needs written permission (CC BY-NC-SA 4.0, see below).

Found a mistake, or have a suggestion? [Open an issue](https://github.com/gifmaster/ai-governance-framework/issues).

## Dansk resumé

**En praktisk ramme for AI governance til små og mellemstore virksomheder i EU.**

De fleste virksomheder bygger ikke selv AI. De køber den eller slår den til i værktøjer, de allerede bruger. Det gør dem til *idriftsættere* under EU's AI-forordning, med en kortere og mere overskuelig liste af pligter.

Rammen stiller to spørgsmål til hver anvendelse: **Hvad bruges AI'en til?** (risikoniveau efter AI-forordningen) og **Hvor meget handler den på egen hånd?** (AI Oversight Scale, fra Human-Only til AI-Driven). Svarene afgør, hvor meget governance der er brug for. Et værktøj, der opsummerer møder, kræver en linje i registeret. Et værktøj, der sorterer jobansøgere, kræver hele pakken.

Indhold: principper, fem dimensioner (governance, mennesker, processer, teknologi og kultur), en livscyklus med fem beslutningspunkter, roller og RACI, en kobling til AI-forordningen og ISO/IEC 42001, en playbook til at drive AI governance i Scrum og SAFe, skabeloner og en 90-dages plan.

Rammen kobler også AI-forordningen til GDPR, NIS2 og DORA: hvor de overlapper, og hvilke indberetningsfrister der starter, når noget går galt.

Danske myndigheder for AI-forordningen er Digitaliseringsstyrelsen, Datatilsynet og Domstolsstyrelsen. For NIS2 er det Styrelsen for Samfundssikkerhed og sektormyndighederne, og for DORA Finanstilsynet.

Rammen hænger sammen med fire gratis værktøjer: EU AI Act Risk Check, AI Contract Clause Checker, AI Use Case Register og Regulation Navigator.

Materialet er på engelsk og må frit bruges og tilpasses i egen organisation med kildeangivelse. Brug i betalte ydelser eller produkter, fx rådgivning, kurser, audits eller software, kræver skriftlig tilladelse.

## About

Created by **Alexander Senderovitz**, AI governance and digital transformation, Copenhagen.
[senderovitz.eu](https://senderovitz.eu) · [alexander@senderovitz.eu](mailto:alexander@senderovitz.eu)

Need help putting it into practice? Get in touch.

## License

[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](LICENSE.md). Credit: *"Practical AI Governance Framework" by Alexander Senderovitz, CC BY-NC-SA 4.0.*

Free to use inside your own organisation. Using it in paid services or products needs permission: [alexander@senderovitz.eu](mailto:alexander@senderovitz.eu).

This framework is practical guidance, not legal advice.
