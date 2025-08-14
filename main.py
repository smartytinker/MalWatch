import os
import subprocess
from malware_runner import run_sample
from log_parser import convert
from report_builder import parse_csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def runprocmon():
    print("[*] Starting Procmon capture...")
    # run_procmon.bat lives next to this script; use relative call
    subprocess.run(["cmd", "/c", "run_procmon.bat", str()], shell=True)
    print("[*] Procmon capture finished.")

if __name__ == "__main__":
    # Sample expected at project/dist/fake.exe (you can replace with your own)
    malwarepath = os.path.join(BASE_DIR, "dist", "fake.exe")
    if not os.path.exists(malwarepath):
        print(f"[!] Sample not found at {malwarepath}. Build or place your sample there.")
    else:
        # Start the sample, then capture via Procmon for <duration> seconds
        run_sample(malwarepath)

    runprocmon()

    if convert():
        report = parse_csv()

        print("\n=== Malware Behaviour Summary ===\n")

        print("[Files Written]")
        for item in report["files written"][:10]:
            print(f" - {item}")

        print("\n[Registry Modified]")
        for item in report["registry mods"][:10]:
            print(f" - {item}")

        print("\n[Network Access]")
        for item in report["network access"][:10]:
            print(f" - {item}")
