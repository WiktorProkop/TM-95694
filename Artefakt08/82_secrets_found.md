# RAPORT ANALIZY WYCIEKÓW (SECRETS)

**Student:** [Miłosz Bartoszuk]
**Indeks:** [96421]
**Data raportu:** 29-03-2026

## 1. Trzy najbardziej groźne znaleziska (High Risk)
Poniższe elementy wymagają natychmiastowej zmiany w kodzie źródłowym:
1. **[Potential_Secret] -> admin_pass**: Sugeruje obecność zahardkodowanego hasła administratora w pliku strings.xml.
2. **[IP_Address] -> 192.168.1.100**: Adres IP wewnętrznej infrastruktury nie powinien być widoczny w publicznej aplikacji.
3. **[API_Key_Format] -> AIzaSyB123456789**: Wykryto klucz API, który może zostać użyty do nieautoryzowanego dostępu do usług Google.

## 2. Trzy znaleziska typu "False Positive" (Low/No Risk)
Elementy błędnie sklasyfikowane jako zagrożenie:
1. **[URL_Endpoint] -> http://www.google.com**: To standardowy link zewnętrzny, powszechnie używany do testowania łączności.
2. **[Potential_Secret] -> google_api_key**: Nazwa klucza sugeruje zagrożenie, ale sam klucz może być publicznym identyfikatorem (nie kluczem prywatnym).
3. **[API_Key_Format] -> secure_view_step4**: To prawdopodobnie nazwa identyfikatora widoku w XML, a nie klucz kryptograficzny.

## Wnioski końcowe
Automatyczne skanowanie RegEx jest skuteczne, ale wymaga manualnej weryfikacji inżyniera, ponieważ skrypt nie rozumie kontekstu biznesowego aplikacji.