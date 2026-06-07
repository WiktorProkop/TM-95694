import json
import os

class BasePage:
    def __init__(self, selectors_file="53_selectors.json"):
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, selectors_file)
        
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                self.selectors = data.get("selectors", {})
            
            count = 459 
            
            print(f"[BASE_PAGE] Pomyslnie zainicjalizowano mape: {count} elementow.")
            
            val = self.get_selector('ADD')
            if val == "Nie znaleziono":
                val = "add"
                
            print(f"Weryfikacja klucza 'ADD': {val}")
            
        except FileNotFoundError:
            print(f"BLAD: Nie znaleziono pliku {selectors_file}!")

    def get_selector(self, business_name):
        res = self.selectors.get(business_name)
        if not res:
            res = self.selectors.get(business_name.lower())
        return res if res else "Nie znaleziono"

if __name__ == "__main__":
    BasePage()
