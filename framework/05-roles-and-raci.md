# 5. Roles and RACI

## Roles

| Role | Who it usually is | Responsibility |
|---|---|---|
| **Management** | CEO or executive team | Approves the AI policy and appetite for AI risk. Accountable overall. |
| **AI Council** | 3 to 6 people across business, IT, legal/DPO and HR | Approves enhanced and strict use cases, resolves disputes, reviews the register every quarter. See the [council charter](../templates/ai-council-charter.md). |
| **AI Governance Lead** | One named person, often part-time | Runs the framework day to day: register, intake, classification, training plan, reporting. |
| **Use Case Owner** | Business manager who wants the AI | Owns one use case through its lifecycle, from intake to retirement. |
| **Human Overseer** | People who review AI outputs | Monitors the system in use and can intervene or stop it. Must have competence, training and authority (Art. 26(2)). |
| **DPO / Privacy** | Data protection officer or privacy lead | Personal data questions, DPIAs. |
| **IT and Security** | IT manager, security lead | Technical setup, access, logging, vendor integration, security review. |
| **Legal and Compliance** | In-house or external counsel | Contracts, regulatory interpretation, sign-off on high-risk classifications. |
| **Procurement** | Purchasing | Makes sure AI tools enter through intake, not by credit card. |
| **All employees** | Everyone | Follow the AI policy, use approved tools, report problems. |

## RACI

R = Responsible (does it), A = Accountable (owns the outcome), C = Consulted, I = Informed

| Activity | Mgmt | Council | Gov. Lead | UC Owner | Overseer | DPO | IT/Sec | Legal | Proc. |
|---|---|---|---|---|---|---|---|---|---|
| Approve AI policy | **A** | R | C | | | C | C | C | |
| Maintain AI register | I | I | **A/R** | C | | | C | | |
| Submit use case intake | | | C | **A/R** | | | | | C |
| Classify risk and oversight level | | C | **A**/R | R | | C | C | C | |
| DPIA | | I | C | R | | **A** | C | C | |
| Fundamental rights impact assessment | | C | R | R | | C | | **A** | |
| Vendor assessment | | | C | R | | C | R | C | **A** |
| Go-live approval (enhanced, strict) | I | **A**/R | R | R | C | C | C | C | |
| Assign and train human overseers | | | C | **A** | R | | | | |
| Monitor in operation | | I | I | **A** | R | | R | | |
| Handle AI incident | I | I | R | **A** | R | C | R | C | |
| AI literacy training (Art. 4) | **A** | I | R | C | | | | | |
| Annual framework review | **A** | R | R | C | | C | C | C | |

## Minimum viable setup

A company with 20 people does not need nine roles. A workable minimum is:

- **Management** keeps accountability and approves the policy.
- **One AI Governance Lead** who also chairs a small council.
- **The council** is the governance lead plus one person from the business and the DPO or an external adviser, meeting every quarter or when a strict use case comes up.
- **Use case owners** and **human overseers** are named per use case.

One person can hold several roles. The one combination to avoid is the same person approving and owning a high-risk use case.
