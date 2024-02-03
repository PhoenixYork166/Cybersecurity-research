#!/bin/bash

if [[ ${UID} -eq 0 ]];
then
    echo "Installing dependencies...";
    apt install tmux hydra hping3 -y;
    exit 0;
else
    echo "Failed to install dependencies...";
    echo "You aren't ROOT...";
    exit 1;
fi