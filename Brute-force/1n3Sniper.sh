#!/bin/bash

# Normal Mode
# sniper -t <TARGET>

# Stealth mode + OSINT + RECON
# sniper -t <TARGET> -m stealth -o -re

# Discover mode
# sniper -t <CIDR> -m discover -w <WORKSPACE_ALIAS>

# Full Port Scan mode
# sniper -t <TARGET> -fp

# ENABLE Bruteforce mode
# sniper -t <TARGET> -b

# Airstrike mode
# sniper -f targets.txt -m airstrike

# Nuke mode with target list, Bruteforce enabled
# sniper -f targets.txt -m nuke -w <WORKSPACE_ALIAS>
if [[ ${UID} -eq 0 ]];
then
    echo "OK, confirm your are ROOT! :D";
    echo "Proceeding 1N3/Sn1per with DoS Nuke Mode :D";
    targets='./targets.txt';
    sniper -f $targets -m nuke -w nukedTown;
    if [[ ${?} -eq 0 ]];
    then
        echo "Congrats!! I believe you brought havoc to your target :D";
        echo "Exiting with 0";
        exit 0;
    else
        echo "Ummm...You might need to fine tune HTTP response from your targets :(";
        echo "Exiting with 1";
        exit 1;
    fi
else
    echo "You aren't ROOT!";
    echo "Exiting with 1";
    exit 1;
fi