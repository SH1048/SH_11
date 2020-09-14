# SH_11
Python_Files_Ethical_Hacking
import subprocess
import optparse
import re

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="please specify the interface")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="please enter the mac address")
    (options, arguments)= parser.parse_args()
    if not options.interface:
        parser.error ("please specify the proper interface")
    elif not options.new_mac:
        parser.error ("need to enter the new mac")
    return options

def change_mac(interface, new_mac):
    print("[+] chnage the mac addr for " + interface + "to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
print(mac_result.group(0))
