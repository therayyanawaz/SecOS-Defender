from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data for alerts
alerts = [
    {"id": 1, "type": "Buffer Overflow", "details": "Detected in vulnerable_function()", "severity": "High"},
    {"id": 2, "type": "Trapdoor", "details": "Unauthorized privilege escalation detected", "severity": "Critical"},
    {"id": 3, "type": "Cache Poisoning", "details": "Unsolicited ARP reply detected", "severity": "Medium"}
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', alerts=alerts)

@app.route('/api/alerts')
def get_alerts():
    return jsonify(alerts)

if __name__ == '__main__':
    app.run(debug=True)
