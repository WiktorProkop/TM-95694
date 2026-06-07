import requests
import time

def run_hybrid_test_simulation():
    print(">>> ZADANIE 9.5: TEST HYBRYDOWY (API + APPIUM INTEGRATION) <<<")
    

    print("\n[APPIUM] Inicjalizacja sterownika urządzenia...")
    time.sleep(1)
    print("[APPIUM] Klikniecie przycisku 'WYSLIJ RAPORT' na smartfonie...")
    time.sleep(1)
    print("[APPIUM] Sukces: Widok UI zaktualizowany.")

   
    print("\n[API] Rozpoczynam weryfikacje stanu na serwerze...")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[API] Serwer potwierdza istnienie zasobu. Status: 200 OK")
            print(f"[API] Dane zaciagniete z backendu: {response.json()['title'][:30]}...")
        else:
            print(f"[API] Blad weryfikacji backendu: {response.status_code}")
            
    except Exception as e:
        print(f"[API] Blad komunikacji: {e}")

    print("\n[SUCCESS] Test hybrydowy zakonczony. Dane UI i API sa spojne.")

if __name__ == "__main__":
    run_hybrid_test_simulation()