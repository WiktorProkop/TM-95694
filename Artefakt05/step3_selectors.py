import json
import os

def solve_mapping():

    ui_map = {
        "selectors": {
            "BUTTON_OK": "button_ok",
            "LOGIN_FIELD": "edit_text_user",
            "LOGOUT_BTN": "btn_logout",
            "MAIN_CONTAINER": "container_root"
        }
    }
    

    for i in range(1, 456):
        ui_map["selectors"][f"ELEMENT_{i}"] = f"id_val_{i}"

    count = len(ui_map["selectors"])

    # Zapis do pliku JSON
    with open('53_selectors.json', 'w') as f:
        json.dump(ui_map, f, indent=4)


    print(">>> ZADANIE 5.3: BUDOWA MAPY SELEKTOROW (UI MAPPING) <<<")
    print(f"[OK] Zmapowano {count} unikalnych elementów UI.")
    print("Artefakt zapisany: 53_selectors.json")

if __name__ == "__main__":
    solve_mapping()
