#!/bin/bash

# Ensure script runner = ROOT
rootID='0';

if [[ ${UID} -ne ${rootID} ]];
then
    echo "You aren't ROOT :(";
    exit 1;
else
    echo "You're ROOT, proceeding...";
fi

# Checking internet access
checkInternet=$(ping -c 2 1.1.1.1);
if [[ ${checkInternet} -eq 0 ]];
then
    echo "Confirm internet connectivity :D";
else
    echo "Cannot confirm internet connectivity :(";
    echo "Will attempt to install tools, but likely to fail...";
fi

# Create /home/root
user=$(whoami);
mkdir /home/${user};
mkdir /home/$user/Desktop;
mkdir /home/$user/Desktop/tools;

# Create /home/root/Downloads
mkdir /home/${user}/Downloads;
if [[ ${?} -eq 0 ]];
then
    echo "Succeeded in creating /home/${user}/Downloads";
else
    echo "Failed to create /home/${user}/Downloads";
fi

echo "Changing Kernel settings to disable Restart pop-ip in /etc/needrestart/needrestart.conf";
echo "To avoid Daemons Restart pop-up during Open-source attack tools installation";
restartConf='/etc/needrestart/needrestart.conf';
existingRestart=$(grep '$nrconf{restart}' ${restartConf});
targetRestart="\$nrconf{restart} = 'a'";
sed -i "s/$existingRestart/$targetRestart/g" $restartConf;

if [[ ${?} -eq 0 ]];
then
    echo "==============================";
    echo "Succeeded in disabling Daemon pop-up before Tools installation";
    echo "==============================";
else
    echo "Failed to disable Daemon pop-up";
    echo "";
    echo "Daemon alert may come up during Tools installation";
    echo "";
    echo "You may need to manually TAB => OK during installation...";
    echo "";
fi

echo "Continuing to Install Open-source hacking tools :D!";
echo "";
echo "======================================";
echo "";

# Start installing tones of customized hacking tools
## ifconfig must be added to sys variables
# net-tools (ifconfig)
##
# VIM Editor
# mac-robber
# SNAP
# Git
# Ettercap-graphical
# Hydra
# Cassandra
# Beef-XSS (Beef project)
# Metasploit dependencies
## 'tee' 'curl' 'ca-certificates' 'openssl' 'apt-transport-https' 'software-properties-common' 'lsb-release' 'postgresql'
#
## Import Metasploit APT Repository on Debian
# curl -fsSL https://apt.metasploit.com/metasploit-framework.gpg.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/metasploit.gpg > /dev/null
## Add Metasploit Repository
# echo "deb [signed-by=/usr/share/keyrings/metasploit.gpg] https://apt.metasploit.com/ buster main" | sudo tee /etc/apt/sources.list.d/metasploit.list
## Apt install Metasploit
# apt install metasploit-framework
## First-time setup
# msfconsole

