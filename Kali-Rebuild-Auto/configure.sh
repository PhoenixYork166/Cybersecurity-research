#!/bin/bash

# Ensure script runner = ROOT
rootID='0';

if [[ ${UID} -eq ${rootID} ]];
then 
    # Checking internet access
    checkInternet=$(ping -c 2 1.1.1.1);
    if [[ ${checkInternet} -eq 0 ]];
    then
        echo "Confirm internet connectivity :D";
        echo "Proceeding!!!!";
    else
        echo "Cannot confirm internet connectivity :(";
        echo "Will attempt to install tools, but likely to fail...";
    fi

    # Create /home/root
    user=$(whoami);
    mkdir /home/${user};
    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in creating /home/${user}";
    else
        echo "Failed to create /home/${user}";
    fi

    # Create /home/root/Desktop
    mkdir /home/${user}/Desktop;
    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in creating /home/${user}/Desktop";
    else
        echo "Failed to create /home/${user}/Desktop";
    fi

    ls -la /home/${user}/Desktop;
    if [[ ${?} -eq 0 ]];
    then
        echo "/home/${user}/Desktop exists!!";
        echo "We'll store all config settings & login credentials here :D";
        desktop="/home/${user}/Desktop/";

    # Create /home/root/Downloads
    mkdir /home/${user}/Downloads;
    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in creating /home/${user}/Downloads";
    else
        echo "Failed to create /home/${user}/Downloads";
    fi

    echo "Proceeding to configure all installed tools";

    ## START - BeefXSS configurations
    echo "Configuring Beef-XSS for Cross-Site scripting attacks :D!";
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";
    echo "Remember to use proxychains when messing with XSS :D!";
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";

    startBeefXSS=$(systemctl start beef-xss);
    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in starting up Beef-XSS!";
        echo "Proceeding to configure Beef-XSS!";
        beefPath='/etc/beef-xss/config.yaml'
        read -p "[Beef-XSS] Enter new username: " newUser;
        read -p "[Beef-XSS] Enter new password: " newPassword;
        editBeefUsername=$(sed -i "s/newUser: beef/newUser: ${newUser}/g ${beefPath}")
        if [[ ${?} -eq 0]];
        then
            echo "Succeeded in changing login username for Beef-XSS! :D";
            echo "Proceeding to change login password for Beef-XSS :D";
            editBeefPassword=$(sed -i "s/passwd: beef/passwd: ${newPassword}/g ${beefPath}");
            if [[ ${?} -eq 0 ]];
            then
                echo "Succeeded in changing Beef-XSS login password :D";
                echo "Proceeding to save Beef-XSS to ${desktop}!!! :D";

                beefUser=$(egrep "\s+${newUser}\:\s+(.*)" ${beefPath});
                beefPasswd=$(egrep "\s+passwd\:\s+(.*)" ${beefPath});
                saveBeefCredentials=$(printf "${beefUser}\n${beefPasswd}\n" > ${desktop}BeefXSS-login.txt);
                if [[ ${?} -eq 0 ]];
                then
                    echo "Succeeded in saving the latest Beef-XSS login :D";
                    echo "Check it out at ${desktop}BeefXSS-login.txt :D";
                    echo "Proceeding to restart Beef-XSS services";
                    restartBeefXSS=$(systemctl restart beef-xss);
                    if [[ ${?} -eq 0 ]];
                    then
                        echo "Succeeded in restart Beef-XSS service :D";
                        echo "Beef-XSS is now accessible at http://127.0.0.1:3000/ui/authentication";

                else
                    echo "Failed to save the latest Beef-XSS login...";                    
                    echo "You may manually change it at ${beefPath} :(";
                fi


        else
            echo "Failed to change login username for Beef-XSS :(";
            echo "Skipping to configure Beef-XSS :(...";
        fi
    else 
        echo "Failed to start Beef-XSS...:(";
    fi
    ## END - BeefXSS configurations

    ## START - OpenVAS Installation & configurations 
    echo "Installing OpenVAS => config for Vulnerability Scanning :D";
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";
    echo "Remember to use proxychains when messing with OpenVAS :D!";
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";
    
    ## START - Configure PostgreSQL 15 && PostgreSQL 14 PORTs
    echo "Updating TCP/IP Ports for PostgreSQL 15 && PostgreSQL 14";
    echo "As a pre-requisite of OpenVAS";
    postgres15Path='/etc/postgresql/15/main/postgresql.conf';
    updatePostgres15=$(sed -i "s/port \= 5433/port \= 5432/g" ${postgres15Path});
    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in updating PostgreSQL 15 port from port 5433 to port 5432 :D";
    else
        echo "Failed to update PostgreSQL 15 port from port 5433 to port 5432 :(";
        echo "You may manually update it at ${postgres15Path}";
    fi

    postgres14Path='/etc/postgresql/14/main/postgresql.conf';
    updatePostgres14=$(sed -i "s/port \= 5432/port \= 5433/g" ${postgres14Path});
    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in updating PostgreSQL 14 port from port 5432 to port 5433 :D";
    else
        echo "Failed to update PostgreSQL 14 port from port 5432 to port 5433 :(";
        echo "You may manually update it at ${postgres14Path}";
    fi

    # Restart PostgreSQL services
    echo "No matter what, let's restart PostgreSQL services :D";
    restartPostgres=$(systemctl restart postgresql);
    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in restarting PostgreSQL services :D";
    else
        echo "Failed to restart PostgreSQL services :(";
        echo "Skipping...";
    fi
    ## END - Configure PostgreSQL 15 && PostgreSQL 14 PORTs

    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";
    echo "No matter what happened!";
    echo "Let's try to push through installation of OpenVAS :D!";
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";

    installOpenVAS=$(apt install openvas -y);
    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in installing OpenVAS :D";
        echo "Continuing to gvm-setup...";
        gvmSetup=$(gvm-setup);
        if [[ ${?} -eq 0 ]];
        then
            echo "Succeeded in setup of GVM";
        else
            echo "Failed to set up GVM :(";
            echo "Skipping...";
        fi
    else
        echo "Failed to install Open VAS :(";
        echo "Skipping...";
    fi
    ## END - OpenVAS Installation & configurations 
    echo "Succeeded in configuring Tools :D";

# If script runner is NOT ROOT
else
    echo "Sorry, you aren't ROOT :(";
fi