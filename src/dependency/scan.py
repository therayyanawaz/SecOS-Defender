import requests
import json

class DependencyScanner:
    CVE_API = "https://services.nvd.nist.gov/rest/json/cves/1.0"
    
    def check_vulnerability(self, package_name):
        response = requests.get(f"{self.CVE_API}?keyword={package_name}")
        return json.loads(response.text).get("result", {}).get("CVE_Items", [])
