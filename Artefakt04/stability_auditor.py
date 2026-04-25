import json
from collections import Counter

INPUT_FILE = "miner_report.json"
OUTPUT_FILE = "stability_report.json"

def audit_stability():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        selectors = json.load(f)

    tags = []
    ids = []
    accessibility_ids = []

    for item in selectors:
        if "error" in item:
            continue

        tag = item.get("tag")
        resource_id = item.get("id")
        accessibility_id = item.get("accessibilityId")

        if tag:
            tags.append(tag)
        if resource_id:
            ids.append(resource_id)
        if accessibility_id:
            accessibility_ids.append(accessibility_id)

    total = len(tags)
    tag_counter = Counter(tags)
    id_counter = Counter(ids)

    metrics = []
    for tag, count in tag_counter.most_common():
        percent = round((count / total) * 100, 2) if total else 0
        risk = "HIGH" if percent >= 50 else "MEDIUM" if percent >= 20 else "LOW"

        metrics.append({
            "selectorType": tag,
            "objects": count,
            "classDominanceIndex": f"{percent}%",
            "risk": risk
        })

    duplicate_ids = {
        selector_id: count
        for selector_id, count in id_counter.items()
        if count > 1
    }

    high_risk_items = [m for m in metrics if m["risk"] == "HIGH"]

    if high_risk_items or duplicate_ids:
        verdict = "MEDIUM_RISK"
    else:
        verdict = "LOW_RISK"

    report = {
        "summary": {
            "totalObjects": total,
            "uniqueIds": len(set(ids)),
            "accessibilityIds": len(accessibility_ids),
            "duplicateIds": len(duplicate_ids),
            "verdict": verdict
        },
        "metrics": metrics,
        "duplicateIdsDetails": duplicate_ids,
        "interpretation": (
            "Raport pokazuje, które klasy widoków dominują w layoutach. "
            "Jeżeli jedna klasa, np. TextView lub Button, ma wysoki procent, "
            "to selektory oparte tylko o klasę są niestabilne. "
            "Bezpieczniej używać resource-id albo accessibilityId."
        )
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"Audit Complete. Verdict: {verdict}")
    print(f"Report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    audit_stability()