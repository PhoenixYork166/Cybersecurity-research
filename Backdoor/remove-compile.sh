#!/bin/bash

filesRemove=('./build' './dist' './reverse_shell.spec')

for file in ${filesRemove[@]}
do
    rm -rf ${file};
    if [[ $? -eq 0 ]];
    then
        echo "$file has been purged :D";
    else
        echo "Failed to purge $file";
    fi
done 