# Agent-level controls: regulation first, then controls

Many AI tools no longer just answer. They read from your systems, call other tools and take actions: send the email, update the record, place the order. This note shows which controls such an **AI agent** needs and, for each one, whether a law asks for it or whether it is good practice.

It does not add a new model. An agent is a use case like any other, and it is governed with the same framework: find the risk tier, set the oversight level, apply the controls that come with them. Agents simply tend to sit at the high end of the [AI Oversight Scale](../framework/03-oversight-scale.md) (levels 4 and 5), where more controls apply.

*Not legal advice. Checked against the law as of October 2026. Whether a law applies to you depends on your organisation and sector; see the [regulatory map](../framework/06-regulatory-map.md).*

## Step 1: Regulation first

Before you pick controls, find out which duties you actually have. Work through four questions.

| Question | If yes | Where to look |
|---|---|---|
| Which EU AI Act tier is the use case in? | High risk brings the deployer duties in Art. 26. Transparency brings Art. 50. Prohibited means stop. | [EU AI Act Risk Check](https://ai-act-risk-check.streamlit.app) |
| Does the agent touch personal data? | GDPR applies in full: lawful basis, minimisation, security, DPIA where needed, rules on automated decisions. | [Regulation Navigator](https://regulation-navigator.streamlit.app) |
| Are you in a NIS2 sector and above the size threshold? | Supply chain security, access control and incident reporting duties cover the agent and its vendors. | Regulation Navigator |
| Are you a financial entity? | DORA applies instead of NIS2. Every AI tool you buy is an ICT service. | Regulation Navigator, [DORA pack](https://contract-clause-checker.streamlit.app) |

Most agents in small organisations are not high risk. That does not make them uncontrolled: GDPR, security duties and plain good practice still apply.

## Step 2: Then controls

**Law** means a legal duty exists for some organisations, depending on the answers above. **Practice** means no law asks for it directly, but it is how you make the legal duties and your own limits work in an agent.

| Control | What it means for an agent | Law | Practice | Framework home |
|---|---|---|---|---|
| **Agent registry** | Every agent is in the AI register, with the tools and data it is connected to and a named owner | DORA Art. 8 and Art. 28(3) (register of information, financial entities); GDPR Art. 30 where personal data is processed | Owner per agent; the register shows connections, not just the product name | [AI register](../templates/ai-register.csv), lifecycle gate G1 |
| **Tool and data permissions** | The agent can reach only the systems and data its task needs, and read access is kept apart from write access | GDPR Art. 5(1)(c), 25 and 32; NIS2 Art. 21(2)(i) (access control); DORA Art. 9(4)(c) | Separate service account per agent; no shared admin rights | Oversight level 4: "defined limits the AI may not cross" |
| **Human approval points** | A person approves actions that cannot be undone, leave the organisation, move money or change personal data | AI Act Art. 14 and 26(2) (high-risk systems); GDPR Art. 22 (decisions based solely on automated processing); Art. 86 | Decide the list of approval points before go-live, and write it in the system record | Oversight levels 3 to 5, stop switch |
| **Memory and retention** | Decide what the agent may remember between tasks, for whom, and for how long | GDPR Art. 5(1)(c) and (e), Art. 17; AI Act Art. 26(6) sets a floor of six months for logs of high-risk systems | One retention rule per agent, applied to memory, logs and caches alike | [Log retention overlap](../framework/06-regulatory-map.md#where-the-laws-overlap) |
| **Logging and monitoring** | Record inputs, tool calls, outputs and approvals so that a decision can be reconstructed and unusual behaviour is noticed | AI Act Art. 26(5) and 26(6) (deployer, high-risk); Art. 12 puts the duty to build in logging on the provider; GDPR Art. 5(2); NIS2 Art. 21(2)(b); DORA Art. 10 | Alerts on unusual volume, new tools or repeated failures | Oversight level 3 (logging) and 5 (outcome monitoring) |
| **Stop switch and incident route** | Anyone responsible can switch the agent off, fall back to the manual process and report an incident to the right authority in time | GDPR Art. 33; NIS2 Art. 23; DORA Art. 17 and 19; AI Act Art. 26(5) and 73 | Test the stop switch, not just write it down | [One incident, several clocks](../framework/06-regulatory-map.md#one-incident-several-clocks), [incident report](../templates/incident-report.md) |
| **Vendors and connectors** | The model provider, the agent platform and every connected tool are suppliers, with contracts that cover security, subprocessors, audit and exit | GDPR Art. 28; NIS2 Art. 21(2)(d); DORA Art. 28 and 30 | Review each contract once against all that apply | [AI Contract Clause Checker](https://contract-clause-checker.streamlit.app) |
| **Disclosure and literacy** | People who deal with the agent are told they are dealing with AI where the law requires it, and the staff who supervise it are trained | AI Act Art. 4 (literacy); Art. 50 (transparency: for chatbots mainly the provider's duty, for emotion recognition, deepfakes and AI-written public text the deployer's); Art. 26(7) (informing workers) | Short training for each overseer on what this agent can and cannot do | [AI policy](../templates/ai-policy.md) |
| **Usage and cost limits** | A budget, rate limit or quota per agent, so a loop or misuse cannot run unnoticed | No direct duty in these laws | A spend cap and a volume cap per agent, reviewed monthly. It also limits the damage of an error | Oversight level 4: "defined limits the AI may not cross" |

The last row is the honest one: usage and cost limits are not a legal requirement. They belong in the framework because a hard limit is the simplest limit to enforce.

## What changes by oversight level

The [controls that come with each level](../framework/03-oversight-scale.md#controls-that-come-with-each-level) already cover most of this. For agents, three things need to be made explicit:

| Level | Add for agents |
|---|---|
| **3 AI-Collaborative** | Tool permissions are read-only unless a person sends the result |
| **4 AI-Embedded** | A written list of approval points, tool and data permissions limited to the task, and usage and cost limits |
| **5 AI-Driven** | Everything at level 4, plus outcome monitoring with alert thresholds and a tested stop switch. If the use case is high risk, redesign first |

## Worked example

A mid-sized company lets an agent handle supplier invoices. It reads incoming invoices, matches them to orders and books them in the accounting system.

- **Regulation.** Minimal risk tier under the AI Act. Personal data is limited (contact names), so GDPR applies. The company is in a NIS2 sector, so the agent platform is a supplier under Art. 21(2)(d). Not a financial entity.
- **Oversight level.** 4: the agent books routine invoices by itself, a person reviews flagged ones and samples.
- **Controls.** Registry entry with the accounting system and the mailbox as connections, and a named owner. Write access only to the invoice ledger, not to payments. Human approval for any invoice above a set amount and for any change of bank details. Logs kept per the company's retention rule. A monthly spend cap. A stop switch that sends invoices back to the manual queue. A contract review of the platform vendor.

The same agent used to screen CV applications would be high risk (Annex III, employment). At oversight level 5 the framework says redesign: add a human decision before the result takes effect.

## Limits of this note

- It covers deployers. If you build or market an agent, you may be a provider with far more duties (Art. 25 and Arts. 9 to 17).
- Duties for providers of general-purpose AI models are outside this note.
- Security testing of agents (prompt injection, tool abuse) needs a specialist and is out of scope, as in the rest of the framework.
- The articles cited are the main hooks, not a complete list. Check the source before you rely on one.
