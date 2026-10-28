# Anmodning om en ny AI-anvendelse

> Udfyld én anmodning pr. anvendelse. Det tager omkring 15 minutter. Kender du ikke svaret, så skriv "ved ikke". Det er også nyttig information. Feltnavnene i parentes svarer til kolonnerne i [AI-registeret](../ai-register.csv), så svarene kan kopieres direkte over.

## Om anvendelsen

| Felt | Svar |
|---|---|
| ID (use_case_id) | *Tildeles af den AI-ansvarlige* |
| Navn (name) | Kort navn, fx "Udkast til kundemails" |
| Formål (purpose) | Hvilket problem løser det? Hvad skal AI'en gøre? |
| Afdeling (business_unit) | |
| Ejer (use_case_owner) | Navnet på den ansvarlige leder |
| Status (status) | idea / intake / assessment / live / retired |

## AI-systemet

| Felt | Svar |
|---|---|
| AI-system (ai_system) | Navnet på værktøjet eller modellen |
| Leverandør (vendor) | Firmaet bag, eller "intern" |
| Vores rolle (our_role) | **Idriftsætter** (deployer: vi bruger det) eller **udbyder** (provider: vi bygger det eller sælger det under vores navn). De fleste virksomheder er idriftsættere. |

## Mennesker og data

| Felt | Svar |
|---|---|
| Berørte personer (affected_people) | Hvem påvirkes af resultaterne? (medarbejdere, ansøgere, kunder, borgere, ...) |
| Personoplysninger (personal_data) | ja / nej. Hvis ja, hvilke? Følsomme oplysninger (helbred, etnisk oprindelse, ...)? |
| Hvor ender data? | Bliver hos os / leverandør i EU / leverandør uden for EU / ved ikke |

## Sådan bruges AI'en

| Felt | Svar |
|---|---|
| Tilsynsniveau (oversight_level) | 2 AI-Assisted / 3 AI-Collaborative / 4 AI-Embedded / 5 AI-Driven. Se [AI Oversight Scale](../../framework/03-oversight-scale.md). |
| Hvem gennemgår resultaterne, og hvor ofte? | |
| Kan vi slukke for det og gå tilbage til den manuelle proces? | |

## Hurtig screening

Sæt kryds ved alt, der passer. Ét kryds betyder, at den AI-ansvarlige kigger nærmere.

- [ ] Bruges til ansættelse, forfremmelse, fordeling af opgaver, vurdering af medarbejdere eller afskedigelse
- [ ] Bruges til at afgøre kredit, forsikring, ydelser, uddannelse eller adgang til tjenester
- [ ] Genkender følelser eller bruger biometri (ansigt, stemme, fingeraftryk)
- [ ] Taler direkte med mennesker (chatbot, stemmeassistent)
- [ ] Laver billeder, lyd, video eller tekst, der bliver offentliggjort
- [ ] Handler på egen hånd, uden at en person tjekker hvert resultat
- [ ] Bruges af eller på vegne af en offentlig myndighed

## Klassifikation *(udfyldes af den AI-ansvarlige)*

| Felt | Svar |
|---|---|
| Risikoniveau efter AI-forordningen (eu_ai_act_tier) | prohibited / high / limited / minimal / out_of_scope. Tjek med [EU AI Act Risk Check](https://ai-act-risk-check.streamlit.app). |
| Governance-intensitet (governance_intensity) | light / standard / enhanced / strict / redesign / stop |
| Konsekvensanalyse efter GDPR (dpia_required) | yes / no |
| Konsekvensanalyse for grundlæggende rettigheder (fria_required) | yes / no |
| Godkendt af (approved_by) | Navn eller "AI-rådet" |
| Godkendt den (approved_on) | Dato |
| Næste gennemgang (next_review) | Dato |
| Noter (notes) | |

Værdierne i registeret står på engelsk, så filen kan bruges direkte i [AI Use Case Register](https://ai-use-case-register.streamlit.app).
