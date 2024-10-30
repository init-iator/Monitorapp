<h1>Övervakningsapplikation README</h1>

<h2>Beskrivning</h2>
<p>
  Denna Python-applikation hjälper dig att övervaka systemresurser såsom CPU, minne och diskutrymme. Du kan ställa in larmnivåer för dessa resurser och få e-postmeddelanden om användningen överskrider den angivna nivån. Applikationen erbjuder också ett realtidsövervakningsläge som kontinuerligt visar resursanvändning.
</p>

<h2>Installation</h2>

<h3>Krav</h3>
<p>
  Se till att du har Python 3 och följande bibliotek installerade:
</p>
<ul>
  <li>sendgrid</li>
  <li>psutil</li>
  <li>datetime</li>
  <li>json</li>
  <li>os</li>
  <li>time</li>
</ul>

<h3>Klona projektet</h3>
<pre><code>git clone https://github.com/init-iator/Monitorapp.git</code></pre>

<h3>Skapa .env-fil</h3>
<p>
  Kopiera filen <code>.env.example</code> till <code>.env</code> och fyll i din SendGrid API-nyckel, mottagarens e-postadress och avsändarens e-postadress.
  Det går också att skapa eller ändra <code>.env</code> filen via programmet. Menu val 8
</p>

<h2>Körning</h2>
<h3>Starta applikationen:</h3>
<pre><code>python main.py</code></pre>

<h2>Användning</h2>
<p>
  Applikationen visar en huvudmeny med olika alternativ:
</p>
<ul>
  <li><strong>Starta övervakning</strong>: Startar en övervakningssession där du kan hämta ögonblicksbilder av systemresurser.</li>
  <li><strong>Lista aktiv övervakning</strong>: Kontrollerar om en övervakningssession är aktiv.</li>
  <li><strong>Skapa larm</strong>: Ställ in larmnivåer för CPU, minne och diskutrymme.</li>
  <li><strong>Visa larm</strong>: Visa sparade larmnivåer.</li>
  <li><strong>Starta övervakningsläge</strong>: Öppnar ett realtidsläge som kontinuerligt övervakar systemresurser och triggar larm samt e-postmeddelanden om användningen överskrider den angivna nivån.</li>
  <li><strong>Ta bort larm</strong>: Ta bort tidigare konfigurerade larm.</li>
  <li><strong>Realtidsövervakning (Prestanda)</strong>: Startar realtidsövervakning av resurser.</li>
  <li><strong>Kontrollera .env-fil för e-post</strong>: Kontrollerar innehållet i .env-filen.</li>
  <li><strong>Avsluta programmet</strong>: Stänger applikationen.</li>
</ul>

<h2>Exempel</h2>
<p>
  För att starta en övervakningssession och hämta en ögonblicksbild av systemresurser, välj alternativ 1 i huvudmenyn. För att konfigurera ett larm för CPU-användning, välj alternativ 3 och ange en procentsats. Applikationen skickar sedan ett e-postmeddelande om CPU-användningen överskrider den angivna nivån.
</p>

<h2>Bidrag</h2>
<p>
  Vi välkomnar bidrag till denna applikation! Du kan föreslå förbättringar, rapportera buggar eller skicka in pull requests på GitHub.
</p>

<h2>Licens</h2>
<p>
  Denna applikation är licensierad under MIT-licensen. Se LICENSE-filen för mer information.
</p>
