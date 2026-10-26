# AI use case intake

> Fill in one form per use case. It should take 15 minutes. If you do not know an answer, write "don't know", that is useful information too. Each field matches a column in the [AI register](ai-register.csv).

## About the use case

| Field | Answer |
|---|---|
| **use_case_id** | *Assigned by the AI Governance Lead* |
| **name** | Short name, e.g. "Customer email drafting" |
| **purpose** | What problem does it solve? What will the AI do? |
| **business_unit** | |
| **use_case_owner** | Name of the manager responsible |
| **status** | idea / intake / assessment / live / retired |

## The AI system

| Field | Answer |
|---|---|
| **ai_system** | Name of the tool or model |
| **vendor** | Company providing it, or "internal" |
| **our_role** | **Deployer** (we use it) or **provider** (we build it or sell it under our name). Most companies are deployers. |

## People and data

| Field | Answer |
|---|---|
| **affected_people** | Who is affected by the outputs? (employees, applicants, customers, citizens, ...) |
| **personal_data** | yes / no. If yes, which kinds? Any special categories (health, ethnicity, ...)? |
| Where does the data go? | Stays with us / vendor in EU / vendor outside EU / don't know |

## How the AI is used

| Field | Answer |
|---|---|
| **oversight_level** | 2 AI-Assisted / 3 AI-Collaborative / 4 AI-Embedded / 5 AI-Driven. See the [AI Oversight Scale](../framework/03-oversight-scale.md). |
| Who reviews outputs, and how often? | |
| Can we switch it off and go back to the manual process? | |

## Quick screening

Tick anything that applies. Any tick here means the governance lead will look closer.

- [ ] Used in hiring, promotion, task allocation, performance or termination
- [ ] Used to decide on credit, insurance, benefits, education or access to services
- [ ] Recognises emotions, or uses biometrics (face, voice, fingerprint)
- [ ] Talks directly to people (chatbot, voice assistant)
- [ ] Generates images, audio, video or text that will be published
- [ ] Acts on its own without a person checking each output
- [ ] Used by or on behalf of a public authority

## Classification *(completed by the AI Governance Lead)*

| Field | Answer |
|---|---|
| **eu_ai_act_tier** | prohibited / high / limited / minimal / out_of_scope. Check with the [EU AI Act Risk Check](https://ai-act-risk-check.streamlit.app). |
| **governance_intensity** | light / standard / enhanced / strict / redesign / stop |
| **dpia_required** | yes / no |
| **fria_required** | yes / no |
| **approved_by** | Name or "AI Council" |
| **approved_on** | Date |
| **next_review** | Date |
| **notes** | |
