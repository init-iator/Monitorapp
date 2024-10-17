Övervakningsapplikation README
Beskrivning

Den här Python-applikationen hjälper dig att övervaka systemresurser såsom CPU-, minne- och diskanvändning. Du kan ställa in larmnivåer för dessa resurser och få aviseringar via e-post om användningen överstiger den angivna nivån. Appen erbjuder även en realtidsövervakningsläge som kontinuerligt visar resursanvändningen.

Installation

Krav: Se till att du har Python 3 och följande bibliotek installerade:
sendgrid
psutil
datetime
json
os
time
Kloning av projektet:
Bash
git clone https://github.com/init-iator/Monitorapp.git

Skapa .env-fil: Kopiera filen .env.example till .env och fyll i dina SendGrid API-nyckel, mottagarens e-postadress och avsändarens e-postadress.
Körning

Starta applikationen:
Bash
python övervakningsapplikation.py

Användning

Applikationen presenterar en huvudmeny med olika alternativ:

Starta övervakning: Startar en övervakningssession där du kan hämta ögonblicksbilder av systemresurser.
Lista aktiv övervakning: Kontrollerar om en övervakningssession är aktiv.
Skapa larm: Ställ in larmnivåer för CPU-, minne- och diskanvändning.
Visa larm: Visa lagrade larmnivåer.
Starta övervakningsläge: Öppnar ett realtidsläge som kontinuerligt visar systemresursernas användning.
Ta bort larm: Ta bort tidigare konfigurerade larm.
Realtidsövervakning (Prestanda): Startar realtidsövervakning av resurser.
Kontrollera .env filen för email utskick: Kontrollerar innehållet i .env-filen.
Avsluta programmet: Stänger applikationen.
Exempel

För att starta en övervakningssession och hämta en ögonblicksbild av systemresurserna, välj alternativ 1 i huvudmenyn. För att konfigurera ett larm för CPU-användning, välj alternativ 3 och ange en procentnivå. Applikationen skickar sedan en e-postavisering om CPU-användningen överstiger den angivna nivån.

Bidrag

Vi välkomnar bidrag till den här applikationen! Du kan föreslå förbättringar, rapportera buggar eller skicka in pull requests på GitHub.

Licens

Den här applikationen är licensierad under MIT-licensen. Se LICENSE-filen för mer information.