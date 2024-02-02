#!/bin/bash

# Normal Mode
# sniper -t <TARGET>

# Stealth mode + OSINT + RECON
# sniper -t <TARGET> -m stealth -o -re

# Discover mode
# sniper -t <CIDR> -m discover -w <WORKSPACE_ALIAS>

# Full Port Scan mode
# sniper -t <TARGET> -fp

# ENABLE Bruteforce mode
# sniper -t <TARGET> -b

# Airstrike mode
# sniper -f targets.txt -m airstrike

# Nuke mode with target list, Bruteforce enabled
# sniper -f targets.txt -m nuke -w <WORKSPACE_ALIAS>