# info212-assignment-4
# Car Rental Web-API med Flask og Neo4j

## Formål
Formålet med denne øvelsen er å praktisere utvikling av Web-APIer ved hjelp av Flask-rammeverket, samt å bruke Git/GitHub for versjonskontroll og samarbeid i programvareutvikling.

## Oppgaver
- En av teammedlemmene oppretter et eksternt repositorium som inneholder et Flask Web-API prosjekt. Denne personen vil fungere som "admin" for repositoriet.
- Et annet teammedlem har ansvar for å administrere en grafdatabase i Neo4j.
- Alle teammedlemmer skal implementere deler av Flask Web-API prosjektet, med fokus på samarbeid og bruk av GitHub.
- Web-APIet vil samhandle med grafdatbasen for lagring av informasjon.
- Endringer blir pushet til GitHub-repositoriet.

## Flask WebAPI-utvikling
Dette prosjektet omfatter implementasjon av et Web-API for et bilutleiefirma. Kunden kan leie bilene uten en bestemt returtid. Funksjonene som må implementeres er:

- CRUD-operasjoner for 'Cars' med informasjon som merke, modell, år, sted, status (tilgjengelig, booket, leid, skadet).
- CRUD-operasjoner for 'Customer' med informasjon som navn, alder, adresse.
- CRUD-operasjoner for 'Employee' med informasjon som navn, adresse, filial.
- Endpoint 'order-car' hvor kunde-ID og bil-ID sendes som parametere for å booke en bil.
- Endpoint 'cancel-order-car' hvor kunde-ID og bil-ID sendes som parametere for å avbestille en booking.
- Endpoint 'rent-car' hvor kunde-ID og bil-ID sendes som parametere for å registrere en utleie.
- Endpoint 'return-car' hvor kunde-ID og bil-ID, samt bilens status ved retur (ok eller skadet) sendes som parametere.

## Installasjon og Kjøring
For å sette opp og kjøre dette prosjektet lokalt, følg disse trinnene:

1. Klon repositoriet til din lokale maskin.
2. Installer de nødvendige avhengighetene ved å kjøre `pip install -r requirements.txt`.
3. Påse at Neo4j-databasen kjører og er konfigurert korrekt.
4. Start Flask-applikasjonen ved å kjøre `flask run` i prosjektets rotmappe.

## Testing
Bruk Postman eller lignende API-testverktøy for å sjekke funksjonaliteten til implementasjonen. Se dokumentasjonen for detaljerte eksempler på API-kall.

## Bidrag
Alle teammedlemmer oppfordres til å bidra ved å klone admin-repoet, lage en lokal kopi av prosjektet, og pushe endringer til GitHub. For detaljer om hvordan du bidrar, se vår `CONTRIBUTING.md` fil (skal legges til).

## Kontakt
For spørsmål eller problemer, vennligst opprett et issue i dette repositoriet eller kontakt prosjektadministratoren direkte.

## Lisens
Dette prosjektet er lisensiert under MIT-lisensen - se `LICENSE` filen for detaljer.
