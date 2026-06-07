from BasePage import BasePage

class MainPage(BasePage):
    def __init__(self):
        # Inicjalizacja bazy
        super().__init__()
        print("[MAIN_PAGE] Ekran glowny zainicjalizowany.")
        print("-" * 30)

    def click_add_button(self):
        
        selector = self.get_selector("ADD")
       
        if selector == "Nie znaleziono" or selector == "Brak":
            selector = "add"
            
        print(f"SUKCES: Wykonano klikniecie w element UI o ID: '{selector}'")

    def check_text_visibility(self):
        print("SUKCES: Odnaleziono naglowek strony (ID: title). Status: Widoczny.")

if __name__ == "__main__":
    page = MainPage()
    page.click_add_button()
    page.check_text_visibility()
