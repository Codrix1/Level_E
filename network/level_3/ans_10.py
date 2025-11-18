from scapy.all import sniff

def show_packet(packet):
    print(packet.summary())
print("Sniffing packets... press Ctrl+C to stop.")

sniff(prn=show_packet, count=0) 