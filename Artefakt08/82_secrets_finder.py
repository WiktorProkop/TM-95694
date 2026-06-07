import os
import re

def find_secrets(strings_path="../Artefakt02/decompiled_apk/res/values/strings.xml"):
    print(f">>> SKANOWANIE ZASOBÓW: {strings_path} <<<")
    
    if not os.path.exists(strings_path):
        print(f"[!] BŁĄD: Nie odnaleziono pliku zasobów. Tworzę plik symulacji do testu...")
        os.makedirs(os.path.dirname(strings_path), exist_ok=True)
        with open(strings_path, "w", encoding="utf-8") as f:
            f.write('<resources>\n<string name="google_api_key">AIzaSyB123456789</string>\n')
            f.write('<string name="server_ip">192.168.1.100</string>\n')
            f.write('<string name="admin_pass">P@ssw0rd2026</string>\n')
            f.write('<string name="url_login">http://www.google.com</string>\n</resources>')

    # Definicja wzorców (RegEx) - narzędzia pracy inżyniera Security
    patterns = {
        "IP_Address": r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
        "URL_Endpoint": r'https?://[\w\.-]+',
        "Potential_Secret": r'(?i)key|token|secret|password|auth|api_key',
        "API_Key_Format": r'[a-zA-Z0-9_-]{20,}'
    }
    
    results = []
    try:
        with open(strings_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for label, pattern in patterns.items():
            matches = re.findall(pattern, content)
            for match in set(matches): # Usuwamy duplikaty
                if len(match) > 3: # Omijamy bardzo krótkie frazy
                    results.append(f"[{label}] -> {match}")

        # Zapis do pliku tekstowego (Artefakt 8.2.1)
        with open("82_secrets_found.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(results))
            
        for res in results:
            print(res)
        print(f"\n[INFO] Analiza zakończona. Znaleziono {len(results)} potencjalnych punktów wycieku.")

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    find_secrets()