# Portfolio Inżyniera
**Autor:** [Miłosz Bartoszuk]  
**Projekt:** Laboratorium Testowanie Mobilne (Bloki 1-10)

## 📱 O Projekcie
Repozytorium zawiera kompletną ścieżkę nauki automatyzacji testów dla platform mobilnych 
(Android/iOS) z wykorzystaniem nowoczesnych narzędzi inżynierskich.

## 🛠 Technologie i Narzędzia
* **Język:** Python 3.10+
* **Framework testowy:** Pytest
* **Automatyzacja mobilna:** Appium Server & Appium Inspector
* **Konteneryzacja:** Docker & Docker Compose
* **Raportowanie:** Allure Framework
* **Inne:** ADB (Android Debug Bridge), Wyse VDI, GitHub

## 📝 Przebieg Laboratorium (Bloki 1-10)

### Bloki 1-3: Fundamenty i Środowisko
Skonfigurowałem środowisko deweloperskie, przygotowałem narzędzia ADB oraz nauczyłem się zarządzać 
emulatorami Androida. Poznałem architekturę Appium.

### Bloki 4-6: Podstawy Pythona i Pytest
Stworzyłem pierwsze skrypty automatyczne. Opanowałem asercje, struktury danych w Pythonie oraz 
mechanizm **fixtures** w Pytest, który pozwolił na optymalizację setupu testów.

### Bloki 7-8: Zaawansowana Automatyzacja i Appium
Zrealizowałem testy funkcjonalne rzeczywistych aplikacji mobilnych. Nauczyłem się lokalizować 
elementy (XPath, ID) oraz obsługiwać gesty (swipe, tap, scroll).

### Blok 9: Konteneryzacja (Docker)
Przeniosłem infrastrukturę testową do kontenerów. Wykorzystałem **Docker Compose**, aby jednym poleceniem 
uruchamiać serwer Appium wraz z zależnościami, co zapewnia powtarzalność testów.

### Blok 10: Profesjonalne Raportowanie i Pipeline
Zaimplementowałem framework **Allure**, tworząc czytelne raporty z meta-danymi (Epic, Feature, Story). Stworzyłem autorski 
**Pipeline w Pythonie**, który automatyzuje cały cykl: od postawienia kontenerów, przez testy, aż po generowanie statycznego raportu HTML.
