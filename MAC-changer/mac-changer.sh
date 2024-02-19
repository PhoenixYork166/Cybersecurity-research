#!/bin/bash

if [[ ${UID} -ne 0 ]];
then
    echo "You aren't ROOT";
    echo "Exiting...";
    exit 1;
fi

eth0_down=$(sudo ifconfig eth0 down);
read -p "Enter NIC to change [eth0]: " NIC;
read -p "Enter new MAC addr: [00:5c:56:aa:bb:cc]: " newMAC;
change_MAC=$(sudo ifconfig $NIC hw ether $newMAC);

if [[ ${?} -eq 0 ]];
then
    echo "MAC changed to ${newMAC}!";
    echo "";
    echo "Current ${NIC} config: ";
    sudo ifconfig ${NIC};
    echo "";
else
    echo "";
    echo "Failed to change NIC: ${NIC} to new MAC: ${newMAC}";
    echo "";
fi

echo "ifconifg ${NIC} up";
eth0_up=$(sudo ifconfig ${NIC} up);
if [[ ${?} -eq 0 ]];
then
    echo "";
    echo "${NIC} is now up :D";
else
    echo "";
    echo "Failed to bring up ${NIC} ;(";   
    echo "";
fi

echo "Restarting network.service";
restartNetwork=$(sudo /etc/init.d/networking restart);
if [[ ${?} -eq 0 ]];
then
    echo "";
    echo "Succeeded in restarting network.service :D";
else
    echo "";
    echo "Failed to restart network.service ;(";   
    echo "";
    exit 1;
fi

echo "Exiting with 0";
exit 0;