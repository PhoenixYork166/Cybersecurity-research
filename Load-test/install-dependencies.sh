#!/bin/bash

# Use Git Bash

modules=('locust')

# Windows
echo "Doing Windows";
for each in "${modules[@]}";
do
    python -m pip install $each --user IGS;
    eachVersion=$(python -m $each --version);

    if [[ $? -eq 0 ]];
    then
        echo "";
        echo "Succeeded in installing $each :D";
        echo "";
        echo "$each of version: ";
        echo "$eachVersion installed :D";
        echo "";
    else
        echo "";
        echo "Failed to install $each :(";
    fi
done

# Linux
echo "Doing Linux";
for each in "${modules[@]}";
do
    pip install $each;
    $each --version;

    if [[ $? -eq 0 ]];
    then
        echo "";
        echo "Succeeded in installing $each :D";
        echo "";
        echo "$each of version: ";
        echo "$eachVersion installed :D";
        echo "";
    else
        echo "";
        echo "Failed to install $each :(";
    fi
done