# --------------
# Imports modules
# --------------
from . import Fore, sys, os, Back, Style, getpass, subprocess, re, time
import ipcalc

# Configure Linux networking at ease :)
def networkConfig(user, sudo_password, formatted_time):
        
    # Configuring a network interface
    nic = input(Fore.YELLOW + f'Enter a network interface iface name [e.g. eth0]: ')
    print(f'\n')
    regex = '^((\w+)|(\d+))$'
    
    validate = re.match(regex, nic)
    #print(Fore.WHITE + f'validate.match: {validate.match}')
    #print(Fore.YELLOW + f'validate boolean: {validate}')

    if validate:
        
        print(Fore.YELLOW + f'Succeeding in passing NIC name check, reasonable ? {validate} :)\nProceeding to configure NIC: {nic}\n')
        ip = input(f'Please enter {nic} IP [e.g. 192.168.0.1]: ')
        
        print(f'\n')
        ipRegex = '((10|1[0-9])|(17[1-9])|(19[1-9]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-4]))$'
        validateIp = re.match(ipRegex, ip)

        if validateIp:
            
            print(Fore.YELLOW + f'validateIp: {validateIp}')
            print(f'\n')
            print(Fore.YELLOW + f'NIC IP: {ip} seems reasonable :)\nProceeding to configure {nic} Netmask...')
            print(f'\n')
            netmask = input(f'Please enter {nic} Netmask: [e.g. 255.255.255.0]')
            print(f'\n')
            netmaskRegex = '^(0|128|192|224|240|248|252|254|255)\.(0|128|192|224|240|248|252|254|255)\.(0|128|192|224|240|248|252|254|255)\.(0|128|192|224|240|248|252|254|255)$'
            print(Fore.YELLOW + f'\n\nCalculating Network Address IP...')
            print(f'\n')
            print(f'\n')
                
            # Calculate Network Address IP
            addr = ipcalc.IP(ip, mask=netmask)
            networkAddressIP = str(addr.guess_network())
            print(Fore.WHITE + f'\n\nCalculated Network Address IP: {networkAddressIP}')
            print(f'\n')
            print(f'\n')
            
            validateNetmask = re.match(netmaskRegex, netmask)

            if validateNetmask:
                
                print(Fore.YELLOW + f'{nic} Netmask: {netmask} seems reasonable :)')
                print(f'\n')
                print(Fore.YELLOW + f'\n\nCalculating Network Address IP...')
                print(f'\n')
                
                # Converting Netmask to CIDR [e.g. /24]
                cidr = sum(bin(int(x)).count('1') for x in netmask.split('.'))
                print(f'\n')
                print(f'\n')
                print(Fore.YELLOW + f'CIDR: {cidr}') 
                print(f'\n')
                print(f'\n')
                
                gateway = input(f'Please enter {nic} Default Gateway [e.g. 192.168.0.254]')
                print(f'\n')
                
                gatewayRegex = '((10|1[0-9])|(17[1-9])|(19[1-9]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-4]))$'
                validateGateway = re.match(gatewayRegex, gateway)

                if validateGateway:
                    
                    print(Fore.YELLOW + f'{nic} gateway: {gateway} seems reasonable :)\nProceeding to create this NIC...')
                    print(f'\n')
                    
                    # Adding this NIC configuration to /etc/network/interfaces
                    addInterface = f'echo {sudo_password} | sudo printf "\nauto {nic}\niface {nic} inet static\naddress {ip}\nnetmask {netmask}\ngateway {gateway}\nup route add -net {networkAddressIP} netmask {netmask} gw {gateway}" >> /etc/network/interfaces'
                    doAddInterface = subprocess.Popen(addInterface, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    doAddInterface_out, doAddInterface_err = doAddInterface.communicate()
                        
                    if doAddInterface.returncode == 0:
                        
                        print(f'\n')
                        print(Fore.WHITE + f'{doAddInterface_out}')
                        print(f'\n')
                        print(Fore.YELLOW + f'Succeeded in adding {nic} to /etc/network/interfaces :)\nProceeding to restart networking.service using systemctl!')
                        print(f'\n')
                        print(f'\n')
                        print(Fore.YELLOW + f'Adding DNS server to /etc/resolv.conf')
                        resolvConf = f'/etc/resolv.conf'
                        dns_server = f'echo {sudo_password} | printf "nameserver {gateway}" >> {resolvConf}'
                        add_dns_server = subprocess.Popen(dns_server, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        add_dns_server_out, add_dns_server_err = add_dns_server.communicate()
                        
                        if add_dns_server.returncode == 0:
                            
                            print(f'\n')
                            print(Fore.WHITE + f'{add_dns_server_out}')
                            print(f'\n')
                            print(Fore.YELLOW + f'Succeeded in adding a new DNS server to {resolvConf} at {formatted_time}')
                            print(f'\n')
                            print(f'\n')
                            
                        else:
                            
                            print(f'\n')
                            print(Fore.WHITE + f'{add_dns_server_err}')
                            print(f'\n')
                            print(f'\n')
                            
                        # Restarting networking.service => systemctl stop networking.service
                        stopNetwork = f'echo {sudo_password} | sudo /etc/init.d/networking stop'
                        doStopNetwork = subprocess.Popen(stopNetwork, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        doStopNetwork_out, doStopNetwork_err = doStopNetwork.communicate()

                        if doStopNetwork.returncode == 0:
                            
                            print(f'\n')
                            print(Fore.WHITE + f'{doStopNetwork_out}')
                            print(f'\n')
                            print(Fore.YELLOW + f'Succeeded in stopping networking.service :)\nProceeding to start networking.service at {formatted_time}')
                            print(f'\n')
                                
                            startNetwork = f'echo {sudo_password} | sudo /etc/init.d/networking start'
                            doStartNetwork = subprocess.Popen(startNetwork, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            doStartNetwork_out, doStartNetwork_err = doStartNetwork.communicate()
                            
                            if doStartNetwork.returncode == 0:
                                
                                print(f'{doStartNetwork_out}')
                                print(f'\n')
                                print(Fore.YELLOW + f'Succeeded in starting networking.service :)\nProceeding to sudo ip route add {ip}/{cidr} via {gateway} dev {nic}')
                                print(f'\n')
                                print(f'\n')
                                      
                            else:
                                
                                print(f'\n')
                                print(Fore.WHITE + f'{doStartNetwork_err}')
                                print(f'\n')
                                print(Fore.RED + f'Failed to start networking.service :(\nPlease manually start networking.service by:\nsudo systemctl start networking.service\nExiting...')
                                print(f'\n')
                                print(f'\n')
    
                        # If networking.service could not be stopped => Exit
                        else:
                            
                            print(f'\n')
                            print(Fore.WHITE + f'{doStopNetwork_err}')
                            print(f'\n')
                            print(f'\n')
                            print(Fore.RED + f'\n\nFailed to stop networking.service\nPlease restart networking.service manually by\nsudo systemctl stop networking.service\nsudo systemctl start networking.service\nExiting...')
                            print(f'\n')
                            print(f'\n')

                    else:
                        
                        print(f'\n')
                        print(Fore.WHITE + f'{doAddInterface_err}')
                        print(f'\n')
                        print(Fore.RED + f'Failed to create {nic} in /etc/network/interfaces :(\nExiting...')
                        print(f'\n')
                        print(f'\n')

                # If NIC Gateway is NOT valid => Exit
                else:
                    
                    print(f'\n')
                    print(f'\n')
                    print(Fore.RED + f'{nic} Gateway: {gateway} is NOT valid :(\nExiting...')
                    print(f'\n')
                    print(f'\n')

            # If NIC Netmask is NOT valid => Exit
            else:
                
                print(f'\n')
                print(f'\n')
                print(Fore.RED + f'{netmask} is NOT a valid netmask :(...Proceeding...')
                print(f'\n')
                print(f'\n')

        # If NIC IP is not reasonable => Exit this module
        else:
            
            print(f'\n')
            print(f'\n')
            print(Fore.RED + f'valideIp: {validateIp}')
            print(f'\n')
            print(f'\n')
            print(Fore.RED + f'This NIC IP: {ip} seems NOT reasonable...\nSkipping...')
            print(f'\n')
            print(f'\n')

    # If NIC name is not reasonable => Exit this module
    elif not validate:
        
        print(f'\n')
        print(f'\n')
        print(Fore.RED + f'Failed to pass NIC name check :(\nPlease enter a NIC name with String & Number only :)\ne.g. eth0\ne.g. ens1\nExiting processes...')
        print(f'\n')
        print(f'\n')
