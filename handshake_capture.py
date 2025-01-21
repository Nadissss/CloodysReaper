import os

def capture_handshake(interface, bssid, output):
    
    """
    Captures WiFi handshakes using airodump-ng.

    Args:
        interface (str): Network interface in monitor mode.
        bssid (str): Target WiFi network BSSID.
        output (str): File to save handshake data.
    """
    print(f"[*] Capturing handshake for BSSID: {bssid} on interface: {interface}")
    try:
        # Run airodump-ng
        os.system(f"airodump-ng -w {output} --bssid {bssid} {interface}")
    except Exception as e:
        print(f"[!] Error: {e}")
