import subprocess
import os

# Project root = folder containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths within the repo
PROC_PATH = os.path.join(BASE_DIR, "tools", "Procmon64.exe")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
PML_PATH = os.path.join(LOGS_DIR, "procmon_log.pml")
CSV_PATH = os.path.join(LOGS_DIR, "capture.csv")

def convert():
    if not os.path.exists(PML_PATH):
        print(f"[!] No PML log found at: {PML_PATH}")
        return False

    if not os.path.exists(PROC_PATH):
        print(f"[!] Procmon not found at: {PROC_PATH}")
        return False

    os.makedirs(LOGS_DIR, exist_ok=True)
    subprocess.run([PROC_PATH, "/OpenLog", PML_PATH, "/SaveAs", CSV_PATH], check=False)
    print(f"[✓] CSV saved to {CSV_PATH}")
    return True
