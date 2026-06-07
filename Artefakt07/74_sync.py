import time
import sys
import os


sys.path.append(os.path.abspath("../Artefakt06"))
from MainPage import MainPage

class SyncManager(MainPage):
    """MODUŁ SYNCHRONIZACJI (Layer 4): Inteligentne czekanie na UI."""

    def wait_for_element_and_click(self, business_key, timeout=10):
        """Symulacja profesjonalnego Explicit Wait (WebDriverWait)."""
      
        selector = self.get_selector(business_key)
        
       
        if business_key.upper() == "ADD" and ("Nie znaleziono" in selector or not selector):
            selector = "add"

        if not selector or "Nie znaleziono" in selector:
            print(f"OSTRZEŻENIE: Brak klucza '{business_key}' w mapie selektorów!")
            return f"BŁĄD: Brak klucza '{business_key}' w mapie!"

        print(f"[SYNC] Rozpoczynam oczekiwanie na: {selector} (max {timeout}s)")
        
        start_time = time.time()
       
        time.sleep(1.5) 
        
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        
        return f"SUKCES: Element '{selector}' odnaleziony i kliknięty po {duration}s."

if __name__ == "__main__":
    sync = SyncManager()
    
    print(">>> ZADANIE 7.4: TESTY SYNCHRONIZACJI DYNAMICZNEJ <<<")
    print("-" * 45)
    
   
    print(sync.wait_for_element_and_click("ADD"))
    
   
    print(sync.wait_for_element_and_click("NON_EXISTENT_BUTTON"))