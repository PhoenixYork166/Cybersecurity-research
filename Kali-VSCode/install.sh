#!/bin/bash

# chmod 777
chmod 777 ./*.deb;

# Install VScode
sudo dpkg -i code_1.73.0-1667318785_amd64.deb;

if [[ $? -eq 0 ]];
then
    echo "";
    echo "Succeeded in install VScode :D";
    echo "";
    echo "code to start vscode :D";
    echo "";
else
    echo "";
    echo "Failed to install VScode";
    exit 1;
fi

exit 0;