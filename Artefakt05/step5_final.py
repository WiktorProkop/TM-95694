import json
import os

def solve_final():

    caps_path = '51_caps.json'
    selectors_path = '53_selectors.json'

    # Wczytanie danych
    with open(caps_path, 'r') as f:
        caps_data = json.load(f)
    with open(selectors_path, 'r') as f:
        ui_map = json.load(f)

    current_pkg = caps_data.get("appPackage") or caps_data.get("appium:appPackage")
    feedback_report = []

    # 1. Weryfikacja Pakietu
    if current_pkg == "io.appium.android.apis":
        feedback_report.append({
            "feature": "Identyfikacja Aplikacji",
            "status": "ZGODNY",
            "message": f"Pakiet {current_pkg} poprawnie zmapowany."
        })
    else:
        feedback_report.append({
            "feature": "Identyfikacja Aplikacji",
            "status": "DO POPRAWY",
            "message": f"Niezgodnosc pakietu. Wykryto {current_pkg}."
        })

    # 2. Weryfikacja Dostepnosci Elementow
    target_element = "ACCESSIBILITY"
    if target_element in ui_map["selectors"]:
        feedback_report.append({
            "feature": "Dostepnosc UI",
            "status": "ZGODNY",
            "message": f"Element {target_element} jest dostepny w layoutach."
        })
    else:

        suggestions = list(ui_map['selectors'].keys())[:3]
        feedback_report.append({
            "feature": "Dostepnosc UI",
            "status": "INFORMACJA",
            "message": f"Nie odnaleziono ID '{target_element}'. Sugestia: Zweryfikuj czy element nie zmienil nazwy na jedna z dostepnych: {suggestions}."
        })


    print(">>> ZADANIE 5.5: GENEROWANIE RAPORTU FEEDBACKU DLA DEWELOPERA <<<")
    print("\n--- FEEDBACK DLA TWORCOW APLIKACJI ---")
    for item in feedback_report:
        print(f"[{item['status']}] {item['feature']}: {item['message']}")
    
    print("\n[INFO] Blok 5 zakonczony. Raport opisowy gotowy: 55_result.xml")

    # Generowanie pliku XML (prosty format JUnit)
    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<testsuite name="Blok5_Final_Report" tests="2">
    <testcase name="PackageVerification" status="{feedback_report[0]['status']}">
        <system-out>{feedback_report[0]['message']}</system-out>
    </testcase>
    <testcase name="UI_Accessibility" status="{feedback_report[1]['status']}">
        <system-out>{feedback_report[1]['message']}</system-out>
    </testcase>
</testsuite>"""

    with open('55_result.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)

if __name__ == "__main__":
    solve_final()
