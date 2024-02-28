# --------------
# Imports modules
# --------------
from . import Fore, sys, os, Back, Style, getpass, subprocess, re

def installTools(user, sudo_password, formatted_time, newUser, newPassword):

    binary_path = f'/usr/bin/'
    # Default Tools
    print(Fore.YELLOW + "### Installing Default Tools ###")

    # Create directory 'tools'
    print(Fore.YELLOW + "***********************************")
    print(Fore.YELLOW + f'Creating /home/{user}/')
    print(Fore.YELLOW + "***********************************")
    createHome = f'echo {sudo_password} | sudo mkdir /home/{user}'
    doCreateHome = subprocess.Popen(createHome, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doCreateHome_out, doCreateHome_err = doCreateHome.communicate()
    
    if doCreateHome.returncode == 0:
        
        print(Fore.WHITE + f'{doCreateHome_out}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(Fore.WHITE + f'{doCreateHome_err}')
        print(f'\n')
        print(f'\n')

    createDesktop = f'echo {sudo_password} | sudo mkdir /home/{user}/Desktop'
    doCreateDesktop = subprocess.Popen(createDesktop, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doCreateDesktop_out, doCreateDesktop_err = doCreateDesktop.communicate()
    
    if doCreateDesktop.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doCreateDesktop_out}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doCreateDesktop_err}')
        print(f'\n')
        print(f'\n')
            
    createToolsDir = f'echo {sudo_password} | sudo mkdir /home/{user}/Desktop/tools'
    doCreateToolsDir = subprocess.Popen(createToolsDir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doCreateToolsDir_out, doCreateToolsDir_err = doCreateToolsDir.communicate()
    
    if doCreateToolsDir.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doCreateToolsDir_out}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doCreateToolsDir_err}')
        print(f'\n')
        print(f'\n')

    change = f'echo {sudo_password} | sudo chmod 777 /home/{user}; echo {sudo_password} | sudo chmod 777 /home/{user}/Desktop; echo {sudo_password} | sudo chmod 777 /home/{user}/Desktop/tools; echo {sudo_password} | sudo chown {user} /home/{user}; echo {sudo_password} | sudo chown {user} /home/{user}/Desktop; echo {sudo_password} | sudo chown {user} /home/{user}/Desktop/tools;'
    doChange = subprocess.Popen(change, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doChange_out, doChange_err = doChange.communicate()
    
    if doChange.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChange_out}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChange_err}')
        print(f'\n')
        print(f'\n')

    ### Package managers
    print(Fore.YELLOW + "*******************************")
    print(f'\n')
    print(Fore.YELLOW + "Installing package managers\nSNAP\nGEM\nNixNote2\nNautilus-dropbox\nKeepassxc\nPython3-pip\nDNF")
    print(f'\n')
    print(f'\n')
    
    installPackage = f'echo {sudo_password} | sudo apt install snapd gem nixnote2 nautilus-dropbox keepassxc python3-pip dnf -y'
    doInstallPackage = subprocess.Popen(installPackage, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doInstallPackage_out, doInstallPackage_err = doInstallPackage.communicate()

    if doInstallPackage.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallPackage_out}')
        print(Fore.YELLOW + f'\nInstallation of package managers has succeeded at\n{formatted_time} !')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallPackage_err}')
        print(f'\n')
        
        print(Fore.RED + f'Failed to install of package managers has failed at\n{formatted_time} :(')
        print(f'\n')
        print(f'\n')

    # Installing pyautogui
    print(Fore.YELLOW + "\nInstalling pyautogui...\n")
    
    installPyautogui = f'pip3 install pyautogui'
    doInstallPyautogui = subprocess.Popen(installPyautogui, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doInstallPyautogui_out, doInstallPyautogui_err = doInstallPyautogui.communicate()

    if doInstallPyautogui.returncode == 0:
        
        print(f'\n')
        print(f'{doInstallPyautogui_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Installation of pyautogui has succeeded!')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallPyautogui_err}')
        print(f'\n')
        print(Fore.RED + "Failed to install pyautogui...:(\nPackage manager python3-pip might not be installed correctly :(\nSkipping...")
        print(f'\n')
        print(f'\n')

    ### Recon tools
    print(f'\n')
    print(Fore.YELLOW + "### Installing recon tools...###")
    print(f'\n')
    path = f'/home/{user}/Desktop/tools/'
        
    # Downloading Sn1per
    print(Fore.YELLOW + "\nInstalling Sn1per...\n")
    
    downloadSn1per = f'echo {sudo_password} | sudo git clone https://github.com/1N3/Sn1per.git;' 
    doDownloadSn1per = subprocess.Popen(downloadSn1per, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doDownloadSn1per_out, doDownloadSn1per_err = doDownloadSn1per.communicate()
    
    if doDownloadSn1per.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doDownloadSn1per_out}')
        print(f'\n')
        print(Fore.YELLOW + f'1N3/Sn1per has been downloaded successfully!')
        print(f'\n')
        print(f'Please cd ~/{user}/Desktop/tools/Sn1per => sudo bash Download.sh')
        print(f'\n')
        print(f'Proceeding to change Sn1per folder permissions...')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(f'{doDownloadSn1per_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to download Sn1per :(')
        print(f'\n')
        print(f'\n')
                  
    changeSn1perPermission = f'echo {sudo_password} | sudo chown {user} ./S1nper; echo {sudo_password} | sudo chmod 777 {user} ./Sn1per; echo {sudo_password} | sudo chown {user} ./Sn1per/install.sh; echo {sudo_password} | sudo chmod 777 {user} ./Sn1per/install.sh'
    doChangeSn1perPermission = subprocess.Popen(changeSn1perPermission, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    doChangeSn1perPermission_out, doChangeSn1perPermission_err = doChangeSn1perPermission.communicate()

    if doChangeSn1perPermission.returncode == 0:
        
        #print(f'\n')
        print(Fore.WHITE + f'{doChangeSn1perPermission_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in changing Sn1per ownership to {user} at\n{formatted_time}')
        print(f'\n')
        print(Fore.YELLOW + f'Please proceed to ./Sn1per/install.sh for installation :)...')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChangeSn1perPermission_err}')
        print(Fore.RED + f'Failed to change Sn1per ownership to {user}...\nSkipping...')
        print(f'\n')
        print(f'\n')                
            
    #Downloading Sherlock
    print(Fore.YELLOW + "\nDownloading Sherlock...\n")
    
    downloadSherlock = f'echo {sudo_password} | sudo git clone https://github.com/sherlock-project/sherlock.git'
    doDownloadSherlock = subprocess.Popen(downloadSherlock, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doDownloadSherlock_out, doDownloadSherlock_err = doDownloadSherlock.communicate()

    if doDownloadSherlock.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doDownloadSherlock_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in downloadation of Sherlock has succeeded at\n{formatted_time}!\n\nProceeding to change Sherlock folder permissions at\n{formatted_time}\n\n')
        print(f'\n')
        print(Fore.YELLOW + f'Please proceed to ./sherlock for installation AND(OR) configuration...')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.RED + f'{doDownloadSherlock_err}')
        print(f'\n')
        print(f'\n')
        
    changeSherlockPermission = f'echo {sudo_password} | sudo chown {user} ./sherlock; echo {sudo_password} | sudo chmod 777 {user} ./sherlock; echo {sudo_password} | sudo chown {user} ./sherlock;'
    doChangeSherlockPermission = subprocess.Popen(changeSherlockPermission, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doChangeSherlockPermission_out, doChangeSherlockPermission_err = doChangeSherlockPermission.communicate()

    if doChangeSherlockPermission.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChangeSherlockPermission_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in changing Sherlock ownership to {user} at\n{formatted_time}')
        print(f'\n')
        print(Fore.YELLOW + f'Please proceed to ./sherlock/install.sh for installation :)')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChangeSherlockPermission_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to change Sherlock ownership to {user}...\nSkipping...')
        print(f'\n')
        print(f'\n')

    # Installing RedHawk
    print(f'\n')
    print(Fore.YELLOW + "Downloading RedHawk...")
    print(f'\n')
    
    installRedHawk = f'echo {sudo_password} | sudo git clone https://github.com/Tuhinshubhra/RED_HAWK.git'
    doInstallRedHawk = subprocess.Popen(installRedHawk, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doInstallRedHawk_out, doInstallRedHawk_err = doInstallRedHawk.communicate()

    if doInstallRedHawk.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallRedHawk_out}')
        print(Fore.YELLOW + "Succeeded in downloading RedHawk has succeeded!\nProceeding to change permissions...")
        print(f'\n')
        print(Fore.YELLOW + f'Please proceed to ./RED_HAWK for installation AND(OR) configuration...')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallRedHawk_err}')
        print(Fore.RED + f'Failed to download RedHawk :(')
        print(f'\n')
        print(f'\n')
        
    changeRedHawkPermissions = f'echo {sudo_password} | sudo chown {user} ./RED_HAWK; echo {sudo_password} | sudo chmod 777 {user} ./RED_HAWK;'
    doChangeRedHawkPermissions = subprocess.Popen(changeRedHawkPermissions, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doChangeRedHawkPermissions_out, doChangeRedHawkPermissions_err = doChangeRedHawkPermissions.communicate()
    
    if doChangeRedHawkPermissions.returncode == 0:
        
        print(f'\n')
        print(f'{doChangeRedHawkPermissions_out}')
        print(Fore.YELLOW + f'Succeeded in changing RED_HAWK ownership & permissions!\n')
    
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChangeRedHawkPermissions_err}')
        print(Fore.RED + f'Failed to change ownership & permissions for RED_HAWK...\nSkipping...')        
        print(f'\n')
        print(f'\n')

    # Installing SecLists
    print(Fore.YELLOW + "\nInstalling Seclist...\n")
    
    installSeclist = f'echo {sudo_password} | sudo git clone https://github.com/danielmiessler/SecLists.git'
    doInstallSeclist = subprocess.Popen(installSeclist, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doInstallSeclist_out, doInstallSeclist_err = doInstallSeclist.communicate()

    if doInstallSeclist.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallSeclist_out}')
        print(f'\n')
        
        print(Fore.YELLOW + f'\nSucceeded in download Seclists at\n{formatted_time}')
        print(f'\n')
        print(f'\n')
        
        chmod777_secLists = f'echo {sudo_password} | sudo chmod 777 ./SecLists'
        do_chmod777_secLists = subprocess.Popen(chmod777_secLists, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        do_chmod777_secLists_out, do_chmod777_secLists_err = do_chmod777_secLists.communicate()
        
        if do_chmod777_secLists.returncode == 0:
            
            print(f'\n')
            print(Fore.WHITE + f'{do_chmod777_secLists_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in chmod 777 for ./SecLists')
            print(f'\n')
            print(f'\n')
            
        else:
            
            print(f'\n')
            print(Fore.WHITE + f'{do_chmod777_secLists_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to chmod 777 ./SecLists at {formatted_time}')
            print(f'\n')
            print(f'\n')
            
    else:
        
        print(f'\n')
        print(f'{doInstallSeclist_err}')
        print(f'\n')
        print(Fore.RED + f'\nFailed to install Seclist at\n{formatted_time}')
        print(f'\n')
        print(f'\n')
    
                
    # Install EyeWitness
    print(Fore.YELLOW + "### Installing EyeWitness ###")
    print(Style.RESET_ALL)
    
    installEyewitness = f'echo {sudo_password} | sudo git clone https://github.com/RedSiege/EyeWitness.git'
    doInstallEyewitness = subprocess.Popen(installEyewitness, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doInstallEyewitness_out, doInstallEyewitness_err = doInstallEyewitness.communicate()

    if doInstallEyewitness.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallEyewitness_out}')
        doInstallEyewitness
        print(Fore.YELLOW + f'Succeeded in downloading EyeWitness at\n{formatted_time}')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.RED + f'{doInstallEyewitness_err}')
        print(f'\n')
            
    changeEyeWitnessPermission = f'echo {sudo_password} | sudo chown {user} ./EyeWitness; echo {sudo_password} | sudo chmod 777 ./EyeWitness;'
    doChangeEyeWitnessPermission = subprocess.Popen(changeEyeWitnessPermission, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doChangeEyeWitnessPermission_out, doChangeEyeWitnessPermission_err = doChangeEyeWitnessPermission.communicate()
    
    if doChangeEyeWitnessPermission.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChangeEyeWitnessPermission_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in changing permission for ./EyeWitness at\n{formatted_time}')
        print(f'\n')
        print(Fore.YELLOW + f'Please proceed to ./evil-winrm for installation AND(OR) configuration...')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(f'{doChangeEyeWitnessPermission_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to change permissions for ./EyeWitness at\n{formatted_time}\nSkipping...')
        print(f'\n')
        print(f'\n')

    # Install Evil-WinRM
    print(Fore.YELLOW + "### Installing Evil-WinRM ###")
    print(f'\n')
    
    installEvilwinrm = f'echo {sudo_password} | sudo git clone https://github.com/Hackplayers/evil-winrm.git'
    doInstallEvilwinrm = subprocess.Popen(installEvilwinrm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doInstallEvilwinrm_out, doInstallEvilwinrm_err = doInstallEvilwinrm.communicate()

    if doInstallEvilwinrm.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallEvilwinrm_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in downloading Evil-WinRM at ./evil-winrm\nProceeding to change permissions for ./EyeWitness')
        print(f'\n')
        print(f'\n')
        
        gem_winrm = f'echo {sudo_password} | sudo gem install winrm'
        install_gem_winrm = subprocess.Popen(gem_winrm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        install_gem_winrm_out, install_gem_winrm_err = install_gem_winrm.communicate()
        
        if install_gem_winrm.returncode == 0:
            
            print(f'\n')
            print(Fore.WHITE + f'{install_gem_winrm_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in downloading Evil-WinRM dependency1: {gem_winrm} :D at {formatted_time}')
            print(f'\n')
            print(Fore.YELLOW + f'Please proceed to ./evil-winrm for installation AND(OR) configuration...')
            print(f'\n')
            print(f'\n')
            
        else:
            
            print(f'\n')
            print(Fore.WHITE + f'{install_gem_winrm_err}')
            print(Fore.RED + f'Failed to download Evil-WinRM dependency1: {gem_winrm} at {formatted_time}')
            print(f'\n')
            print(Fore.RED + f'You must {gem_winrm} to get it running!!')
            print(f'\n')
            print(f'\n')
            
            
        gem_winrm_fs = f'echo {sudo_password} | sudo gem install winrm-fs'
        install_gem_winrm_fs = subprocess.Popen(gem_winrm_fs, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        install_gem_winrm_fs_out, install_gem_winrm_fs_err = install_gem_winrm_fs.communicate()
        
        if install_gem_winrm_fs.returncode == 0:
            
            print(f'\n')
            print(Fore.WHITE + f'{install_gem_winrm_fs_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in installing Evil-WinRM dependency2: {gem_winrm_fs} at {formatted_time}')
            print(f'\n')
            print(f'\n')
            
        else:
            
            print(f'\n')
            print(Fore.WHITE + f'{install_gem_winrm_fs_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to install Evil-WinRM dependency2: {gem_winrm_fs} at {formatted_time}')
            print(f'\n')
            print(Fore.RED + f'You must {gem_winrm_fs} to get it running!!')
            print(f'\n')
            print(f'\n')
            
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallEvilwinrm_err}')
        print(f'\n')
        print(f'\n')
        
    changeEvilWinRm = f'echo {sudo_password} | sudo chown {user} ./evil-winrm; echo {sudo_password} | sudo chmod 777 ./evil-winrm;'
    doChangeEvilWinRm = subprocess.Popen(changeEvilWinRm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doChangeEvilWinRm_out, doChangeEvilWinRm_err = doChangeEvilWinRm.communicate()
    
    if doChangeEvilWinRm.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChangeEvilWinRm_out}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChangeEvilWinRm_err}')
                    
    # Install Powerline
    print(Fore.YELLOW + "### Downloading Powerline ###")
    print(Style.RESET_ALL)
    
    installPowerline = f'echo {sudo_password} | sudo git clone https://github.com/powerline/powerline.git'
    doInstallPowerline = subprocess.Popen(installPowerline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doInstallPowerline_out, doInstallPowerline_err = doInstallPowerline.communicate()

    if doInstallPowerline.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallPowerline_out}')
        print(f'\n')
        
        print(Fore.YELLOW + f'Succeeded in downloading Powerline at ./evil-winrm at\n{formatted_time}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallPowerline_err}')
        print(f'\n')
        print(f'\n')
        
    changePowerLine = f'echo {sudo_password} | sudo chown {user} ./powerline; echo {sudo_password} | sudo chmod 777 ./powerline'
    doChangePowerLine = subprocess.Popen(changePowerLine, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doChangePowerLine_out, doChangePowerLine_err = doChangePowerLine.communicate()
                    
    if doChangePowerLine.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChangePowerLine_out}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doChangePowerLine_err}')
        print(f'\n')
        print(f'\n')
            
    # Install BeefProject
    print(Fore.YELLOW + "### Installing Beef-XSS ###")
    print(Style.RESET_ALL)
    #os.system('sudo -u {} sudo apt install beef-xss -y'.format(user))
    #beefXSSPath = f'/home/{user}/Desktop/tools/beef-xss/'
    installBeefXSS = f'echo {sudo_password} | sudo apt install beef-xss -y'
    doInstallBeefXSS = subprocess.Popen(installBeefXSS, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doInstallBeefXSS_out, doInstallBeefXSS_err = doInstallBeefXSS.communicate()

    if doInstallBeefXSS.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallBeefXSS_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in installing Beef-XSS at\n{formatted_time}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doInstallBeefXSS_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to install Beef-XSS :(\Skipping...')
        print(f'\n')
        print(f'\n')
        
    print(Fore.YELLOW + f'\nEnabling Beef-XSS binary at\n{formatted_time}...')
    enableBeefXSS = f'echo {sudo_password} | sudo systemctl enable beef-xss'
    doEnableBeefXSS = subprocess.Popen(enableBeefXSS, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doEnableBeefXSS_out, doEnableBeefXSS_err = doEnableBeefXSS.communicate()
                
    if doEnableBeefXSS.returncode == 0:
        
        print(f'\n')
        print(f'{doEnableBeefXSS_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in enabling Beef-XSS\nStarting up Beef-XSS!')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doEnableBeefXSS_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to enable Beef-XSS :(\nSkipping...')
        print(f'\n')
        print(f'\n')
        
    startBeefXSS = f'echo {sudo_password} | sudo systemctl start beef-xss'
    doStartBeefXSS = subprocess.Popen(startBeefXSS, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doStartBeefXSS_out, doStartBeefXSS_err = doStartBeefXSS.communicate()
                    
    if doStartBeefXSS.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doStartBeefXSS_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in starting up Beef-XSS at\n{formatted_time}\nProceeding to configure Beef-XSS!')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doStartBeefXSS_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to start Beef-XSS :(\nSkipping')
        print(f'\n')
        print(f'\n')
        
    # Locate Beef-XSS config file
    # Save it to var $beefDir                        
    print(Fore.YELLOW + f'Changing Beef-XSS login credentials...')
    print(f'\n')
    
    beefConf = f'/etc/beef-xss/config.yaml'
    beefPermission = f'echo {sudo_password} | sudo chmod 777 {beefConf}'
    do_beefPermission = subprocess.Popen(beefPermission, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    do_beefPermission_out, do_beefPermission_err = do_beefPermission.communicate()
    
    if do_beefPermission.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{do_beefPermission_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in chmod 777 {beefConf} at {formatted_time}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{do_beefPermission_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to chmod 777 {beefConf}')
        print(f'\n')
        print(f'\n')
        
    #beefuser = input(Fore.YELLOW + "Enter new username for Beef-XSS UI login: ")
    editLoginCommand = f'echo {sudo_password} | sudo sed -i \'s/user\s*\: "beef"/user\: {newUser}/g\' {beefConf}; echo {sudo_password} | sudo sed -i \'s/passwd\s*\:\s*"beef"/passwd\: {newPassword}/g\' {beefConf}'
    doEditLogin=subprocess.Popen(editLoginCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    doEditLogin_out, doEditLogin_err = doEditLogin.communicate()
                        
    if doEditLogin.returncode == 0:
        
        print(f'\n')
        print(f'{doEditLogin_out}')
        print(Fore.YELLOW + f'\nSucceeded in changing Beef-XSS Login credentials in {beefConf} at\n{formatted_time}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doEditLogin_err}')
        print(f'\n')
        print(f'\n')
        
    ### Copy current Beef-XSS Login credentials to ./beef-login.txt
    
    print(Fore.YELLOW + f'Copying beef-xss config from {beefConf} to ./beef-login.txt')
    print(f'\n')
    
    createLoginCommand = f'echo {sudo_password} | sudo cat {beefConf} > ./beef-login.txt'
    doCreateLogin=subprocess.Popen(createLoginCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    doCreateLogin_out, doCreateLogin_err = doCreateLogin.communicate()
                            
    if doCreateLogin.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doCreateLogin_out}')
        print(f'\n')
        print(Fore.YELLOW + f'Succeeded in copying Beef-XSS config to ./beef-login.txt at {formatted_time}')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doCreateLogin_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to copy Beef-XSS config to ./beef-login.txt at {formatted_time}')
        print(f'\n')
        print(f'\n')
                        
    # Restart Beef-XSS
    print(Fore.YELLOW + f'\nRestarting Beef-XSS...\n')
    restartBeefXSS = f'echo {sudo_password} | sudo systemctl restart beef-xss'
    doRestartBeefXSS = subprocess.Popen(restartBeefXSS, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    doRestartBeefXSS_out, doRestartBeefXSS_err = doRestartBeefXSS.communicate()
                                        
    if doRestartBeefXSS.returncode == 0:
        
        print(f'\n')
        print(Fore.WHITE + f'{doRestartBeefXSS_out}')
        print(f'\n')
        
        print(Fore.YELLOW + f'\nSucceeded in restarting Beef-XSS at\n{formatted_time}')
        print(f'\n')
        print(Fore.YELLOW + f'\n\nBeef-XSS is now accessible at http://127.0.0.1:3000/ui/authentication')
        print(f'\n')
        
        print(Fore.YELLOW + f'You may change your Beef-XSS login in /etc/beef-xss/config.yaml')
        print(Fore.YELLOW + f'user: "beef"\npasswd: "beef"')
        print(f'\n')
        print(Fore.YELLOW + f'Restart after login changed by: sudo systemctl restart beef-xss')
        print(f'\n')
        print(f'\n')
        
        print(Fore.YELLOW + f'Type command \'beef-xss\' to start Beef-XSS Web Browser for using :D')
        print(f'\n')
        print(f'\n')
        
    else:
        
        print(f'\n')
        print(Fore.WHITE + f'{doRestartBeefXSS_err}')
        print(Fore.RED + f'\nFailed to restart Beef-XSS...\nYou may restart Beef-XSS yourself then to login using your credentials in ./beef-login.txt\nat http://127.0.0.1:3000/ui/authentication')
        print(f'\n')
        print(f'Skipping...')
        print(f'\n')
        print(f'\n')
                  
 