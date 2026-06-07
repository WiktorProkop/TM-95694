import json
import os

def run_library_audit():
    print(">>> ZADANIE 8.3: ANALIZA ŁAŃCUCHA DOSTAW (SCA) <<<")
    req_file = "requirements.txt"
    
    # Symulowana baza danych podatności (CVE)
    cve_database = {
        "com.google.android.gms:10.0.1": {"id": "CVE-2021-4352", "sev": "HIGH", "desc": "Błąd weryfikacji certyfikatu"},
        "com.squareup.okhttp:2.7.5": {"id": "CVE-2016-2402", "sev": "MEDIUM", "desc": "Podatność na Man-in-the-Middle"},
        "org.apache.commons:1.0.0": {"id": "CVE-2015-7501", "sev": "CRITICAL", "desc": "Zdalne wykonanie kodu (RCE)"},
        "com.android.support:25.0.0": {"id": "CVE-2019-1234", "sev": "LOW", "desc": "Wyciek informacji w logach"}
    }

    vulnerabilities_found = []

    if not os.path.exists(req_file):
        print(f"[!] Brak pliku {req_file}")
        return

    with open(req_file, "r") as f:
        libs = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    print(f"[INFO] Rozpoczynam skanowanie bibliotek z pliku: {req_file}...\n")
    
    for lib in libs:
        if lib in cve_database:
            issue = cve_database[lib]
            vulnerabilities_found.append({
                "library": lib,
                "cve_id": issue["id"],
                "severity": issue["sev"],
                "description": issue["desc"]
            })
            print(f"[{issue['sev']}] {lib}")
            print(f"    Id: {issue['id']} | Opis: {issue['desc']}")

    # Zapis do pliku JSON (Artefakt 8.3)
    with open("83_vulnerabilities.json", "w", encoding="utf-8") as jf:
        json.dump(vulnerabilities_found, jf, indent=4, ensure_ascii=False)

    print(f"\n[OK] Znaleziono {len(vulnerabilities_found)} podatności. Raport zapisany w 83_vulnerabilities.json")

if __name__ == "__main__":
    run_library_audit()