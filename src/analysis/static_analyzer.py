import subprocess
import json

class StaticAnalyzer:
    def __init__(self):
        self.tools = {
            "semgrep": "semgrep --config auto --json",
            "bandit": "bandit -r . -f json"
        }
    
    def run_scan(self, tool):
        result = subprocess.run(
            self.tools[tool].split(), 
            capture_output=True, 
            text=True
        )
        return json.loads(result.stdout)

# Example usage:
# analyzer = StaticAnalyzer()
# analyzer.run_scan("semgrep")
