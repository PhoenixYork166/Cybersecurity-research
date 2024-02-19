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
    'requests'
    'psutil'
    'metplotlib'
    'scikit-learn'
    'jedi'
    'scipy'
    'scapy'
    'idlex'
    'ipcalc'
    'auto-py-to-exe'
)

# Install Python3 package manager pip
apt install -y pip;
OS_ID=$(cat /etc/os-release | egrep '^\s*ID\s*=(.*)$');

for module in ${modules[@]};
    do
        echo "Installing Windows Python module: ${module}";
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

        # Debian
        echo "Installing Kali Linux Python module: ${module}";
        installLinuxMod=$(pip install ${module});
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

        # CentOS 9
        echo "Installing CentOS stream 9 Linux Python module: ${module}";
        installLinuxMod=$(yum install -y python3-${module});
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
