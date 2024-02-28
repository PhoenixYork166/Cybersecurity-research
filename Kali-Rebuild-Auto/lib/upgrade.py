# Import these for every module component
# --------------
# Imports modules
# --------------
from . import Fore, sys, os, Back, Style, getpass, subprocess, re

# Update && upgrade Kali repository
def upgrade(user, sudo_password, formatted_time):

    print(Fore.WHITE + f'******************************************')
    print(Fore.WHITE + f'*****Updating Kali Linux archive keys*****')
    print(Fore.WHITE + f'******************************************')

    print(Fore.YELLOW + f'\nAction 1. Updating expried keys on Kali base-build image\nFrom: https://archive.kali.org/archive-key.asc\nTo: /etc/apt/trusted.gpd.d/kali-archive-keyring.asc\n')
    # Update expired keys on Kali base-build image
    #os.system('sudo wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-keyring.asc')
    updateExpiredKeys = f'echo {sudo_password} | sudo wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-keyring.asc'

    doUpdateExpiredKeys = subprocess.Popen(updateExpiredKeys, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doUpdateExpiredKeys_out, doUpdateExpiredKeys_err = doUpdateExpiredKeys.communicate()

    if doUpdateExpiredKeys.returncode == 0:
        
        print(Fore.WHITE + f'{doUpdateExpiredKeys_out}')
        print(f'\n')
        print(Fore.YELLOW + f'********Succeeded in performing Action 1. Updating expired keys\n{doUpdateExpiredKeys_out}\nat {formatted_time}')
        print(Fore.YELLOW + f'***************************************************************************************************************')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(Fore.WHITE + f'{doUpdateExpiredKeys_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to perform Action 1. Updating expried keys on Kali base-build image\nat\n{formatted_time}')
        print(f'\n')
        print(f'\n')
        
    # Update Kali.org Repo
    # Temporarily changing chmod for /etc/apt/sources.list
    print(Fore.YELLOW + "Changing chmod for /etc/apt/sources.list to 777 temporarily...")
    print(f'\n')
    
    chmod = f'echo {sudo_password} | sudo chmod 777 /etc/apt/sources.list'
    doChmod = subprocess.Popen(chmod, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doChmod_out, doChmod_err = doChmod.communicate()
    
    if doChmod.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChmod_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in temporarily chmod 777 /etc/apt/source.lists')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChmod_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to temporarily chmod 777 /etc/apt/sources.list at {formatted_time}')
        print(f'\n')
        print(f'\n')

    print(Fore.YELLOW + f'Proceeding to configure HTTPS Kali Linux repo...\n')
    
    addDeb = f'echo {sudo_password} | sudo printf "deb https://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src https://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list'
    doAddDeb = subprocess.Popen(addDeb, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doAddDeb_out, doAddDeb_err = doAddDeb.communicate()

    if doAddDeb.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doAddDeb_out}')
        print(f'\n')
        print(Fore.YELLOW + f'\nSucceeded in adding below:\ndeb https://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src https://http.kali.org/kali kali-rolling main non-free contrib\nat:\n{formatted_time}')
        print(Fore.YELLOW + "*******************************************")
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.RED + f'{doAddDeb_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to add following config to /etc/apt/sources.list\ndeb-src https://http.kali.org/kali kali-rolling main non-free contrib\nat {formatted_time}')
        print(f'\n')
        print(f'\n')
        
    # Print /etc/apt/sources.list config
    # No matter changes are made or NOT
    print(Fore.YELLOW + "*******************************************")
    print(Fore.YELLOW + "Current APT config is: \n")
    aptConfig = f'echo {sudo_password} | sudo cat /etc/apt/sources.list'
    printAptConfig = subprocess.Popen(aptConfig, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    printAptConfig_out, printAptConfig_err = printAptConfig.communicate()
    print(Fore.YELLOW + "*******************************************")
    
    if printAptConfig.returncode == 0:
        
        print(f'\n')
        print(f'{printAptConfig_out}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(f'{printAptConfig_err}')
        print(f'\n')
        print(f'\n')
                    
    # Update && Upgrade
    print(Fore.YELLOW + "##########################################################")
    print(Fore.YELLOW + "\n\n### Updating & Upgrading Advanced Package Manager ###\n")
    print(Fore.WHITE + "\nDoing apt update && apt upgrade now...\n")
    
    #os.system('sudo apt update && sudo apt upgrade -yuf')
    updateAndUpgrade = f'echo {sudo_password} | sudo apt update && sudo apt upgrade -yuf'
    doUpdateAndUpgrade = subprocess.Popen(updateAndUpgrade, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doUpdateAndUpgrade_out, doUpdateAndUpgrade_err = doUpdateAndUpgrade.communicate()
            
    if doUpdateAndUpgrade.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doUpdateAndUpgrade_out}')
        print(f'\n')
        print(Fore.YELLOW + f'\nSucceeded in updating && upgrading APT at:\n{formatted_time}')
        print(f'\n')
        print(f'\n')
        print(Fore.YELLOW + f'\nCurrent /etc/apt/sources.list is as following:')
        print(f'\n')
        print(f'\n')
                        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doUpdateAndUpgrade_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to update && upgrade APT at:\n{formatted_time}')
        print(f'\n')
        print(f'\n')

    # Changing chmod for /etc/apt/sources.list back to 644
    print(Fore.YELLOW + "\nChanging chmod for /etc/apt/sources.list back to 644...")
    print(f'\n')
    
    chmodBack = f'echo {sudo_password} | sudo chmod 644 /etc/apt/sources.list'
    doChmodBack = subprocess.Popen(chmodBack, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doChmodBack_out, doChmodBack_err = doChmodBack.communicate()

    if doChmodBack.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChmodBack_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in changing chmod 644 for:\n/etc/apt/sources.list')
        print(f'\n')
        print(f'\n')      
              
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChmodBack_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to change chmod 644 for:\n/etc/apt/sources.list...\nSkipping...')
        print(f'\n')
        print(f'\n')


        

        
    
