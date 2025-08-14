# MalWatch

MalWatch is a simple malware behavior monitoring tool that uses [Sysinternals Procmon](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon) to capture file, registry, and network activity of a sample running in a sandbox environment.

## Features
- **Automated Procmon Capture** – Starts and stops Procmon automatically.
- **Headless Logging** – Logs all events to a `.pml` file without requiring user interaction.
- **CSV Output** – Automatically converts the `.pml` log into CSV for easy analysis.
- **Behavior Summary** – Prints a quick summary of files written, registry keys modified, and network connections.

## Requirements
1. **Windows OS** (Procmon is Windows-only)
2. **Python 3.8+**
3. **Procmon64.exe**  
   Download from Microsoft Sysinternals:  
   https://learn.microsoft.com/en-us/sysinternals/downloads/procmon
4. **Required Python packages**  
   ```bash
   pip install pandas
   ```

## Folder Structure
```
MalWatch-main/
│
├── main.py                 # Main Python script
├── procmon_capture.bat     # Batch script to run Procmon in background
├── tools/
│   └── Procmon64.exe       # Sysinternals Process Monitor
├── logs/
│   ├── procmon_log.pml     # Raw Procmon log (binary format)
│   └── capture.csv         # Converted CSV log
└── dist/
    └── fake.exe            # Sample executable to monitor
```

> **Note:** `fake.exe` is **safe** — it is a harmless demonstration file that simulates basic activity for testing purposes.  
> It is **not** malicious.

## Usage
### 1. Run MalWatch
```bash
python main.py
```

By default:
- Runs `dist/fake.exe` as the malware sample.
- Captures Procmon logs for **30 seconds**.
- Converts logs to `logs/capture.csv`.
- Prints a behavior summary in the console.

### 2. Custom Duration
You can specify the duration (in seconds) when calling the batch file directly:
```bash
procmon_capture.bat 10
```
This will capture for 10 seconds instead of 5.

## Output
Example behavior summary:
```
=== Malware Behaviour Summary ===

[Files Written]
 - C:\ProgramData\Example\file.tmp

[Registry Modified]
 - HKCU\Software\Example

[Network Access]
 - example.local:12345 -> example.local:80
```

## Why Pandas is Used
- **Easy CSV Parsing** – Pandas reads large Procmon CSV logs without manual parsing.
- **Fast Filtering** – Quickly search for specific operations (e.g., WriteFile, RegSetValue).
- **Deduplication** – Remove duplicate entries in one line.
- Without pandas, you'd need more code and it would be slower for large logs.

## Notes
- **Sandbox Usage** – Always run suspicious samples inside an isolated VM or controlled environment.
- **Admin Rights** – Procmon may require Administrator privileges to capture all events.
- **PML to CSV Conversion** – The Python script handles conversion, but you can manually convert via Procmon GUI if needed.

## License
This project is for educational and research purposes only. Use at your own risk.
