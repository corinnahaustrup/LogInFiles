# Python Log Analyzer
A Python project that analyzes server logs to detect brute-force attacks.

## The Program
* Reads a server log file.
* Counts failed login attempts per IP address.
* Warns if an IP has 3+ failed attempts.
* Validates IP addresses correctly.

## How to Run
To generate the log file and run the analysis, use the following commands:
```bash
python server.py       # Creates server.log
python LogInFiles.py   # Analyzes the log file
```

## Example Output
```text
--- Analyzing Logs ---
[WARNING] Potential brute-force attack from IP: 192.168.1.50 (5 failed attempts)
[INFO] Minor failed attempts from IP: 172.16.0.4 (1)
```

## Skills Demonstrated
* Regular expressions (regex)
* File handling in Python
* IP address validation
