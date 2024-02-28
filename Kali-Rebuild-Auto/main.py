import os
import colorama
from colorama import Fore, Back, Style
import subprocess
import getpass
import re
import sys
import time
#import ipcalc

import string

# Import all lib
from lib import addUser, updatePostgres, upgrade, installTools, cleanup

# To confirm Linux distribution in /etc/os-release
def get_distroName():
    
    try:
        
        with open('/etc/os-release', 'r') as os_release_file:
            
            for line in os_release_file:
                
                if line.startswith('ID='):
                    
                    distro = line.split('=')[1].strip().strip('"')
                    
                    # Extact distribution name and remove quotes
                    return distro
                
    except FileNotFoundError:
        print(Fore.RED + f'Could NOT confirm Linux Distribution...\nSkipping...\n')
        return None

# Move distroName outside the function
distroName = get_distroName()

#distroName = f"Current distro name is: {getDistro}"
#print(Fore.MAGENTA + distroName)
echoDistroName = f"Current distro name is :{distroName}"
print(Fore.MAGENTA + echoDistroName)
#print(type(distroName))

# A function to return all essential Python modules
def initializeModules():
    
    global os, Fore, Back, Style, getpass, subprocess, re

    # Initialize colorama
    colorama.init(autoreset=True)

    return os, Fore, Back, Style, getpass, subprocess, re
    # Initialize all modules

# Getting ROOT priviledge from users to allow sudo actions
def getCredentials():
    
    try:
        
        print(Fore.WHITE + "\nProceeding...\n")
        
        get_user = f'whoami'
        do_get_user = subprocess.run(
            get_user, 
            shell=True,
            text=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
            )
        
        if do_get_user.returncode == 0:
            user = do_get_user.stdout
            print(f'Current user: {do_get_user.stdout}')
        else:
            print(Fore.RED + f'Failed to {get_user}')
            print(f'Current user: {do_get_user.stderr}')
            #user = do_get_user.stderr
            sys.exit()


        
        sudo_password = getpass.getpass(prompt='Enter sudo password: ')
        
        # Define special characters
        special_characters = string.punctuation
        
        # Check if any special characters are in the password
        if any(char in special_characters for char in sudo_password):
            print(Fore.RED + f'This Script does NOT support sudo_password with Special Characters OR Symbols :(\n\nExiting...\n')
            sys.exit()
        else:
            print(Fore.WHITE + f'sudo_password is accepted ;)\nProceeding...\n')
        
        return user, sudo_password

    except Exception as e:
        
        # Handle exceptions
        print(Fore.RED + f'Error retrieving root credentials from script user: {str(e)}')
        print(Fore.WHITE + f'{do_get_user.stderr}')
        
        print(Fore.RED + 'Terminating script running & all Shell processes...\n')
        sys.exit()

# Returning user, sudo_password from getCredentials()
user, sudo_password = getCredentials()

directory1 = f'/home/{user}'
mkdir1 = f'echo {sudo_password} | sudo mkdir /home/{user}'
do_mkdir1 = subprocess.run(
    mkdir1,
    shell=True,  
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
    )
   
if do_mkdir1.returncode == 0:
        
    print(f'\n')
    print(f'{do_mkdir1.stdout}')
    print(f'\n')
        
else:
    print(f'\n')
    print(f'{do_mkdir1.stderr}')
    print(f'\n')

directory2 = f'/home/{user}/Desktop'
mkdir2 = f'echo {sudo_password} | sudo mkdir /home/{user}'
do_mkdir2 = subprocess.run(
    mkdir2,  
    shell=True,
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
    )
   
if do_mkdir2.returncode == 0:
        
    print(f'\n')
    print(Fore.WHITE + f'{do_mkdir2.stdout}')
    print(f'\n')
        
else:
    print(f'\n')
    print(Fore.RED + f'{do_mkdir2.stderr}')
    print(f'\n')
        
directory3 = f'/home/{user}/Desktop/tools'
mkdir3 = f'echo {sudo_password} | sudo mkdir /home/{user}'
do_mkdir3 = subprocess.run(
    mkdir3, 
    shell=True,
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
    )
   
if do_mkdir3.returncode == 0:
        
    print(f'\n')
    print(Fore.WHITE + f'{do_mkdir3.stdout}')
    print(f'\n')
        
else:
    print(f'\n')
    print(Fore.RED + f'{do_mkdir3.stderr}')
    print(f'\n')
    

def getTime():
    
    try:
        
        # Get current local time as a struct time OBJ
        current_time = time.localtime()
        formatted_time = time.strftime('%Y-%m-%d-%H:%M:%S', current_time)
        
        return formatted_time
    
    except Exception as e:
        
        print(Fore.RED + f'Failed to retrieve current time :(\n')

