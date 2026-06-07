# 📊 RAPORT Z AUDYTU BEZPIECZEŃSTWA: APIDEMOS
**Data:** 29-03-2026
**Audytor:** [Twoje Imię i Numer Studenta]
**Projekt:** Mobilny Audyt Stabilności i Security

## 📉 1. OCENA KOŃCOWA (SECURITY SCORE)
**WYNIK:** 0/100 (na podstawie 84_risk_score.txt)
**STATUS:** 🔴 REJECTED / NEEDS FIX

## 🛡️ 2. KLUCZOWE OBSZARY RYZYKA

### A. Konfiguracja Systemowa (Zadanie 8.1)
* **Problem:** Aktywna flaga `android:debuggable="true"`.
* **Wpływ:** Umożliwia napastnikowi pełny podgląd pamięci aplikacji i śledzenie zmiennych w czasie rzeczywistym.

### B. Wycieki Danych (Zadanie 8.2)
* **Problem:** Zahardkodowane klucze API i hasła w pliku strings.xml.
* **Wpływ:** Ryzyko nieautoryzowanego dostępu do infrastruktury serwerowej i usług zewnętrznych (np. Google Cloud).

### C. Biblioteki Zewnętrzne (Zadanie 8.3)
* **Problem:** Wykryto 4 krytyczne podatności, w tym RCE (Remote Code Execution) w org.apache.commons.
* **Wpływ:** Możliwość zdalnego przejęcia kontroli nad urządzeniem użytkownika.

## 📝 3. MAPA DROGOWA NAPRAWCZA (REMEDIATION)
1. **[PRIORYTET 1]:** Natychmiastowa aktualizacja biblioteki `org.apache.commons` do wersji wolnej od luki CVE-2015-7501.
2. **[PRIORYTET 1]:** Wyłączenie trybu debugowania w wersji produkcyjnej manifestu.
3. **[PRIORYTET 2]:** Migracja wrażliwych danych z plików XML do bezpiecznego magazynu (Android Keystore).

---

## 🎓 WNIOSKI KOŃCOWE
Aplikacja ApiDemos w obecnej wersji stanowi wysokie ryzyko dla użytkowników i organizacji. Nie zaleca się publikacji w sklepie Google Play bez wdrożenia powyższych poprawek.