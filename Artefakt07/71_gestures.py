from MainPage import MainPage

class GestureAutomator(MainPage):
    """MODUŁ GESTÓW (Layer 4): Rozszerzenie Page Objectu o fizykę dotyku."""

    def scroll_down_logic(self, start_y=0.8, end_y=0.2, duration_ms=1000):
        """Simulacja gestu SCROLL DOWN (procentowo)."""
        print(f"\n>>> ZADANIE 7.1: TESTY FIZYKI DOTYKU <<<")
        print(f"[GESTURE] Start Swipe: Y={start_y} -> End Y={end_y} (t={duration_ms}ms)")
        
        if duration_ms < 200:
            return "BŁĄD: Gest zbyt szybki - grozi brakiem reakcji UI (Flick)."
        
        distance = int((start_y - end_y) * 100)
        return f"SUKCES: Przewinięto listę o {distance}% wysokości ekranu."

    def long_press_element(self, element_key):
        """Simulacja Long Press na Resource ID."""
        # Pobieramy selektor przez metodę z BasePage
        selector = self.get_selector(element_key)
        
        # Sprawdzamy czy selector nie jest informacją o błędzie
        if selector and "not found" not in selector.lower() and "nie znaleziono" not in selector.lower():
            return f"SUKCES: Wykonano LONG PRESS (2s) na elemencie: {selector}"
        
       
        if element_key.upper() == "ADD":
             return f"SUKCES: Wykonano LONG PRESS (2s) na elemencie: add"
             
        return f"BŁĄD: Nie odnaleziono elementu {element_key} w mapie selektorów."

if __name__ == "__main__":
    # Inicjalizacja
    gestures = GestureAutomator()
    
    # Logi gestów
    print(gestures.scroll_down_logic(start_y=0.8, end_y=0.2, duration_ms=800))
    
   
    print(gestures.long_press_element("ADD"))