#!/bin/bash

sysctl='/etc/sysctl.conf';
# This allows your Kali to route all intercepted packets
# back to your targets
# To avoid Victims' network connectivity issues
printf "net.ipv4.ip_forward=1" >> $sysctl;

# Activate sysctl changes w/o rebooting
sudo sysctl -p;
if [[ $? -ne 0 ]];
then
    echo "";
    echo "Failed sysctl -p";
    exit 1;
else
    echo "";
    echo "Done :D";
    exit 0;
fi