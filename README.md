# SecOS-Defender
A framework to detect and mitigate OS vulnerabilities like buffer overflows.

## Setup
1. Install: `sudo apt install gcc libasan6 python3-pip; pip3 install flask`
2. Compile: `gcc -fsanitize=address -g vuln.c -o vuln`
3. Run: `./vuln > output.txt`, `python3 alert.py`, `python3 app.py`

## Usage
- Input "AAAAAAAAAA" to trigger overflow.
- Check alerts at http://127.0.0.1:5000.

## Screenshot
(Imagine a Flask UI with "Buffer Overflow Detected" and "Update software")
