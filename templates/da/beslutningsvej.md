# Sådan behandles anmodninger om AI

> **Sådan bruger du skabelonen.** Dette er beslutningsvejen bag [anmodningen om en ny AI-anvendelse](ai-anmodning.md): hvem svarer, hvor hurtigt, og hvilke svar der findes. Det svarer til beslutningspunkt G1 og for de fleste anvendelser også G2 i [livscyklussen](../../framework/04-use-case-lifecycle.md). Udskift tallene i [klammer] med det, I faktisk kan overholde.

## 1. Første gennemsyn, inden for [2] arbejdsdage

Den AI-ansvarlige læser anmodningen og svarer på tre spørgsmål.

| Spørgsmål | Hvis ja |
|---|---|
| Er det et godkendt værktøj brugt til et godkendt formål? | Der skal ikke træffes en ny beslutning. Giv besked og luk sagen. |
| Er der sat kryds under *Hurtig screening*? | Klassificér grundigt med [EU AI Act Risk Check](https://ai-act-risk-check.streamlit.app), før der træffes en beslutning. Aldrig hurtigt spor. |
| Mangler der oplysninger, der kan ændre svaret? | Sæt sagen **i bero**, og bed om oplysningerne. Fristen står stille, til svaret kommer. |

## 2. Klassificér og fastsæt intensiteten

Fastsæt risikoniveauet efter AI-forordningen og tilsynsniveauet. Tilsammen giver de [governance-intensiteten](../../framework/03-oversight-scale.md#governance-intensity), og intensiteten afgør, hvem der beslutter.

| Intensitet | Hvem beslutter | Svar inden for |
|---|---|---|
| light | AI-ansvarlig | [2] arbejdsdage |
| standard | AI-ansvarlig, orienterer AI-rådet | [5] arbejdsdage |
| enhanced | AI-rådet | [10] arbejdsdage eller næste møde |
| strict | AI-rådet, efter vurderingerne i [AI-systemets dokumentation](../ai-system-record.md) | Når vurderingerne er færdige |
| redesign | Tilbage til den, der har spurgt: AI'ens selvstændighed skal ned, før sagen kan behandles | [5] arbejdsdage |
| stop | Afvist. Forbudt efter AI-forordningen. | [2] arbejdsdage |

## 3. De fem mulige svar

| Svar | Betydning | Registrér i AI-registeret |
|---|---|---|
| **Godkendt** | Gå i gang som beskrevet. | status *assessment* eller *live*, approved_by, approved_on, next_review |
| **Godkendt med betingelser** | Gå i gang, men kun på de betingelser, der står skrevet. | Som ovenfor, betingelserne i *notes* |
| **I bero** | Vi mangler oplysninger, eller en vurdering (konsekvensanalyse, kontrakttjek) skal laves først. | status *intake* eller *assessment*, hvad der mangler i *notes* |
| **Sendt til AI-rådet** | Intensiteten er enhanced eller strict, eller sagen er uklar. | status *assessment* |
| **Afvist** | Ikke tilladt, eller risikoen står ikke mål med gevinsten. Giv begrundelsen. | status *retired*, begrundelsen i *notes* |

## 4. Typiske betingelser

Vælg dem, der passer. Skriv dem i beslutningen, så det er tydeligt, hvad der skal gøres.

- Kun [disse typer data] må bruges. Ingen følsomme personoplysninger.
- En person gennemgår hvert resultat, før det forlader organisationen.
- Brugerne gennemfører [modul] i [planen for AI-færdigheder](ai-kompetenceplan.md), før de får adgang.
- Databehandleraftalen er underskrevet, og kontrakten er tjekket med [AI Contract Clause Checker](https://contract-clause-checker.streamlit.app) før idriftsættelse.
- De berørte får at vide, at AI indgår.
- Brugen begrænses til [team eller antal brugere] indtil gennemgangen den [dato].
- Værktøjet må læse [systemer], men må ikke sende, slette eller betale uden en persons godkendelse.

## 5. Giv besked

Svar skriftligt med beslutningen, begrundelsen og eventuelle betingelser. En kort besked er nok:

> Din anmodning om **[anvendelse]** er **[godkendt med betingelser]**. Betingelser: [liste]. Ejer: [navn]. Næste gennemgang: [dato]. Spørgsmål: [AI-ansvarlig].

## 6. Hold fristerne

Tæl hvert kvartal, hvor mange anmodninger der fik svar til tiden, og rapportér det til AI-rådet. Hvis folk venter for længe, holder de op med at spørge og begynder at bruge værktøjer i det stille. Et hurtigt "ja, med betingelser" er bedre governance end et langsomt "måske".
