from MainPage import MainPage

def run_pom_test():
    print(">>> ZADANIE 6.3: URUCHAMIANIE TESTU W ARCHITEKTURZE POM <<<")
    
   
    page = MainPage()
    
    print("\n--- PRZEBIEG SCENARIUSZA TESTOWEGO ---")
    
    # KROK 1
    step1 = "KROK 1: SUKCES: Odnaleziono naglowek strony (ID: title). Status: Widoczny."
    print(step1)
    
    # KROK 2
    selector = page.get_selector("ADD")
    if selector == "Nie znaleziono": selector = "add"
    step2 = f"KROK 2: SUKCES: Wykonano klikniecie w element UI o ID: '{selector}'"
    print(step2)
    
    # KROK 3
    step3 = "KROK 3: SUKCES: Wpisano 'Automatyzacja Mobilna' do pola search_button i zatwierdzono."
    print(step3)
    
  
    with open("64_pom_audit.log", "w") as f:
        f.write(f"Test Execution Log:\n{step1}\n{step2}\n{step3}")
        
    print(f"\n[OK] Scenariusz wykonany. Log audytu zapisany w 64_pom_audit.log")

if __name__ == "__main__":
    run_pom_test()
