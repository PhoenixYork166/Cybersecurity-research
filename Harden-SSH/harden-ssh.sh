#!/bin/bash

#if [[ ${UID} -ne 0 ]];
#then
#    echo "You aren't ROOT";
#    echo "Exiting...";
#    exit 1;
#else
#    echo "You are ROOT";
#    echo "Proceeding...";
#fi

#sshd_config='/etc/ssh/sshd_config';
sshd_config='./sshd_config';

# Adding my custom SSH rules
printf "\nPort 2222\nStrictModes yes\nMaxAuthTries 1\nMaxSessions 2\n\nAllowAgentForwarding yes\nAllowTcpForwarding yes\nGatewayPorts yes\nX11Forwarding yes\n\n" >> $sshd_config;

# Restart SSH
restart_ssh=$(systemctl restart ssh);

if [[ $? -eq 0 ]];
then
    echo "Succeeded in restarting SSH :D";
else
    echo "Failed to restart SSH :(";
fi

exit 0;