# Retreiving current formatted time from getTime()
formatted_time = getTime()
    

confirmAddUser = input("Do you wanna add a new priviledged user? [Y/N]: ")

# Passing newUser, newPassword inputs from passingUser() to this.module
#newUser,newPassword = passingUser()
# Whether addUser()
if confirmAddUser.lower() == 'y':
    
    # Adding a new privileged user
    # Sanity checks
    newUser = input("Enter new privileged user name: ")
    newPassword = getpass.getpass("Enter your new privileged user password: ")
    confirmNewPassword = getpass.getpass("Enter your new privileged user password: ")

    if newPassword == confirmNewPassword:
        
        print(Fore.YELLOW + f'Will add a new privileged user {newUser}\nnewPassword: {newPassword}\nfor you as {user} :)\nStarting at {formatted_time}')
        # If newPassword == confirmNewPassword
        # Run addUser() callback from ./lib/addUser.py
        addUser.addUser(user, sudo_password, newUser, newPassword, formatted_time)

    else:

        print(Fore.YELLOW + f'NOT gonna add a new priviledged user\nSkipping...\n')

else:
    print(Fore.YELLOW + f'NOT gonna add a new priviledged user\nSkipping...\n')
    #return None, None

# To update PostgreSQL 15 && 14 TCP ports (5432 && 5433)
confirmUpdatePostgres = input("Do you wanna update PostgreSQL14 & 15 ports 5432? [Y/N]: ")
   
# Whether updatePostgresql()
if confirmUpdatePostgres.lower() == 'y':
    
    print(Fore.YELLOW + f'Will update postgreSQL 15 & 14 ports :)...\n')
    updatePostgres.updatePostgres(user, sudo_password, formatted_time)

else:
    
    print(Fore.YELLOW + f'NOT gonna update postgreSQL 15 & 14 ports\nSkipping...\n')    



# To update http.kali.org => https.kali.org
confirmUpgrade = input("Do you wanna upgrade apt & kali repo? [Y/N]: ").strip()    



## For installing open-source tools
confirmInstallTools = input("Do you wanna install tools? [Y/N]: ")

    
# Whether upgrade()
if confirmUpgrade.lower() == 'y':
    
    print(Fore.YELLOW + f'\n\nWill update Kali repository connection using HTTPS\nto allow apt update && apt upgrade\n\n')
    upgrade.upgrade(user, sudo_password, formatted_time)
    
else:
    
    print(Fore.YELLOW + f'\n\nWill NOT update Kali repository\n\nYou have to manually edit Kali repository config file\nhttp://kali.org => https://kali.org\nAND update the Kali keys from Kali archive\nin order to get apt install functions working...\n\n')
    #confirmUpgrade = 'n'

# Whether installTools()
if confirmInstallTools.lower() == 'y':
    
    print(Fore.YELLOW + f'Will install Open-source tools for you ;)')    
    
    print(f'\n')
    print(f'Package managers\n[e.g. Python3-pip, SNAP, GEM, NixNote2, Nautilus-dropbox, Keepassxc, DNF\n')
    print(Fore.YELLOW + f'')
    
    newUser = input('Enter newUser for Attack Tools [root]: ')
    newPassword = getpass.getpass('Enter newPassword for Tools: ')
    
    installTools.installTools(user, sudo_password, formatted_time, newUser, newPassword)

else:
    
    print(f'\n')
    print(Fore.YELLOW + f'NOT want to install open-source tools\nSkipping...')
    print(f'\n')
    print(f'\n')
    
## For customizing a NIC
# confirmNetworking = input("Do you wanna configure a network interface? [Y/N]: ")
# def passingNetworking():

#     if confirmNetworking and confirmNetworking.lower() == 'y':

#         print(Fore.YELLOW + f'\nWill set up a NIC for you :)\n')
#         return confirmNetworking

#     else:

#         print(Fore.YELLOW + f'\nNot gonna set up a NIC\nSkipping...\n')

# confirmNetworking = passingNetworking()

## For customizing Keyboard Layout
# confirmChangeKeyboardLayout = input("Do you wanna change keyboard layout? [Y/N]: ")

# def passingKeyboard():

#     if confirmChangeKeyboardLayout and confirmChangeKeyboardLayout.lower() == 'y':
#         
#         print(Fore.YELLOW + f'\nWill change keyboard layout :)\n')
#         return confirmChangeKeyboardLayout

#     else:

#         print(Fore.YELLOW + f'\nNot gonna change keyboard layout\n')

# confirmChangeKeyboardLayout = passingKeyboard()

