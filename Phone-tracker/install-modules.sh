#!/bin/bash
modules=(
    'phonenumbers'
    'timezonefinder'
    'h3'
    'numpy'
    'geopy'
    'geographiclib'
    'pytz'
)


# Windows
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
    

# Linux
for module in ${modules[@]};
    do
        echo "Installing Python module: ${module}";
        installMod=$(sudo pip install ${module} --user root);
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
exit 0;
