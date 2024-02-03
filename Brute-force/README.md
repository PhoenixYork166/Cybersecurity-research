## Hi Fellow hackers
## 
## This folder is used for DoS testing
## 
## Please use along with Kali Linux
## providing you with bunch of namelists & wordlists
## in /usr/share/wordlists/
## metasploit namelist /usr/share/wordlists/metasploit/namelist.txt
##
## Rock you /usr/share/wordlists/rockyou.txt
## Downlaod rockyou.txt
## sudo wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt;
##
## Brute-forcing tools used
## hydra
## https://www.kali.org/tools/hydra/
##
## 1N3/Sn1per
## https://github.com/1N3/Sn1per
##
## Using Hydra & 1N3/Sn1per as DoS tools
## combined fire-superiority with TMUX
## TMUX = Terminal multiplexer
## Thus, we can consolidate our fire-power
## of running a single Brute-force script
## in 100 numbers of terminal on a 16 CPU & 16GB RAM Kali Linux
##
## TMUX https://github.com/tmux/tmux
## Usage of TMUX multiplexer
## 
## You may try out this Multiplexer on a super-computer :D
## script='hydra-hardcode.sh';

# Trial & Error tested
# maximum of 100 sessions can be handled by a 16 CPU + 16GB RAM VM
## #!/bin/bash
## sessions=100;
##
## for ((i=0; i<$sessions; i++));
## do
##    tmux new-session -d -s "session${i}" "bash ${script}";
## done