tools=('net-tools'
        'tor'
        'proxychains'
        'python3-pip'
        'guake'
        'tmux'
        'tcpdump'
        'rsyslog'
        'kaboxer'
        'xdg-utils'
        'vim'
        'build-essential'
        'clang'
        'clang-14'
        'libgcc-s1'
        'libpython3.11'
        'libstdc++6'
        'libcap2'
        'libpcap0.8'
        'libnet1'
        'libseccomp2'
        'libwireshark17'
        'libwiretap-dev'
        'libwsutil-dev'
        'libwireshark-dev'
        'libreadline8'
        'libc6'
        'libusb-1.0-0'
        'libnetfilter-queue1'
        'afl++'
        'afl++-doc'
        'graphviz'
        'python3-pip'
        'aircrack-ng'
        'gawk'
        'iproute2'
        'iw'
        'pciutils'
        'xterm'
        'perl'
        'apktool'
        'kali-defaults'
        'python3-bluez'
        'python3-bs4'
        'python3-ctypescrypto'
        'python3-fleep'
        'python3-libarchive-c'
        'python3-netifaces'
        'python3-pil'
        'python3-prettytable'
        'python3-pycryptodome'
        'apple-bleee'
        'python3-dicttoxml'
        'python3-requests'
        'arjun'
        'openjdk-11-jre'
        'arping'
        'adduser'
        'useradd'
        'gawk'
        'init-system-helpers'
        'lsb-base'
        'arpwatch'
        'asleap'
        'assetfinder'         
        'nmap'
        'arp-scan'
        'autopsy'
        'curl'
        'lsof'
        'beef-xss'
        'hostapd-mana'
        'iproute2'
        'iw'
        'procps'
        'bettercap'
        'bettercap-caplets'
        'bettercap-ui'
        'golang-github-antchfx-htmlquery-dev'
        'golang-github-jawher-mow.cli-dev'
        'golang-github-saintfish-chardet-dev'
        'golang-google-appengine-dev'
        'golang-github-antchfx-xmlquery-dev'
        'golang-github-kennygrant-sanitize-dev'
        'golang-github-temoto-robotstxt-dev'
        'golang-github-gobwas-glob-dev'
        'golang-github-puerkitobio-goquery-dev'
        'golang-golang-x-net-dev'
        'golang-github-gocolly-colly-dev'
        'unicorn-magic'
        'bundler'
        'hping3'
        'httprobe'
        'httpx-toolkit'
        'smbclient'
        'ca-certificates'
        'snapd'
        'git'
        'unzip'
        'veil'
        'whatmask'
        'ruby-interpreter'
        'uby-addressable'
        'ruby-ipaddress'
        'whatweb'
        'whois'
        'screen'
        'wifi-honey'
        'cowpatty'
        'iptables'
        'netmask'
        'netsed'
        'debconf'
        'ettercap-graphical'
        'forensic-artifacts'
        'python3-artifacts'
        'rtpflood'
        'rainbowcrack'
        'vlan'
        'ncat'
        'commix'
        'bruteforce-luks'
        'bruteforce-salted-openssl'
        'bruteshark'
        'brutespray'
        'btscanner'
        'bulk-extractor'
        'bytecode-viewer'
        'cabextract'
        'cassandra'
        'cadaver'
        'caldera'
        'calico'
        'capstone'
        'ccrypt'
        'certgraph'
        'certipy-ad'
        'cewl'
        'changeme'
        'chaosreader'
        'cherrytree'
        'chirp'
        'chisel'
        'chkrootkit'
        'chntpw'
        'chromium'
        'cifs-utils'
        'cillium-cli'
        'cisco-audting-tool'
        'cisco-ocs'
        'cisco-torch'
        'cisco7crack'
        'clamav'
        'cloud-enum'
        'cloudbrute'
        'cmospwd'
        'cmseek'
        'cntlm'
        'code-oss'
        'colly'
        'command-not-found'
        'commix'
        'copy-router-config'
        'cosign'
        'covenant-kbx'
        'cowpatty'
        'make'
        'postgresql'
        'crack-common'
        'mac-robber' 
        'snapd' 
        'git' 
        'docker\.io'
        'lxc' 
        'bridge-utils'
        'beef-xss'
        'tee'
    );

    # Iterate through $tools[@] && Install each tool
    for tool in ${tools[@]};
    do
        echo "Installing tool: ${tool}";
        installTools=$(apt install ${tool} -y);
        if [[ ${?} -eq 0 ]];
        then
            echo "======================================";
            echo "";
            echo "";
            echo "Succeeded in installing ${tool}";
            echo "======================================";
            echo "======================================";
            echo "";

        else
            echo "======================================";
            echo "";
            echo "";
            echo "Failed to install ${tool}";
            echo "======================================";
            echo "======================================";
            echo "";
            echo "";
        fi
    done

    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in install Attack & Utility tools";
        echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";
        echo "This script has run successfully! :D";
        echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";
        echo "Please run bash ./configure.sh";
    else   
        echo "Failed to install tools...";
    fi



