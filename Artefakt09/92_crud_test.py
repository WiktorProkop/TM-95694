import requests
import json

def test_create_resource():
    print(">>> ZADANIE 9.2: TEST TWORZENIA ZASOBU (POST) <<<")
    
    url = "https://jsonplaceholder.typicode.com/posts"
    
   
    new_post = {
        "title": "Test Mobilny Blok 9",
        "body": "Automatyzacja API jest szybsza niz UI",
        "userId": 1
    }
    
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    print(f"[INFO] Wysylanie zadania POST do: {url}")

    try:
        
        response = requests.post(url, data=json.dumps(new_post), headers=headers, timeout=5)
        
        
        status = response.status_code
        result_data = response.json()
        
        print(f"[DEBUG] Status Code: {status}") # Oczekiwane 201
        print(f"[DEBUG] Server Response: {result_data}")
        
        if status == 201:
            print(f"[SUCCESS] Zasob stworzony pomyslnie! ID nowego obiektu: {result_data['id']}")
        else:
            print(f"[FAIL] Serwer nie stworzyl zasobu. Status: {status}")
            
    except Exception as e:
        print(f"[FATAL] Blad polaczenia: {e}")

if __name__ == "__main__":
    test_create_resource()