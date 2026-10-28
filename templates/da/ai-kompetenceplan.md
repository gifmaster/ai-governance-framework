# Plan for AI-færdigheder: [Organisationens navn]

| | |
|---|---|
| Version | 1.0 |
| Ejer | [AI-ansvarlig] |
| Godkendt af | [Direktionen] |
| Næste gennemgang | [Dato, senest 12 måneder senere] |

> **Sådan bruger du skabelonen.** Udskift alt i [klammer], og slet disse noter. Planen beskriver, hvem der lærer hvad, og [oplæringsloggen](../training-log.csv) dokumenterer, at det er sket. Behold begge: Når en kunde, en revisor eller en myndighed spørger, hvad I gør for AI-færdigheder, er de jeres svar.

## 1. Hvad loven kræver

Udbydere og idriftsættere af AI-systemer skal **træffe foranstaltninger, der understøtter** et tilstrækkeligt niveau af AI-færdigheder hos deres personale og andre, der betjener AI-systemer på deres vegne. Det skal ske under hensyn til deres viden, erfaring, uddannelse og oplæring og den sammenhæng, systemerne bruges i. *(AI-forordningen art. 4, som ændret ved Digital Omnibus om AI, forordning (EU) 2026/1744)*

Det betyder i praksis:

- Kravet gælder for alle organisationer, der bruger AI i arbejdet, uanset risikoniveau. Et værktøj, der opsummerer møder, er nok.
- Der kræves foranstaltninger, ikke et garanteret vidensniveau hos hver enkelt. Den ændrede tekst siger det direkte.
- Foranstaltningerne skal passe til rollen og værktøjerne. Ét generelt e-læringskursus til alle er et svagt bevis.
- Dokumentér det. Loven foreskriver ikke en bestemt form, men uden dokumentation kan I ikke vise, hvad I har gjort.

Andre krav, hvor de gælder:

- **Højrisiko-AI:** Idriftsættere skal overlade det menneskelige tilsyn til personer med de nødvendige kompetencer, den nødvendige oplæring og den nødvendige myndighed *(art. 26, stk. 2, for systemer i bilag III fra 2. december 2027)*.
- **NIS2-virksomheder:** Ledelsen skal gennemgå uddannelse i cybersikkerhed *(NIS2 art. 20, stk. 2)*. **Finansielle enheder under DORA:** Ledelsesorganet skal holde sig opdateret om IKT-risici *(DORA art. 5, stk. 4)*. Kombinér det med AI-færdigheder, hvor det giver mening.

## 2. Hvem lærer hvad

| Gruppe | Hvem | Emner | Form og varighed | Hvornår |
|---|---|---|---|---|
| **Alle medarbejdere** | Alle, der kan komme til at bruge AI i arbejdet | Hvad AI kan og ikke kan. Vores [AI-politik](ai-politik.md) og [regler for brug af AI](brug-af-ai.md). Regler for data. At tjekke resultater. At melde problemer. | [Oplæg eller e-læring, 45 til 60 min.] | Inden for [4 uger] efter start, opfriskning hver [12. måned] |
| **Hyppige brugere** | Medarbejdere, der bruger AI dagligt eller i kundevendt arbejde | De værktøjer, de bruger: styrker, typiske fejl, indstillinger, hvilke data der må bruges. Mærkning af AI-indhold. | [Praktisk workshop, 1 til 2 timer, pr. værktøj] | Før adgang til værktøjet, opfriskning når værktøjet ændres |
| **Personer med tilsyn** | Medarbejdere, der gennemgår, godkender eller kan stoppe et AI-systems output som en del af jobbet | Hvordan systemet virker og fejler. Hvad der skal tjekkes, hvor ofte, hvornår man griber ind, hvordan man stopper det, hvordan beslutninger registreres. Overdreven tillid til automatik. | [Gennemgang pr. system, 1 til 2 timer, med ejeren af anvendelsen] | Før idriftsættelse, opfriskning hver [12. måned] eller når systemet ændres |
| **Ledelse** | Direktion og bestyrelse | Hvor vi bruger AI, vores risikovillighed, de relevante regler, ledelsens ansvar. | [Oplæg, 60 til 90 min.] | En gang om året |
| **AI-ansvarlig og AI-råd** | Dem, der klassificerer og beslutter | AI-forordningen og tilgrænsende regler, klassifikation, rammeværket, værktøjerne. | [Kursus eller ekstern uddannelse] | En gang om året og efter større lovændringer |

## 3. Hvilke systemer kræver oplæring af personer med tilsyn

Alle anvendelser med governance-intensiteten **enhanced** eller **strict** skal have mindst én navngiven person med tilsyn, der er oplært før idriftsættelse. Skriv anvendelsens ID i oplæringsloggen, så sammenhængen kan tjekkes.

## 4. Dokumentation

| Dokumentation | Hvor |
|---|---|
| Hvem der er oplært, i hvad, hvornår og af hvem | [Oplæringsloggen](../training-log.csv) |
| Materialet, med version og dato | [Mappe eller link] |
| Deltagerlister eller rapporter fra e-læring | [Mappe eller link], henvist til i loggens kolonne *evidence* |
| Denne plan, godkendt og dateret | [Mappe eller link] |

Registrér grupper frem for enkeltpersoner, hvor det er nok ("Kundeservice, 14 personer"). Oplysninger om enkeltpersoner er personoplysninger: Gem dem kun, så længe I har brug for dem, og følg jeres sædvanlige regler for opbevaring af HR-data.

Loggens kolonner står på engelsk, så den kan bruges direkte i [AI Use Case Register](https://ai-use-case-register.streamlit.app): *learner_group* er gruppen (all_staff, frequent_user, overseer, management eller governance), *audience* er hvem, *people* er antal personer, *module* er emnet, *use_case_id* er de anvendelser, oplæringen dækker (adskilt med semikolon), *delivered_on* er datoen, *delivered_by* er underviseren, *format* er formen, *evidence* er dokumentationen, og *next_refresh* er datoen for næste opfriskning.

## 5. Hvordan vi ved, at det virker

- Gennemgå oplæringsloggen hvert kvartal: grupper uden oplæring, overskredne opfriskninger, systemer uden oplærte personer med tilsyn. [AI Use Case Register](https://ai-use-case-register.streamlit.app) laver disse tjek på loggen og registeret samlet.
- Spørg medarbejderne en gang om året, hvor sikre de føler sig i brugen af AI, og hvor de har brug for hjælp.
- Se på hændelser: Skyldtes en hændelse, at nogen ikke kendte et værktøjs begrænsninger, så justér oplæringen.

## 6. Gennemgang

Planen gennemgås mindst en gang om året, og når vi tager en ny type AI i brug, et værktøj ændres væsentligt, eller lovgivningen ændres.
