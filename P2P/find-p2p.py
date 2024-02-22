#!/usr/bin/env python3
from scapy.all import ARP, Ether, srp
import ipaddress

__subnet__ = input('Enter networkAddr/CIDR [192.168.2.0/23]: ')
def detect_ptp_link(subnet):
    try:
        # Generate IP addresses to scan
        addresses = ipaddress.ip_network(subnet)
        # Create ARP request packet
        arp_request = ARP(pdst=str(subnet))
        ether_broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = ether_broadcast / arp_request

        # Send the packets and get answers
        answered, _ = srp(arp_request_broadcast, timeout=2, verbose=False)

        # Analyze responses
        if len(answered) == 1:
            print(f"Point-to-point link detected with device at {answered[0][1].psrc}")
        else:
            print("This does not seem to be a point-to-point link.")

    except ValueError as e:
        print(f"Error: {e}")

# Example usage:
# Replace '192.168.1.0/30' with the subnet you want to scan.
detect_ptp_link(__subnet__)