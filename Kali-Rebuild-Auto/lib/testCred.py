# Import these for every module component
# --------------
# Imports modules
# --------------
#from . import user, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re
# Import module specific variables
#from . import thisTime
#from . import newUser, newPassword
import time

def testCred(user, sudo_password):
    
    print(f'\n')
    print(f'user: {user}')
    print(f'\n')
    print(f'sudo_password: {sudo_password}')
    print(f'\n')
    
# Get current local time as a struct time OBJ
# current_time = time.localtime()

# formatted_time = time.strftime('%Y-%m-%d-%H:%M:%S', current_time)

# print(f'Current time: {formatted_time}')