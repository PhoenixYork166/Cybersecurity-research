git clone https://github.com/praetorian-inc/Hob0Rules.git;

chmod 777 ./Hob0Rules;
chmod 777 ./Hob0Rules/*.*;
chmod 777 ./Hob0Rules/*;
chmod 777 ./Hob0Rules/wordlists;
chmod 777 ./Hob0Rules/wordlists/*.*;

gunzip ./Hob0Rules/wordlists/rockyou.txt.gz;
chmod 777 ./Hob0Rules/wordlists/rockyou.txt;
mv ./Hob0Rules/wordlists/rockyou.txt .;

# Install TMUX
apt update -y;
apt install -y tmux;
