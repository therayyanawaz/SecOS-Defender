# SecOS-Defender
A framework to detect and mitigate operating system vulnerabilities such as buffer overflows, trapdoors, and cache poisoning.

## Overview
SecOS-Defender is a simple prototype built to simulate a buffer overflow attack, detect it using tools like Address Sanitizer (ASAN), log alerts, and display them with mitigation suggestions on a basic web interface using Flask. It’s designed for Ubuntu Linux and serves as a quick demonstration of vulnerability detection for educational purposes.

## Setup
To get SecOS-Defender running, follow these steps:

1. **Install Dependencies**:
   ```bash
   sudo apt update
   sudo apt install gcc libasan6 python3-pip -y
   pip3 install flask
   ```
2. **Compile the Vulnerable Code**:
   ```bash
   gcc -fsanitize=address -g vuln.c -o vuln
   ```
3. **Run the Framework**:
   - Simulate attack: `./vuln > output.txt` (type "AAAAAAAAAA" when prompted).
   - Detect and log: `python3 alert.py`.
   - Start the web UI: `python3 app.py` (open `http://127.0.0.1:5000` in a browser).

## Usage
- **Simulate a Buffer Overflow**: Run `./vuln` and enter a string longer than 10 characters (e.g., "AAAAAAAAAA") to trigger an overflow.
- **Detect the Issue**: Use `python3 alert.py` to check the output and log an alert to `alerts.log`.
- **View Results**: Visit `http://127.0.0.1:5000` to see the alert (e.g., "Buffer Overflow Detected - High Severity") and a mitigation suggestion (e.g., "Update software, enable ASLR").

## Files
- `README.md`: This documentation.
- `vuln.c`: C code with a vulnerable buffer for simulation.
- `alert.py`: Python script to detect overflows and log alerts.
- `app.py`: Flask app for the web interface.
- `templates/dashboard.html`: Webpage template for displaying alerts and mitigation.
- `mitigations.json`: Contains mitigation suggestions in JSON format.
- `alerts.log`: Sample alert log.
- `output.txt`: Sample output from the simulation.

## Screenshot


## Notes
- Focuses mainly on buffer overflows; trapdoors and cache poisoning are placeholders for future expansion.
- (not a production tool)
