# Governance backlog items

Ready-to-copy enablers for the [agile playbook](../playbook/agile-governance.md). Paste them into Jira, Azure DevOps or any other tool and adjust.

---

### Update AI register entry

**As** the AI Governance Lead, **I want** the register entry for [use case] to reflect this change, **so that** our inventory stays accurate.

**Acceptance criteria**
- Purpose, data, vendor and oversight level in the register match the delivered feature
- Status and next review date are set

*Intensity: all*

---

### Design human oversight

**As** the use case owner, **I want** a clear design for how people review and can stop [system], **so that** we keep effective human oversight.

**Acceptance criteria**
- Named overseer role, with what they review and how often
- A working way to override or stop the system, and a fallback process
- Overseers trained before go-live
- Documented in the AI system record, section 4

*Intensity: level 3 and up. Required for high-risk (Art. 14, 26(2))*

---

### Set up logging and retention

**As** IT, **I want** AI outputs and human decisions to be logged and kept for [period], **so that** we can monitor, investigate and prove compliance.

**Acceptance criteria**
- Logs capture input reference, output, timestamp and reviewer decision
- Retention set to at least six months for high-risk systems (Art. 26(6))
- Access to logs limited to named roles

*Intensity: level 3 and up*

---

### Add AI disclosure

**As** a user, **I want** to know when I am talking to an AI or reading AI-generated content, **so that** I can judge it accordingly.

**Acceptance criteria**
- Clear notice at the first interaction, or label on the generated content
- Wording approved by the use case owner

*Intensity: when Art. 50 applies*

---

### Complete DPIA

**As** the DPO, **I want** a DPIA for [use case], **so that** risks to people's data are identified and handled before go-live.

**Acceptance criteria**
- DPIA completed and signed off by the DPO
- Required mitigations added to the backlog

*Intensity: enhanced and up, when personal data is processed (GDPR Art. 35)*

---

### Complete fundamental rights impact assessment

**As** legal, **I want** a fundamental rights impact assessment for [use case] before first use, **so that** we meet Art. 27.

**Acceptance criteria**
- Assessment covers the process, affected groups, risks of harm, oversight measures and actions if risks materialise
- Result notified to the market surveillance authority where required

*Intensity: strict, for public bodies and for credit or life and health insurance use cases*

---

### Inform workers

**As** HR, **I want** employees and their representatives informed before [system] is used at work, **so that** we meet Art. 26(7) and our agreements.

**Acceptance criteria**
- Information given before go-live, in line with collective agreements
- Record of when and how in the AI system record

*Intensity: strict, workplace use*

---

### Vendor documentation review

**As** procurement, **I want** the vendor's instructions for use, data processing terms and training-data statement reviewed, **so that** we know what we are buying.

**Acceptance criteria**
- Documents stored and linked in the AI system record
- Gaps raised with the vendor or accepted by the use case owner

*Intensity: standard and up*
