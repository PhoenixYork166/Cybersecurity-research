#!/bin/bash
modules=(
    'bs4'
    'all_packages'
    'colorama'
    'docopt'
    'freeze'
    'numpy'
    'pandas'
    'pytest'
    'pytest-cov'
    'selenium'
    'retry'
    'metplotlib'
    'scikit-learn'
    'jedi'
    'scipy'
    'scapy'
    'idlex'
    'ipcalc'
)

for module in ${modules[@]};
    do
        echo "Installing Python module: ${module}";
        installMod=$(python -m pip install ${module} --user IGS);
        if [[ ${?} -eq 0 ]];
        then
            echo "======================================";
            echo "";
            echo "Succeeded in installing Python3-${module}";
            echo "";
            echo "======================================";

        else
            echo "======================================";
            echo "";
            echo "Failed to install ${module}";
            echo "";
            echo "======================================";
        fi
    done
