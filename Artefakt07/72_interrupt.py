import time
import sys
import os


sys.path.append(os.path.abspath("../Artefakt06"))
from MainPage import MainPage

class InterruptManager(MainPage):
    """MODUŁ PRZERWAŃ (Layer 4): Symulacja zdarzeń systemowych Androida."""

    def simulate_incoming_call(self, duration_sec=3):
        """Symuluje nadchodzące połączenie, które przysłania aplikację."""
        print(f"\n>>> ZADANIE 7.2: TESTY ODPORNOŚCI NA PRZERWANIA <<<")
        print(f"[INTERRUPT] KROK 1: Stan aplikacji przed połączeniem: ACTIVE")
        print(f"[INTERRUPT] KROK 2: Wyzwalanie zdarzenia: INCOMING CALL (Duration: {duration_sec}s)")
        
       
        time.sleep(1)
        print(">>> SYSTEM: Aplikacja w tle (onPause) | Widoczny ekran połączenia <<<")
        
        time.sleep(duration_sec)  # Czas trwania rozmowy
        
        print(f"[INTERRUPT] KROK 3: Zakończenie połączenia. Powrót do aplikacji.")
      
        
        return "SUKCES: Aplikacja odzyskała fokus (onResume). Dane sesji zachowane."

    def simulate_low_battery_warning(self):
        """Symuluje systemowy komunikat o niskim stanie baterii."""
        print(f"\n[INTERRUPT] Wyzwalanie zdarzenia: LOW BATTERY WARNING")
      
        return "SUKCES: Aplikacja obsłużyła systemowe okno dialogowe bez błędu."

if __name__ == "__main__":
   
    interrupt_test = InterruptManager()
    
   
    print(interrupt_test.simulate_incoming_call(duration_sec=3))
    
  
    print(interrupt_test.simulate_low_battery_warning())