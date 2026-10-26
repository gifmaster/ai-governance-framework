# 1. Principles

Six principles shape every part of this framework. When a template or a process step is unclear, go back to these.

## 1. Fit for purpose, not maximum compliance

Governance should match the risk. A spam filter and a credit scoring model do not need the same paperwork. Every control in this framework is scaled by the [governance intensity](03-oversight-scale.md#governance-intensity) of the use case, so low-risk AI moves fast and high-risk AI gets the attention it needs.

## 2. Know what is binding and what is optional

Organisations often mix up law, standards and good practice, and end up either over-engineering or missing a real obligation. This framework keeps them apart in four tiers:

| Tier | What it is | Examples | Status |
|---|---|---|---|
| 1 | Law and regulators | EU AI Act, GDPR, guidance from Digitaliseringsstyrelsen and Datatilsynet | **Must** |
| 2 | International standards | ISO/IEC 42001, ISO/IEC 23894, OECD AI Principles | **Should**, if you want to be certifiable or comparable |
| 3 | Research-based methods | AIGA Hourglass Model of organisational AI governance | **Could**, used as the structural backbone |
| 4 | Industry practice | NIST AI RMF, OWASP Top 10 for LLM and agentic applications | **Could**, picked where it fits |

Every requirement in the templates is tagged with the tier it comes from. See the [regulatory map](06-regulatory-map.md).

## 3. Most organisations are deployers

Most small and mid-sized companies do not build AI. They buy it, switch it on inside tools they already use, or call it through an API. Under the EU AI Act that makes them **deployers**, and deployers have a much shorter list of obligations than providers. The framework starts from the deployer's point of view and adds provider controls only when a company builds or substantially changes an AI system.

## 4. Governance lives in the work, not next to it

A review board that meets once a quarter will be bypassed. Governance steps belong in the places where work already happens: the intake form, the procurement checklist, the sprint, the Definition of Done. The [agile playbook](../playbook/agile-governance.md) shows how.

## 5. People first

Most AI incidents are not caused by the model. They are caused by someone who did not know the tool's limits, trusted it too much, or did not know whom to tell when it went wrong. AI literacy, clear ownership and a culture where people speak up are controls in their own right.

## 6. Calm, plain language

Governance only works if people understand it. No fear-driven messaging, no jargon where a normal word will do, and every rule should be explainable to the person who has to follow it.
