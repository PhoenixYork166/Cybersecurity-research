#!/bin/bash

script='hydra-hardcode.sh';
sessions=1000;

for ((i=0; i<$sessions; i++));
do
    tmux new-session -d -s "session${i}" "bash ${script}";
done