#!/bin/bash
fileCompile='./client.py';
build='./build';
spec='./client.spec';

python -m pyinstaller ${fileCompile} --onefile --noconsole;

if [[ ${?} -eq 0 ]];
then
    echo "${fileCompile} has been compiled to .exe :D";
    rm -rf $build;
    rm -rf $spec;
    echo "Find .exe in ./dist :D";
    exit 0;
else
    echo "Failed to compile ${fileCompile} to .exe :(";
    echo "Exiting with 1";
    exit 1;
fi