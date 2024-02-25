#!/bin/bash

# Ensure script runner = ROOT
rootID='0';

if [[ ${UID} -eq ${rootID} ]];
then 
    # If user's UID='0' = ROOT => Continue

    # # Ask whether add a new NIC
    # read -p "Do you wanna configure a new NIC? [Y/N]" newNIC;
    # if [[ ${newNIC} -eq 'Y' ]] || [[ ${newNIC} -eq 'y' ]];
    # then 
    #     echo "Alright! Adding a new NIC for you!";
    #     read -p "Enter NIC name for NAT: [ens33]" nicName;
    #     read -p "Confirm NIC name for NAT: [ens33]" confirmNicName;
    #     if [[ ${nicName} -eq ${confirmNicName} ]];
    #     then
    #         echo "Proceeding...";
    #         read -p "Enter ${nicName}'s IP [192.168.0.18]: " nicIP;
    #         read -p "Enter ${nicName}'s netmask: [255.255.255.0]" nicNetmask;
    #         read -p "Enter ${nicName}'s gateway: [192.168.0.1]" nicGateway;
    #         read -p "Enter ${nicName}'s network address: [192.168.0.0]" nicNetwork;
    #     else
    #         echo "NAT nic name ${nicName} does NOT MATCH ${confirmNicName}";
    #         echo "Please re-enter NAT nic name...";
    #         read -p "Enter NIC name for NAT: [ens33]" nicName;
    #         read -p "Confirm NIC name for NAT: [ens33]" confirmNicName;
    #     fi
        
    #     # Adding NAT NIC
    #     networkConfig='/etc/network/interfaces'
    #     printf "auto ${nicName}\niface ${nicName} inet static\naddress ${nicIP}\nnetmask ${nicNetmask}\ngateway ${nicGateway}\nup route add -net ${nicNetwork} netmask ${nicNetmask} gw ${nicGateway}" >> ${networkConfig};
        
    #     if [[ ${?} -eq 0 ]]
    #     then
    #         echo "Successfully added new NIC into ${networkConfig}";
    #         echo "Restarting networking services";
    #         # Stop networking service
    #         systemctl stop networking;
    #         if [[ ${?} -eq 0 ]]
    #         then
    #             echo "Succeeded in stopping networking service";
    #             echo "Starting networking service again...";
    #             systemctl start networking;
    #             if [[ ${?} -eq 0 ]]
    #             then
    #                 echo "Succeeded in starting networking service";
    #                 echo "Succeeded in adding ${nicName}";
    #             else
    #                 echo "Failed to start networking service...";
    #             fi

    #         else
    #             echo "Failed to stop networking service...";
    #             echo "Skipping networking service restart...";
    #         fi

    #     else
    #         echo "Failed to add new NIC into ${networkConfig}...";
    #     fi

    # else
    #     echo "NOT gonna add a new NIC :)";
    #     echo "Skipping...";
    # fi

    # Checking internet access
    checkInternet=$(ping -c 2 1.1.1.1);
    if [[ ${checkInternet} -eq 0 ]];
    then
        echo "Confirm internet connectivity :D";
        echo "Proceeding!!!!";
    else
        echo "Cannot confirm internet connectivity :(";
        echo "Will attempt customization, but likely to fail...";
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

    # Create /home/root/Downloads
    mkdir /home/${user}/Downloads;
    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in creating /home/${user}/Downloads";
    else
        echo "Failed to create /home/${user}/Downloads";
    fi

    echo "======== START - Debian background theme============";
    # Update Debian login page to a less scary image
    # Download Anonymous .jpg
    findImage=$(find /home/${user}/Downloads | grep 'anonymous');

    if [[ ${?} -ne 0 ]];
    then
        echo "========================";
        echo "========================";
        echo "Cannot find Image, downloading...";
        echo "";
        anonymousImage='https://media.wnyc.org/i/800/0/l/85/1/we-are-anonymous.jpg'
        cd /home/${user}/Downloads && wget ${anonymousImage};
        if [[ ${?} -eq 0 ]];
        then
            anonymousImagePath="/home/${user}/Downloads/we-are-anonymous.jpg";
            echo "Succeeded in downloading Anonymous Image :D";
            echo "Proceeding to change Debian profile :D";
            imagePath='/usr/share/backgrounds/';
            # Change Debian profile image
            cp $findImage $imagePath;
            if [[ ${?} -eq 0 ]];
            then
                echo "Succeeded in adding a lock screen Image :D";
                echo "Removing existing Kali Linux lock screen images";
                lockScreen='/usr/share/backgrounds/';
                #rm -rf $lockScreengnome
                rm -rf $lockScreenkali
                rm -rf $lockScreenkali*
            else
                echo "Failed to copy new image to lock screen image :(";
            fi
        else
            echo "Failed to download Image";
            echo "Skipping...";
            echo "========================";
            echo "========================";
        fi

    else
        echo "Not downloading Anonymous Image :(";
    fi
    echo "======== END - Debian background theme============";

    # Update expired Kali Linux keys on a Debian12 base-build image
    echo "============= Adding expired Kali Linux keys on this Debian Linux plain build =================";
    
    # Updating expired Kali Linux keys
    addKey=$(wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-keyring.asc);
    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in updating Kali Linux keys!";
        echo "======================================";
    else
        echo "Failed to update Kali Linux keys...";
        echo "======================================";
    fi

    # Backup existing Debian repository
    aptPath='/etc/apt/sources.list';
    aptBackup='/etc/apt/sources-backup.list';
    
    # Echo output of existing Apt Repository
    echo "Current Debian Apt Repository: ";
    echo "=================================";
    cat ${aptPath};
    echo "=================================";
    echo "Backup existing Apt repository before making it to Kali repo...";
    cp ${aptPath} ${aptBackup};
    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in backing up existing Apt repo";
        echo "Proceeding to change Apt repo to Kali repo!";
        echo "";
        echo "";
        #printf "deb https://deb.debian.org/debian bookworm main non-free-firmware\ndeb-src http://deb.debian.org/debian bookworm main non-free-firmware\n\ndeb https://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src https://http.kali.org/kali kali-rolling main non-free contrib" > ${aptPath};
        printf "deb https://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src https://http.kali.org/kali kali-rolling main non-free contrib" > ${aptPath};
        if [[ ${?} -eq 0 ]];
        then
            echo "";
            echo "Succeeded in customizing this Debian repo to Kali repo!";
            echo "Proceeding to apt update && apt upgrade!";
            echo "";

            # After changing Debian repository to Kali repository
            # 1st time apt update && apt upgrade
            apt-get update && apt-get -y upgrade;
            if [[ ${?} -eq 0 ]] || [[ ${?} -eq 100 ]];
            then
                # If SUCCEEDED apt update & apt upgrade 
                # APT Repository already becomes Kali!!
                echo "Succeeded in APT update => upgrade!:D";
                # Proceed apt autoremove to remove obsolete apt resources
                echo "1st time Cleaning up APT!";
                apt autoremove -y;
                if [[ ${?} -eq 0 ]];
                then
                    echo "Succeeded in 1st time cleaning up APT trash :D";
                    echo "Proceeding to 2nd time apt-get update && apt-get -y upgrade; the 2nd time";
                    echo "======================================";
                    echo "======================================";
                else
                    echo "Failed to 1st time clean up ATPT trash :(";
                    echo "No worries, let's try to do APT update => upgrade again";
                    echo "======================================";
                    echo "======================================";
                    echo "";
                fi

                # 2nd time apt update && apt -y upgrade
                apt-get update && apt-get -y upgrade;
                if [[ ${?} -eq 0 ]];
                then
                    echo "Succeeded in 2nd time apt-get update && apt-get -y upgrade";
                    echo "Proceeding 2nd time apt autoremove...";
                    echo "======================================";
                    echo "======================================";
                    echo "";
                    apt autoremove -y;

                    if [[ ${?} -eq 0 ]];
                    then
                        echo "Succeeded in 2nd time APT clean up :D";
                        echo "";
                        echo "======================================";
                        echo "======================================";
                    else
                        echo "Failed to 2nd time clean up APT trashes";
                        echo "You may manually APT clean up!";
                        echo "";
                        echo "======================================";
                        echo "======================================";
                        echo "";
                    fi
                else
                    echo "Failed 2nd time to apt-get update && apt-get -y upgrade";
                    echo "No worries :) We'll try to breakthrough though :D";
                    echo "";
                    echo "======================================";
                    echo "======================================";
                    echo "";
                fi
            else
                echo "Failed to upgrade to Kali linux :(";
            fi

            # 1st time apt update && apt -y upgrade 
            if [[ ${?} -eq 0 ]];
            then
                echo "Congrats! Your Debian has now become a Kali Linux :D!";
                echo "Please reboot this Debian linux first";
                echo "";
                echo "Before running the Tools installation script";
                echo "";

                echo "Changing Kernel settings to disable Restart pop-ip in /etc/needrestart/needrestart.conf";
                echo "To avoid Daemons Restart pop-up during Open-source attack tools installation";
                restartConf='/etc/needrestart/needrestart.conf';
                existingRestart=$(grep '$nrconf{restart}' ${restartConf});
                targetRestart="\$nrconf{restart} = 'a'";
                sed -i "s/$existingRestart/$targetRestart/g" $restartConf;
                if [[ ${?} -eq 0 ]];
                then
                    echo "Succeeded in disabling Daemon pop-up before Tools installation";
                    echo "Please reboot before running this script to install tools :D!!";
                    echo "DONE DONE DONE DONE DONE DONE DONE";
                else
                    echo "Failed to disable Daemon pop-up";
                    echo "Daemon alert may come up during Tools installation";
                fi

            else
                echo "We feel sorry that your Debian did NOT become a Kali Linux :(";
                # Terminate Customization here if failed to become a Kali linux
            fi

        else
            echo "Failed to customize this Debian repo to Kali repo...";
        fi

    else
        echo "Failed to back up existing Apt repo";
        echo "Skipping Debian customization...";
    fi
else
    echo "You aren't ROOT";
fi