# financial-education

**Bezpłatne, dwujęzyczne (polski + angielski) kursy dla inwestorów: jak gospodarka porusza rynkami, wyjaśnione na prawdziwych danych.**

> English version of this page: [README.md](README.md).

![Język: polski i angielski](https://img.shields.io/badge/j%C4%99zyk-polski%20%2B%20angielski-red)
![Kurs: 16 rozdziałów](https://img.shields.io/badge/kurs-16%20rozdzia%C5%82%C3%B3w%20%2B%20s%C5%82owniczek-blue)
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
