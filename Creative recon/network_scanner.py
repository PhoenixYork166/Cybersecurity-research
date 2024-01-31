import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    return parser.parse_args()

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_boardcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_boardcast, timeout=10, verbose=True)[0]
    
    clients_list = []

    for e in answered_list:
        clients_dict = {"ip": e[1].psrc, "mac": e[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list

def print_result(results):
    print("IP\t\t\tMAC Address\n--------------------------------------")
    for client in results:
        print(client["ip"] + "\t\t" + client["mac"])

scan_result= scan(get_arguments().target)
print_result(scan_result)