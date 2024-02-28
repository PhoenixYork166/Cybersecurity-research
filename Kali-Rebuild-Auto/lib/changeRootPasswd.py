# --------------
# Imports modules
from . import Fore, os, Back, Style, getpass, subprocess, re

def changeRootPasswd(user, sudo_password, formatted_time):

    #sudo_password = getpass.getpass(prompt='Please enter your sudo password: ')
    print(Fore.YELLOW + "### Changing root default pwd ###")

    changeRootPasswd = f'echo {sudo_password} | sudo passwd {user}'
    doChangeRootPasswd = subprocess.Popen(changeRootPasswd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doChangeRootPasswd_out, doChangeRootPasswd_err = doChangeRootPasswd.communicate()

    if doChangeRootPasswd.returncode == 0:
        
        print(f'\n')
        print(doChangeRootPasswd_out)
        print(f'\n')
        print(Fore.YELLOW + f'Changing ROOT passwd was done! at {formatted_time}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChangeRootPasswd_err}')
        print(f'\n')
        print(Fore.RED + f'Changing ROOT passwd failed :( at {formatted_time}')
        print(f'\n')
        print(f'\n')
    