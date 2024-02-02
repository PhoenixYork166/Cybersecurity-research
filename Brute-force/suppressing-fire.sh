#!/bin/bash

script='hydra-hardcode.sh';

# Trial & Error tested
# maximum of 100 sessions can be handled by a 16 CPU + 16GB RAM VM
sessions=100;

for ((i=0; i<$sessions; i++));
do
    tmux new-session -d -s "session${i}" "bash ${script}";
done