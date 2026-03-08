from scapy.all import *

def process_packet(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"\n📡 Packet Captured")
        print(f"Source IP      : {ip_layer.src}")
        print(f"Destination IP : {ip_layer.dst}")
        print(f"Protocol       : {ip_layer.proto}")

def start_sniffing():
    print("🔍 Starting Packet Sniffer... Press Ctrl+C to stop.\n")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    start_sniffing()