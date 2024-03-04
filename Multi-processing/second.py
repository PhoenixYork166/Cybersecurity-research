# Testing to create many processes
import multiprocessing
import os

#input_processes = input('Please enter number of processes [500]: ')
input_processes = 10


def print_cube(num):
    print(f'os.getpid(): {os.getpid()}')
    print(f'Cube: {num * num * num}')


def print_square(num):
    print(f'os.getpid(): {os.getpid()}')
    print(f'Square: {num * num}')
    
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
        p = multiprocessing.Process(target=print_square, args=(i,))

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
        
if __name__ == '__main__':
    main()
    
    