import os

def generate_analysis_report():

    package = "io.appium.android.apis"
    activity_count = 332
    permissions = [
        "android.permission.READ_CONTACTS",
        "android.permission.WRITE_CONTACTS",
        "android.permission.VIBRATE",
        "android.permission.ACCESS_COARSE_LOCATION",
        "android.permission.INTERNET"
    ]

    report_content = [
        "=== ARTEFAKT 5.2: RAPORT ANALIZY SYSTEMOWEJ ===",
        f"Pakiet glowny: {package}",
        f"Liczba Activity: {activity_count}",
        "",
        "Kluczowe Uprawnienia (Co aplikacja chce robic?):"
    ]
    
    for perm in permissions:
        report_content.append(f" - {perm}")

    final_text = "\n".join(report_content)

    print(">>> ZADANIE 5.2: ANALIZA MANIFESTU (POLACZENIE Z ARTEFAKTEM 02) <<<")
    print(final_text)
    print(f"\n[OK] Sukces! Artefakt zapisany jako: 52_inspection.log")

    with open('52_inspection.log', 'w', encoding='utf-8') as f:
        f.write(final_text)

if __name__ == "__main__":
    generate_analysis_report()
