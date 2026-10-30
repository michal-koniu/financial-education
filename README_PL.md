# financial-education

**Bezpłatne, dwujęzyczne (polski + angielski) kursy dla inwestorów: jak gospodarka porusza rynkami, wyjaśnione na prawdziwych danych.**

> English version of this page: [README.md](README.md).

![Język: polski i angielski](https://img.shields.io/badge/j%C4%99zyk-polski%20%2B%20angielski-red)
![Kurs: 16 rozdziałów](https://img.shields.io/badge/kurs-16%20rozdzia%C5%82%C3%B3w%20%2B%20s%C5%82owniczek-blue)
![Poradnik: zarabianie wokół GTA 6](https://img.shields.io/badge/poradnik-GTA%206%20zarabianie-orange)
![Dane: FRED, odtwarzalne](https://img.shields.io/badge/dane-FRED%2C%20odtwarzalne-green)
![Licencja: CC BY 4.0 + MIT](https://img.shields.io/badge/licencja-CC%20BY%204.0%20%2B%20MIT-lightgrey)

Wszystko tutaj to materiał edukacyjny. Nic z tego nie jest doradztwem finansowym.

---

## Kurs — [praktyczna makroekonomia dla inwestorów](pl/praktyczna-makroekonomia/00-INDEKS.md) (`pl/praktyczna-makroekonomia/`, wersja angielska: [`en/practical-macro-economy/`](en/practical-macro-economy/00-INDEX.md))

Po tym kursie obejrzysz film o makroekonomii i rynku kryptowalut, na przykład
[Benjamina Cowena](https://www.youtube.com/@benjaminjcowen) (Into The Cryptoverse), którego zestaw wskaźników kurs
omawia w całości, i zrozumiesz każdy wskaźnik, metrykę i wykres. Będziesz wiedzieć, co każdy z nich mierzy, skąd
wziąć dane za darmo, co wyprzedza, za czym podąża i co historycznie oznaczał dla bitcoina, altcoinów, akcji,
obligacji, dolara i złota. Kurs jest niezależny i niezwiązany z autorem kanału.

| Część | Rozdziały | Tematy |
|---|---|---|
| Narzędzia | [01](pl/praktyczna-makroekonomia/01-JAK-CZYTAC-WYKRESY-MAKRO.md) | skala logarytmiczna, średnie kroczące, pasma regresji, skale ryzyka, korelacja i wyprzedzenie, pułapki statystyczne |
| Makro | [02](pl/praktyczna-makroekonomia/02-FED-I-STOPY-PROCENTOWE.md)–[09](pl/praktyczna-makroekonomia/09-SEZONOWOSC-I-CYKLE-POLITYCZNE.md) | Fed, obligacje i krzywa rentowności, inflacja, rynek pracy, wzrost, płynność i dolar, akcje i złoto, sezonowość |
| Krypto | [10](pl/praktyczna-makroekonomia/10-CYKLE-I-MODELE-WYCENY-BITCOINA.md)–[12](pl/praktyczna-makroekonomia/12-DOMINACJA-ALTCOINY-I-ROTACJA.md) | cykle i modele wyceny bitcoina, on-chain i sentyment, dominacja i altcoiny |
| Synteza | [13](pl/praktyczna-makroekonomia/13-JAK-TO-SIE-LACZY.md)–[16](pl/praktyczna-makroekonomia/16-SLOWNICZEK.md) | **jak to się łączy**, dekoder filmów i skuteczność prognoz, twój pulpit i rutyna, słowniczek |

## Poradnik — [zarabianie wokół GTA 6: co jest realne](pl/gta6-mozliwosci-zarobku/README.md) (`pl/gta6-mozliwosci-zarobku/`)

Poradnik edukacyjny dla osoby technicznie biegłej, z lokalnym zestawem AI, która chce wiedzieć, które sposoby zarabiania wokół
wielkiej premiery gry są realne, które to szum, i gdzie agenty naprawdę pomagają. 25 opcji ocenionych pod kątem dochodu,
prawdopodobieństwa, automatyzacji, szybkości i ryzyka, z pokazanym rachunkiem; sześć miejsc, w których „agenty robią wszystko"
zawodzi; potok agentów z bramkami ludzkimi; 90-dniowy plan premiery z kryteriami porzucenia oraz lista tego, co wykluczone,
i dlaczego. Research biurkowy z oznaczeniem siły dowodów, stan na 30 października 2026; fakty i zasady platform zmieniają się
szybko, więc sprawdź je ponownie, zanim zadziałasz. To nie jest porada prawna, podatkowa ani inwestycyjna.

| Plik | Co w nim jest |
|---|---|
| [README](pl/gta6-mozliwosci-zarobku/README.md) | podsumowanie w dziesięciu punktach, tabela ocen, rekomendacje, szum do zdyskontowania, słowniczek, znane luki |
| [01-STATUS-I-ZASADY](pl/gta6-mozliwosci-zarobku/01-STATUS-I-ZASADY.md) | stan gry, analogie premierowe, zasady Rockstara/Take-Two/Cfx/Tebex, zasady platform i wyszukiwarki |
| [02-OPCJE-Z-OCENA](pl/gta6-mozliwosci-zarobku/02-OPCJE-Z-OCENA.md) | każda opcja: jak płaci, dowody, agenty a człowiek, ryzyka, dochód niski/bazowy/wysoki, reguła wyboru |
| [03-POTOKI-AGENTOW](pl/gta6-mozliwosci-zarobku/03-POTOKI-AGENTOW.md) | gdzie agenty zawodzą, zalecana kombinacja, potok z bramkami ludzkimi i zabezpieczeniami |
| [04-PLAN-90-DNI](pl/gta6-mozliwosci-zarobku/04-PLAN-90-DNI.md) | fazy, kluczowe daty, kryteria porzucenia, budżet czasu i pieniędzy |
| [05-WYKLUCZONE](pl/gta6-mozliwosci-zarobku/05-WYKLUCZONE.md) | co wykluczone i dlaczego oraz co legalne, ale niezalecane |
| [ZRODLA](pl/gta6-mozliwosci-zarobku/ZRODLA.md) | wszystkie źródła z uwagami o jakości |

## Narzędzie — [laboratorium makro](tools/macro-lab/README.md) (`tools/macro-lab/`)

Jeden skrypt w Pythonie (tylko biblioteka standardowa, bez klucza API), który pobiera bezpłatne dane z FRED i przelicza
statystyki kursu: odwrócenia krzywej rentowności a recesje, sygnały reguły Sahm, co następowało po każdej pierwszej
obniżce Fed, cykl prezydencki, średnie kroczące bitcoina, wartość godziwą z regresji logarytmicznej i korelacje.
[Migawka z 30 października 2026](tools/macro-lab/REPORT-2026-10-30.md).

```bash
python3 tools/macro-lab/macro_lab.py --out REPORT.md
```

## Notatki badawcze — [`research-notes/`](research-notes/README.md)

Notatki robocze, na których powstał kurs (po angielsku), z oznaczeniem siły dowodów i źródłami, oraz
[dziennik weryfikacji faktów](research-notes/FACT-CHECK-LOG.md) ze wszystkimi poprawkami wprowadzonymi przed publikacją.

---

## Licencja

Teksty kursów: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pl). Kod: MIT. Szczegóły: [LICENSE.md](LICENSE.md).
