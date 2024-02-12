#!/bin/bash
fileCompile='./client.py';
build='./build';
spec='./client.spec';

echo "Removing existing ./dist/*.exe";
rm -rf ./dist;
rm -rf ./build;
rm -rf ./client.spec;

python -m pyinstaller ${fileCompile} --onefile --noconsole;

if [[ ${?} -eq 0 ]];
then
    echo "${fileCompile} has been compiled to .exe :D";
    echo "removing redundant files...";
    rm -rf $build;
    rm -rf $spec;
    exit 0;
else
    echo "Failed to compile ${fileCompile} to .exe :(";
    echo "Exiting with 1";
    exit 1;
fi