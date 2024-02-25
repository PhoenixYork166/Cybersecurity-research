# Usage
# 1. Upgrade Kali Repo
# bash upgrade.sh
##
# 2. Install Attack Tools
# bash install-tools.sh
##
# 3. Configure Tools
# bash configure.sh
##
# 4. Install Python3 dependencies
# bash install-pymodules.sh
##
## This repo is a dedication to my cybersecurity mentor: Jimmy gor🙇🏻‍♀️ 
##
## Much appreciated your education for Orchestration, advanced Network defenses, Infrastructure Security and Regular Expression🙇🏻‍♀️
## No Jimmy, no me🙇🏻‍♀️
##
## This repo helps you unleash Kali Linux & install tools much faster via Python automation
## right after you configured a NIC for internet connection :D
##
## Usage
## git clone https://github.com/phoenixyork166/Kali-Rebuild-Auto.git
## 
## cd ./Kali-Rebuild-Auto && sudo python3 ./main.py
## If you Kali Linux doesn't support this main.py, 
## Run the Shell Scripts instead
## bash./Kali-Rebuild-Auto/upgrade.sh;
## bash ./Kali-Rebuild-Auto/install-tools.sh;
# Cybersecurity Red teaming with Kali Linux
![Kali Linux](https://i.ytimg.com/vi/0LajChcEkP0/maxresdefault.jpg)
##
# Penetration Testing / Ethical Hacking
![Ethical Hacking](https://media.licdn.com/dms/image/D4D12AQHZBU6pxH7LZQ/article-cover_image-shrink_600_2000/0/1686636471875?e=2147483647&v=beta&t=-UIGq76Snqp-gB_bUmLfSnFo6KFYE2r7VUT5iIY4BYg)
##
# Kali Linux new build script
![Debian Linux](https://i.ytimg.com/vi/Y4umB6KqB4g/maxresdefault.jpg)
## Hi this script will do following tasks for you
##
## 1. Add a new priviledged user => Install open-source tools later on
## Enter new priviledged username 
## Confirm new priviledge user password
## Avoid using Kali root
## Add this priviledged user to /etc/sudoers
## Allow this priviledged user to run Bash
## new priviledged user=(ALL) ALL

## 2. Update PostgreSQL14, 15 Port values
### i. Changing port 5433 => 5432 for PostgreSQL15 to allow 'gvm-setup' during OpenVAS installation
### ii. Changing port 5432 => 5433 for PostgreSQL14 to allow 'gvm-setup' during OpenVAS installation

## 3. Update && Upgrade Kali's repository
## This is the most troublesome step when setting up a new Kali Linux...
### i. Add Kali archive keys
### ii. Update apt-key directory
### iii. Updating Kali's repo from HTTP to HTTPS to allow smooth apt update && apt upgrade -yuf; lateron
### deb https://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list
### deb-src https://http.kali.org/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list

## 4. Install a ton of open-source tools
## Create a tool directory for new priviledged user
## [Will not install these tools if choose not to create a new priviledged user]
## Install popular package managers (RPM, SNAP, NixNote2, Nautilus-dropbox, Keepassxc, Python3 PIP, DNF, GEM)
## 1N3/Sn1per
## PyAutoGUI
## Sherlock
## RedHawk
## Hping3
## Apache2
## SecList from https://github.com/danielmiessler/SecLists.git
## Visual Studio Code
## Guake - Drop Down Terminal (F12)
## Terminal Multiplexer - TMUX 
## NFS (Net File Share)
## XSSER
## EyeWitness
## Evil Win-RM
## PowerLine
## Remote System Logging (rsyslog)
## Linux Containers - lxc & lxd
## Docker
## BeefProject (via Apt) 
