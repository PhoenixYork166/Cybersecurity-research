#!/usr/bin/python3

import sys
from scapy.all import *


class scapy_demo(object):

    # Using a constructor
    # must remove arg in __init__
    def __init__(self):

        # super to inherit class
        super(scapy_demo, self).__init__()
        
        # do nothing
        pass

    # Passing in pcap file to main()
    def main(self, pcap_file):
        
        # read the .pcap file from argument
        # store .pcap to pcap variable
        pcap = rdpcap(pcap_file)

        # Printing output of pcap sessions
        pcap_sessions = pcap.sessions()
        print(f'pcap_sessions:\n{pcap_sessions}')
        print(f'\n')

        # Preparing to store source IPs into an empty set
        src_ips = set()
        print(f'Printing out source IP as a set\n')

        for pkt in pcap:
            try:
                src_ips.add(pkt[IP].src)
                #print(pkt[IP].src)
            except IndexError:
                pass
        
        # Printing out src_ips{} to screen
        print(f'src_ips:\n{src_ips}')

if __name__ == '__main__':

    # If user only run the script
    # without any arguments after scapy-demo1.py
    if len(sys.argv) <= 1:
        sys.exit(f'You must provide a pcap!!\npython3 scapy-demo1.py <.pcap>')

    # first, instantiate the class
    scapy_demo = scapy_demo()

    # Getting user input value
    scapy_demo.main(sys.argv[1])

    
    