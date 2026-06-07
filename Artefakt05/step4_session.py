import json
import os

def solve_session():
    caps_path = '51_caps.json'
    selectors_path = '53_selectors.json'

    # Sprawdzanie czy pliki istnieją
    if not os.path.exists(caps_path) or not os.path.exists(selectors_path):
        print("BŁĄD: Brakuje plików 51_caps.json lub 53_selectors.json!")
        return

    # 1. Wczytywanie Capsów
    with open(caps_path, 'r') as f:
        caps_data = json.load(f)

    # 2. Wczytywanie Selektorów
    with open(selectors_path, 'r') as f:
        ui_map = json.load(f)

    # Pobieranie danych (z obsługą różnych formatów JSON)
    app_pkg = caps_data.get("appPackage") or caps_data.get("appium:appPackage")
    app_act = caps_data.get("appActivity") or caps_data.get("appium:appActivity")
    dev_name = caps_data.get("deviceName") or caps_data.get("appium:deviceName")
    ui_count = len(ui_map.get("selectors", {}))

    # 3. Weryfikacja integracji
    if not app_pkg or not app_act:
        status_msg = "FAILED: Missing appPackage or appActivity in JSON!"
        status_color = "FAILED"
    else:
        status_msg = "READY TO CONNECT"
        status_color = "SUCCESS"

    # Budowanie raportu do konsoli i pliku
    report = [
        ">>> ZADANIE 5.4: INTEGRACJA ARTEFAKTÓW (STABLE BUILD) <<<",
        "=== ARTEFAKT 5.4: SESSION READINESS REPORT ===",
        f"Target App    : {app_pkg}",
        f"Main Activity : {app_act}",
        f"Device        : {dev_name}",
        f"UI Elements   : {ui_count} loaded",
        f"Status        : {status_msg}"
    ]

    final_report = "\n".join(report)
    print(final_report)

    # Zapis do 54_session.log
    with open('54_session.log', 'w', encoding='utf-8') as f:
        f.write(final_report)

if __name__ == "__main__":
    solve_session()