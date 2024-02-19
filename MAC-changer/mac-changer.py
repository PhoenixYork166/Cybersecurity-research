# To stay Anonymous
# Impersonate other devices
# Bypass Filters

# #!/usr/bin/env python3
# Use terminal ;)
import subprocess
# Styling Python ;)
from colorama import Fore, Back, Style
# Timing ;)
import time
# import optparse

# parser = optparse.OptionParser()

#parser.add_option('-i', '--interface', dest='interface', help='NIC to change its MAC addr ;)')
#parser.add_option('-m', '--mac', dest='new_mac', help='New MAC addr ;)')
#(options, arguments) = parser.parse_args()

ifconfig = f'ifconfig'
NIC = input(f'Enter NIC name to change MAC addr [eth0]: ')
new_MAC = input(f'Enter new MAC addr for {NIC} [00:5c:56:aa:bb:cc]: ')

# Get current local time as a struct time OBJ
current_time = time.localtime()
formatted_time = time.strftime('%Y-%m-%d-%H:%M:%S', current_time)

def changeMAC():
    do_ifconfig = subprocess.Popen(ifconfig, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = do_ifconfig.communicate()

    if do_ifconfig.returncode == 0:
        print(f'Succeeded in running {ifconfig}')
        print(f'{out}')
    else:
        print(f'Failed to run {ifconfig}')
        print(f'{err}')
        
    # Turning of NIC before changing MAC addr
    NIC_off = f'{ifconfig} {NIC} down'
    do_NIC_off = subprocess.Popen(NIC_off, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    do_NIC_off_out, do_NIC_off_err = do_NIC_off.communicate()

    if do_NIC_off.returncode == 0:
        print(f'\n')
        print(f'{do_NIC_off_out}')
        print(f'Succeeded in turning of {NIC}')
    else:
        print(f'\n')
        print(f'{do_NIC_off_err}')
        print(f'Failed to turn off {NIC}')
            
    change_MAC = f'{ifconfig} {NIC} hw ether {new_MAC}'
    do_change_MAC = subprocess.Popen(change_MAC, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    do_change_MAC_out, do_change_MAC_err = do_change_MAC.communicate()

    if do_change_MAC.returncode == 0:
        print(f'\n')
        print(f'{do_change_MAC_out}\nat {formatted_time}')
        print(f'\n')
        print(f'\n')
    else:
        print(f'\n')
        print(f'{do_change_MAC_err}\nat {formatted_time}')
        print(f'\n')
        print(f'\n')

    # Bring NIC back online
    NIC_on = f'{ifconfig} {NIC} up'
    do_NIC_on = subprocess.Popen(NIC_on, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    do_NIC_on_out, do_NIC_on_err = do_NIC_on.communicate()

    if do_NIC_on.returncode == 0:
        print(f'\n')
        print(f'{do_NIC_on_out}')
        print(f'Succeeded in turning ON {NIC}')
    else:
        print(f'\n')
        print(f'{do_NIC_on_err}')
        print(f'Failed to turn ON {NIC}')
        
    # Force restart networking.service
    restartNetwork = f'/etc/init.d/networking restart'
    do_restartNetwork = subprocess.Popen(restartNetwork, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    do_restartNetwork_out, do_restartNetwork_err = do_restartNetwork.communicate()
    if do_restartNetwork.returncode == 0:
        print(f'\n')
        print(Fore.WHITE + f'{do_restartNetwork_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in restarting network.service ;)\nat {formatted_time}')
        print(f'\n')
        print(f'\n')        

# if this script = main script => Execute
if __name__ == '__main__':
    changeMAC()


