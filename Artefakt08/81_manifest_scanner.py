import xml.etree.ElementTree as ET
import os

def scan_manifest():
    # Ścieżka docelowa
    dir_path = "../Artefakt02/decompiled_apk"
    manifest_path = os.path.join(dir_path, "AndroidManifest.xml")
    
    print(f">>> URUCHAMIANIE AUDYTU BEZPIECZEŃSTWA <<<")
    
    # Automatyczne tworzenie brakujących folderów
    if not os.path.exists(dir_path):
        print(f"[!] Tworzę brakującą ścieżkę: {dir_path}")
        os.makedirs(dir_path)

    # Tworzenie pliku manifestu do testów, jeśli go nie ma
    if not os.path.exists(manifest_path):
        print("[!] Tworzę plik symulacji AndroidManifest.xml...")
        dummy_content = (
            '<?xml version="1.0" encoding="utf-8"?>\n'
            '<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.example.test">\n'
            '    <application android:debuggable="true">\n'
            '        <uses-permission android:name="android.permission.INTERNET"/>\n'
            '        <uses-permission android:name="android.permission.READ_CONTACTS"/>\n'
            '    </application>\n'
            '</manifest>'
        )
        with open(manifest_path, "w", encoding="utf-8") as f:
            f.write(dummy_content)

    # Analiza XML
    dangerous_perms = ['INTERNET', 'READ_CONTACTS', 'CAMERA', 'WRITE_EXTERNAL_STORAGE']
    found_risky = []

    tree = ET.parse(manifest_path)
    root = tree.getroot()
    
    # Szukanie flagi debuggable
    app_tag = root.find('application')
    is_debug = app_tag.get('{http://schemas.android.com/apk/res/android}debuggable', 'false')

    # Szukanie uprawnień
    for perm in root.findall('uses-permission'):
        name = perm.get('{http://schemas.android.com/apk/res/android}name', '')
        for dangerous in dangerous_perms:
            if dangerous in name:
                found_risky.append(name)

   
    with open("RiskyPermission.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<SecurityAudit>\n')
        f.write(f'  <Flags>\n    <Debuggable>{is_debug}</Debuggable>\n  </Flags>\n')
        f.write('  <RiskyPermissions>\n')
        for p in found_risky:
            f.write(f'    <Permission>{p}</Permission>\n')
        f.write('  </RiskyPermissions>\n')
        f.write('</SecurityAudit>')

    print(f"[SUCCESS] Wygenerowano raport: RiskyPermission.xml")
    print(f"[INFO] Flaga Debuggable: {is_debug}")
    print(f"[INFO] Znaleziono ryzykownych uprawnień: {len(found_risky)}")

if __name__ == "__main__":
    scan_manifest()