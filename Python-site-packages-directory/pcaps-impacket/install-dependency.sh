#!/bin/bash

if [[ $UID -ne 0 ]];
then
    echo "You aren't ROOT";
    exit 1;
else
    echo "You are ROOT";
    echo "Proceeding...";
    echo "";
fi

sudo wget https://bootstrap.pypa.io/pip/2.7/get-pip.py;

if [[ $? -eq 0 ]];
then
    echo "Succeeded in downloading get-pip.py for pip2.7";
    echo "Proceeding to install pip2.7";
else
    echo "Failed to download get-pip.py for pip2.7";
    echo "";
fi

sudo chmod 777 ./get-pip.py;
sudo python2.7 get-pip.py;

testPIP2_7=$(pip2.7);

if [[ $? -eq 0 ]];
then
    echo "Succeeded in install pip2.7 :D";
    echo "Proceeding to pip2.7 install pcapy six";
    echo "";
    pip2.7 install pcapy;
    pip2.7 install six;

else
    echo "Failed to install pip2.7 :(";
fi

echo "";
echo "Downloading python2.7 impacket module from github...";

sudo git clone https://github.com/CoreSecurity/impacket;
if [[ $? -eq 0 ]];
then
    echo "Succeeded in downloading impacket module from github";
    echo "Proceeding to install impacket module for python2.7";
    echo "";
    sudo python2.7 ./impacket/setup.py install;
else
    echo "Failed to download impacket module from github..";
    echo "Exiting...";
    exit 1;
fi



