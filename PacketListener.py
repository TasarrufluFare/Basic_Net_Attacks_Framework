import scapy.all as scapy
from scapy_http import http


def listen_packets(interface):
    print("------------------------------------------------")
    print("Packet Listener has started working.")
    scapy.sniff(iface=interface, store=False, prn=analyze_packets)


def analyze_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

