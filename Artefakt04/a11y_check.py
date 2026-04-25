import json
import glob
import os
import xml.etree.ElementTree as ET

ANDROID_NS = "{http://schemas.android.com/apk/res/android}"
ANDROID_ID = ANDROID_NS + "id"
ANDROID_TEXT = ANDROID_NS + "text"
ANDROID_CONTENT_DESC = ANDROID_NS + "contentDescription"

LAYOUT_PATH = "../decompiled_apk/res/layout"
OUTPUT_FILE = "a11y_report.json"

def clean_id(value):
    if not value:
        return "no-id"
    return value.split("/")[-1]

def main():
    gaps = []

    files = glob.glob(os.path.join(LAYOUT_PATH, "**", "*.xml"), recursive=True)

    for file in files:
        try:
            tree = ET.parse(file)

            for elem in tree.iter():
                node_text = elem.get(ANDROID_TEXT)
                node_desc = elem.get(ANDROID_CONTENT_DESC)
                node_id = elem.get(ANDROID_ID)

                if node_text and not node_desc:
                    gaps.append({
                        "file": os.path.basename(file),
                        "id": clean_id(node_id),
                        "text": node_text,
                        "issue": "Brak atrybutu contentDescription"
                    })

        except Exception as e:
            gaps.append({
                "file": os.path.basename(file),
                "error": str(e)
            })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(gaps, f, indent=2, ensure_ascii=False)

    print(f"[OK] A11y report generated: {OUTPUT_FILE}")
    print(f"[OK] Found {len(gaps)} accessibility gaps")

if __name__ == "__main__":
    main()