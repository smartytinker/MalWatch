import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "logs", "capture.csv")

def parse_csv():
    results = {"files written": [], "registry mods": [], "network access": []}

    if not os.path.exists(CSV_PATH):
        print(f"[!] CSV not found at: {CSV_PATH}")
        return results

    with open(CSV_PATH, newline='', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            path = row.get("Path", "")
            op = row.get("Operation", "")

            if "WriteFile" in op:
                results["files written"].append(path)
            elif "RegSetValue" in op or "RegCreateKey" in op:
                results["registry mods"].append(path)
            elif "TCP" in op or "UDP" in op:
                results["network access"].append(path)

    return results
