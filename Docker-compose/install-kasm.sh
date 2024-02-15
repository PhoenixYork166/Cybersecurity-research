#!/bin/bash

if [[ ${UID} -eq 0 ]];
then
    echo "Confirmed you're root, proceeding...";
    # Create .swap partition for Kasm
    sudo dd if =/dev/zero bs=1M count=1024 of=/mnt/1GiB.swap

    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in creating .swap partition for Kasm :D";
        echo "chmod 600 /mnt/1GiB.swap";

        sudo chmod 600 /mnt/1GiB.swap;
        if [[ ${?} -eq 0 ]];
        then
            echo "Succeeded in chmod 600 /mnt/1GiB.swap";
            echo "Make it into swap\nmkswap /mnt/1GiB.swap";
            sudo mkswap /mnt/1GiB.swap;
            if [[ ${?} -eq 0 ]];
            then
                echo "Done mkswap /mnt/1GiB.swap";
                echo "Turning on the swap...";
                sudo swapon /mnt/1GiB.swap;
                if [[ ${?} -eq 0 ]];
                then
                    echo "Succeeded in turning on the Swap";
                    echo "Making sure swap comes back after reboot...";
                    echo '/mnt/1GiB.swap swap swap defaults 0 0' | sudo tee -a /etc/fstab;
                    if [[ ${?} -eq 0 ]];
                    then
                        echo "Alright, this swap comes back after reboot :)";
                        echo "Downloading Kasm...";
                        sudo wget https://kasm-static-content.s3.amazonaws.com/kasm_release_1.10.0.238225.tar.gz;
                        if [[ ${?} -eq 0 ]];
                        then
                            echo "Succeeded in downloading Kasm :D";
                            echo "Proceeding to untar Kasm...";
                            echo "chmod 777 ./kasm_release_1.10.0.238225.tar.gz";
                            sudo chmod 777 ./kasm_release_1.10.0.238225.tar.gz;
                            sudo tar -zxvf ./kasm_release_1.10.0.238225.tar.gz;
                            echo "chmod 777 ./kasm_release";
                            sudo chmod 777 ./kasm_release;
                            
                            echo "Downloading Docker Compose as a dependency of Kasm...";
                            sudo curl -L "https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose;
                            echo "chmod +x /usr/local/bin/docker-compose";
                            chmod +x /usr/local/bin/docker-compose;
                            echo "Current docker-compose version: ";
                            docker-compose --version;
                                                        
                            if [[ ${?} -eq 0 ]];
                            then
                                echo "Succeeded in installing docker-compose :D";
                                echo "Installing Kasm...";
                                cd ./kasm_release && chmod 777 ./*.* && bash ./install.sh;
                                
                            else
                                echo "Failed to install docker-compose :(";
                                echo "Please manually apt update && apt -y upgrade...";
                                echo "Exiting...";
                                exit 1;
                            fi
                    else
                        echo "Failed to making swap into fstab..."
                        exit 1;
                    fi

                else
                    echo "Failed to turn on the Swap";
                    echo "Exiting...";
                fi

            else
                echo "Failed to mkswap /mnt/1GiB.swap";
                echo "Exiting...";
                exit 1;
            fi


        else
            echo "Failed to chmod 600 /mnt/1GiB.swap";
            echo "Exiting...";
            exit 1;
        fi

    else
        echo "Failed to create .swap partition for Kasm";
        echo "Exiting...";
        exit 1;
    fi

else
    echo "You aren't ROOT";
    echo "Exiting...";
    exit 1;
fi
