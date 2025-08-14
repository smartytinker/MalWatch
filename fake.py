import os
import tempfile
import subprocess
import winreg
import time
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, "logs")

def create_fake_exe():
    fake_dir = os.path.join(LOGS_DIR, "FakeMalware")
    os.makedirs(fake_dir, exist_ok=True)
    fake_exe = os.path.join(fake_dir, "evil.exe")
    with open(fake_exe, "w", encoding="utf-8") as f:
        f.write("This is a fake malware executable.")
    return fake_exe

def add_registry_persistence(exe_path):
    try:
        reg_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0, winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(reg_key, "FakeMalware", 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(reg_key)
    except Exception as e:
        print(f"[!] Registry write failed: {e}")

def create_temp_files():
    os.makedirs(LOGS_DIR, exist_ok=True)
    for i in range(5):
        temp_file = os.path.join(tempfile.gettempdir(), f"fake_file_{i+1}.tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(f"Fake content {i+1}")
        time.sleep(0.3)

def simulate_network():
    try:
        requests.get("http://example.com", timeout=2)
    except Exception:
        print("[*] Network sim failed (expected)")

def spawn_process():
    subprocess.Popen(["notepad.exe"])

def main():
    print("[*] Starting fake malware simulation...")
    os.makedirs(LOGS_DIR, exist_ok=True)
    exe_path = create_fake_exe()
    add_registry_persistence(exe_path)
    create_temp_files()
    simulate_network()
    spawn_process()
    print("[*] Simulation complete.")

if __name__ == "__main__":
    main()
