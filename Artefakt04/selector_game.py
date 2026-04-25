import json

INPUT_FILE = "miner_report.json"

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        selectors = json.load(f)

    ids = [
        item["id"]
        for item in selectors
        if item.get("id")
    ]

    if not ids:
        print("STATUS: NIEZALICZONE! Brak ID do analizy.")
        return

    chosen_selector = ids[0]
    occurrences = ids.count(chosen_selector)

    print(f"Testowany selektor: //*[@resource-id='{chosen_selector}']")
    print(f"Liczba znalezionych elementów: {occurrences}")

    if occurrences == 1:
        print("STATUS: ZALICZONE! Twój selektor jest unikalny.")
    else:
        print("STATUS: NIEZALICZONE! Selektor nie jest unikalny.")

if __name__ == "__main__":
    main()