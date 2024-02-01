#!/bin/bash
fileCompile='./reverse_shell.py';
python -m pyinstaller ${fileCompile};

if [[ ${?} -eq 0 ]];
then
    echo "${fileCompile} has been compiled to .exe :D";
    exit 0;
else
    echo "Failed to compile ${fileCompile} to .exe :(";
    echo "Exiting with 1";
    exit 1;
fi