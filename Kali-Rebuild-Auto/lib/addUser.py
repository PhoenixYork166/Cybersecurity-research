# Import these for every module component
# --------------
# Imports modules
# --------------
from . import Fore, sys, os, Back, Style, getpass, subprocess, re

def addUser(user, sudo_password, newUser, newPassword, formatted_time):
    
    # Adding a new privileged user
    addPrivUser = f'echo {sudo_password} | sudo adduser {newUser}'
    doAddPrivUser = subprocess.Popen(addPrivUser, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doAddPrivUser_out, doAddPrivUser_err = doAddPrivUser.communicate()
        
    if doAddPrivUser.returncode == 0:
        
        #print(f'{doAddPrivUser_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in add new Priviledged User at {formatted_time}:D')            
        print(f'{doAddPrivUser_out}')
        print(f'\n')
                
        # Changing current password for {newUser} so that he/she can login
        changePassword = f'echo "{newUser}:{newPassword}" | chpasswd'
        doChangePassword = subprocess.Popen(changePassword, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        doChangePassword_out, doChangePassword_err = doChangePassword.communicate()
        
        if doChangePassword.returncode == 0:
            
            print(Fore.WHITE + f'{doChangePassword_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in creating the password: {newPassword} for {newUser}\nat {formatted_time}')
            print(f'\n')
            print(f'\n')
            
            # Adding 'user' to usermod -aG
            usermod = f'echo {sudo_password} | sudo usermod -aG sudo {newUser}'
            doUsermod = subprocess.Popen(usermod, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            doUsermod_out, doUsermod_err = doUsermod.communicate()
            
            if doUsermod.returncode == 0:
                
                print(Fore.WHITE + f'{doUsermod_out}')
                print(f'\n')
                print(Fore.YELLOW + f'Succeeed in adding {newUser} to sudoers group :D\nOperation was done at {formatted_time}')
                print(f'\n')
                print(f'\n')
                
                # Allowing 'user' to Popen Bash
                print(f'\n')
                print(Fore.YELLOW + f'Adding this new privileged user: {newUser} to Bash group at {formatted_time}')
                print(f'\n')
                print(f'\n')
                #addBash = os.system("sudo chsh -s /bin/bash " + user)
                addBash = f'echo {sudo_password} | sudo chsh -s /bin/bash {newUser}'
                doAddBash = subprocess.Popen(addBash, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                doAddBash_out, doAddBash_err = doAddBash.communicate()
                
                if doAddBash.returncode == 0:
                    
                    print(Fore.WHITE + f'{doAddBash_out}')
                    print(f'\n')
                    print(Fore.YELLOW + f'Succeeded in adding {newUser} to Bash group\n\n')
                    # Adding 'user' to /ect/sudoers config
                    sudoers = f'/etc/sudoers'
                    addSudoer = f'echo {sudo_password} | sudo printf "{newUser}\tALL=(ALL)\tALL\n" >> {sudoers}'
                    doAddSudoer = subprocess.Popen(addSudoer, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    doAddSudoer_out, doAddSudoer_err = doAddSudoer.communicate()
                    
                    if doAddSudoer.returncode == 0:
                        
                        print(f'\n')
                        print(Fore.WHITE + f'{doAddSudoer_out}')
                        print(f'\n')
                        print(Fore.YELLOW + f'Succeeded in adding {newUser} to /etc/sudoer config at {formatted_time}')                        
                        print(f'\n')
                        print(f'\n')
                        
                    else:
                        
                        print(f'\n')
                        print(Fore.WHITE + f'{doAddSudoer_err}')
                        print(f'\n')
                        print(Fore.RED + f'Failed to add {newUser} to /etc/sudoers config at {formatted_time}')
                        print(f'\n')
                        print(f'\n')
                        
                else:
                    
                    print(f'\n')
                    print(Fore.WHITE + f'{doAddBash_err}')
                    print(f'\n')
                    print(Fore.RED + f'Failed to add {newUser} to Bash group at {formatted_time}')
            
            else:
                
                print(f'\n')
                print(Fore.WHITE + f'{doUsermod_err}')
                print(f'\n')
                print(Fore.RED + f'Failed to add {newUser} to sudoers group at {formatted_time}')
        
        else:
            
            print(f'\n')
            print(Fore.WHITE + f'{doChangePassword_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to create the password for {newUser} at {formatted_time}')
    
    else:
        
        print(f'\n')
        print(f'{doAddPrivUser_err}')
        print(f'\n')
        print(f'\n')

        


    

    
