# Imports modules
# --------------
from . import Fore, sys, os, Back, Style, getpass, subprocess, re

def updatePostgres(user, sudo_password, formatted_time):

    print(Fore.YELLOW + "\nUpdating PosgreSQL 15 port from port 5433 to port 5432...\n")
        
    updatePostgres15 = f'echo {sudo_password} | sudo sed -i \'s/port \= 5433/port \= 5432/g\' /etc/postgresql/15/main/postgresql.conf'
    doUpdatePostgres15 = subprocess.Popen(updatePostgres15, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doUpdatePostgres15_out, doUpdatePostgres15_err = doUpdatePostgres15.communicate()

    if doUpdatePostgres15.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doUpdatePostgres15_out}')
        print(f'\n')
        print(Fore.YELLOW + "Updating PosgreSQL 15 port from port 5433 to port 5432\nhas succeeded!")
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doUpdatePostgres15_err}')
        print(f'\n')
        print(Fore.RED + "Updating PosgreSQL 15 port from port 5433 to port 5432\nhas failed... :(")
        print(f'\n')
        print(f'\n')

    print(Fore.WHITE+ "Updating PosgreSQL 14 port from port 5432 to port 5433")

    # Changing port 5432 => 5433 for PostgreSQL14 to allow update
    #os.system('sudo sed -i \'s/port \= 5432/port \= 5433/g\' /etc/postgresql/15/main/postgresql.conf')
    updatePostgres14 = f'echo {sudo_password} | sudo sed -i \'s/port \= 5432/port \= 5433/g\' /etc/postgresql/14/main/postgresql.conf'
    doUpdatePostgres14 = subprocess.Popen(updatePostgres14, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doUpdatePostgres14_out, doUpdatePostgres14_err = doUpdatePostgres14.communicate()

    if doUpdatePostgres14.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doUpdatePostgres14_out}')
        print(f'\n')
        print(Fore.YELLOW + "\nUpdating PosgreSQL 14 port from port 5432 to port 5433 has succeeded!")
        print(f'\n')
        print(f'\n')
                
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doUpdatePostgres14_err}')
        print(Fore.RED + "\nFailed to update PostgreSQL 14 port no. :(")
        print(f'\n')
        print(f'\n')

    # Restart PostgreSQL service
    print(f'\n')
    print(Fore.YELLOW + "Restarting PostgreSQL service...")
    print(f'\n')
    restartPostgres = f'echo {sudo_password} | sudo systemctl restart postgresql'
    doRestartPostgres = subprocess.Popen(restartPostgres, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doRestartPostgres_out, doRestartPostgres_err = doRestartPostgres.communicate()

    if doRestartPostgres.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doRestartPostgres_out}')
        print(f'\n')
        print(Fore.YELLOW + "Restarting PostgreSQL service has succeeded!")
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doRestartPostgres_err}')
        print(f'\n')
        print(f'\n')
        print(Fore.RED + "Restarting PostgreSQL service has failed...:(")
        print(f'\n')
        print(f'\n')
    
    
