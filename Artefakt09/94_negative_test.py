import requests

def test_api_negative():
    print(">>> ZADANIE 9.4: TESTY NEGATYWNE (OBSLUGA BLEDOW) <<<")
    
   
    url = "https://jsonplaceholder.typicode.com/posts/9999"
    
    try:
        print(f"[INFO] Proba pobrania nieistniejacego zasobu: {url}")
        response = requests.get(url, timeout=5)
        
        status_code = response.status_code
        
        print(f"[DEBUG] Otrzymany Status Code: {status_code}")
        
       
        if status_code == 404:
            print("[SUCCESS] Test negatywny zaliczony: API poprawnie zwrocilo kod 404 Not Found")
        else:
            print(f"[FAIL] API powinno zwrocic 404, a zwrocilo: {status_code}")
            
    except Exception as e:
        print(f"[FATAL] Blad polaczenia: {e}")

if __name__ == "__main__":
    test_api_negative()