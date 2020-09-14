import scapy.all as scapy
import optparse

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-t", "--target", dest= "target ", help = "please enter the ip address to get the mac")
    (options, arguments)= parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst= ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 2, verbose =False)[0]


    client_list =[]

    for elemnent in answered_list:
        client_dict= {"ip":elemnent[1].psrc, "mac":  elemnent[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(result_list):
    print("IP\t\t\tMac Addr\n..............................................")
    for client in result_list:
        print(client["ip"] + "\t\t"+ client["mac"])


scan_result = scan("IP_Segment")
print_result(scan_result)
options = get_arguments()






