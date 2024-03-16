import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    
    # Trimming all fucking \r\n from Bytes req/res
    cmd = cmd.strip()
    
    if not cmd:
        return
    
    # If cmd object does NOT exist
    # standard error = subprocess standard output
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    
    return output.decode()  

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        # Using '''Content''' to handle large comment blocks
        # Educating users how to parse inputs to this netcat python tool
        # Accept users' inputs in terminal parser
        # Flagging:
        # -t = host
        # -p = port
        # -l = listening
        # -u = upload a file
        # -c = cmd command
        # -e = execute shell command
        epilog=textwrap.dedent('''Example: 
                               netcat.py -t 192.168.0.168 -p 5555 -l -c 
                               netcat.py -t 192.168.0.168 -p 5555 -l -u=mytest.txt
                               netcat.py -t 192.168.0.168 -p 5555 -l -e=\"cat /etc/passwd"
                               echo "ABC" | ./netcat.py -t 192.168.0.168 -p 135 
                               netcat.py -t 192.168.0.168 -p 5555
                               ''')
        )

    # Handling -c flag command execution
    parser.add_argument('-c', '--command', action='store_true', help='command shell:\nnetcat.py -t 192.168.0.168 -p 5555 -l -c')
    parser.add_argument('-e', '--execute', help='Execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen mode')
    parser.add_argument('-p', '--port', type=int, default=5555, help='Specify a port [5555]')
    parser.add_argument('-t', '--target', default='127.0.0.1', help='Specify a host IP')
    parser.add_argument('-u', '--upload', help='Upload a file')
    
    # Instantiate arguments from users' inputs
    args = parser.parse_args()
    
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
    
    nc = NetCat(args, buffer.encode())
    