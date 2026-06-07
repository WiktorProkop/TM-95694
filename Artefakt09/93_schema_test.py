import requests

def test_api_schema():
    print(">>> ZADANIE 9.3: WALIDACJA TYPU DANYCH (SCHEMA VALIDATION) <<<")
    url = "https://jsonplaceholder.typicode.com/todos/1"
    
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        
       
        user_id = data.get('userId')
        title = data.get('title')
        completed = data.get('completed')

        print(f"[DEBUG] Dane z API: {data}")
        print("-" * 30)

        
        is_valid = True
        
        if not isinstance(user_id, int):
            print(f"[ERROR] userId powinien byc INT, a jest: {type(user_id)}")
            is_valid = False
        else:
            print(f"[OK] userId jest poprawnym typem (Integer)")

        if not isinstance(title, str):
            print(f"[ERROR] title powinien byc STRING, a jest: {type(title)}")
            is_valid = False
        else:
            print(f"[OK] title jest poprawnym typem (String)")

        if not isinstance(completed, bool):
            print(f"[ERROR] completed powinien byc BOOL, a jest: {type(completed)}")
            is_valid = False
        else:
            print(f"[OK] completed jest poprawnym typem (Boolean)")

        if is_valid:
            print("\n[SUCCESS] Pomyslna walidacja typu danych (string vs number vs bool)!")
        else:
            print("\n[FAIL] Wykryto bledne typy danych w odpowiedzi API!")

    except Exception as e:
        print(f"[FATAL] Blad podczas walidacji: {e}")

if __name__ == "__main__":
    test_api_schema()