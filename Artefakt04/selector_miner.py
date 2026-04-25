import json
import glob
import os
import xml.etree.ElementTree as ET

ANDROID_ID = "{http://schemas.android.com/apk/res/android}id"
ANDROID_CONTENT_DESC = "{http://schemas.android.com/apk/res/android}contentDescription"

def clean_id(value):
    if not value:
        return None
    return value.split("/")[-1]

def mine_selectors(path):
    result = []

    files = glob.glob(os.path.join(path, "**", "*.xml"), recursive=True)

    for file in files:
        try:
            tree = ET.parse(file)
            root = tree.getroot()

            for element in root.iter():
                resource_id = clean_id(element.get(ANDROID_ID))
                content_desc = element.get(ANDROID_CONTENT_DESC)

                if resource_id or content_desc:
                    result.append({
                        "file": file.replace("\\", "/"),
                        "tag": element.tag,
                        "id": resource_id,
                        "accessibilityId": content_desc
                    })

        except Exception as e:
            result.append({
                "file": file.replace("\\", "/"),
                "error": str(e)
            })

    return result

if __name__ == "__main__":
    layout_path = "../decompiled_apk/res/layout"
    selectors = mine_selectors(layout_path)

    with open("miner_report.json", "w", encoding="utf-8") as f:
        json.dump(selectors, f, indent=2, ensure_ascii=False)

    print(f"[OK] Extracted {len(selectors)} selectors")
    print("[OK] Report saved to miner_report.json")