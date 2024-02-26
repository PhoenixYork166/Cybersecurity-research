#!/bin/sh
#iptables.sh

#SSH_IP="1.1.1.1.1"

# delete all rules
iptables -F
iptables -X
iptables -Z
iptables -t nat -F

## block all
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP

# allow local connections
iptables -A INPUT  -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# allow established access
iptables -A INPUT -j ACCEPT -m conntrack --ctstate ESTABLISHED,RELATED
iptables -A OUTPUT -j ACCEPT -m conntrack --ctstate ESTABLISHED,RELATED

## INPUT
# allow from remote, ssh
#iptables -A INPUT -j ACCEPT -i vmbr0 -s "$SSH_IP" -p tcp --dport 22
iptables -A INPUT -j ACCEPT -p tcp --dport 22
# allow from fw-WAN, ssh
iptables -A INPUT -j ACCEPT -i vmbr0 -p tcp --dport 22
iptables -A INPUT -j ACCEPT -i vmbr1 -p tcp --dport 22
# allow from WAN http, https, dns, ping
iptables -A INPUT -j ACCEPT -i vmbr0 -p tcp --sport 80
iptables -A INPUT -j ACCEPT -i vmbr0 -p tcp --sport 443
iptables -A INPUT -j ACCEPT -i vmbr0 -p udp --sport 53
iptables -A INPUT -j ACCEPT -i vmbr0 -p icmp
iptables -A INPUT -j ACCEPT -i vmbr1 -p icmp

## OUTPUT
# allow to host, http, https, dns, ping
iptables -A OUTPUT -j ACCEPT -o vmbr0 -p tcp --dport 80
iptables -A OUTPUT -j ACCEPT -o vmbr0 -p tcp --dport 443
iptables -A OUTPUT -j ACCEPT -o vmbr0 -p udp --dport 53
# allow to fw-WAN, ping
iptables -A OUTPUT -j ACCEPT -o vmbr1 -p icmp
# allow to LAN, ssh
iptables -A OUTPUT -j ACCEPT -o vmbr1 -p tcp --dport 22
iptables -A OUTPUT -j ACCEPT -p tcp --dport 22

# forward packet from host to firewall
iptables -A FORWARD -j ACCEPT -i vmbr0 -o vmbr1
iptables -A FORWARD -j ACCEPT -i vmbr1 -o vmbr0

## PREROUTING
# route tcp to firewall, except ssh
iptables -A PREROUTING -t nat -j DNAT -i vmbr0 -p tcp --match multiport ! --dports 22 --to-destination 10.0.0.2
# route udp to firewall
iptables -A PREROUTING -t nat -j DNAT -i vmbr0 -p udp --to-destination 10.0.0.2

## POSTROUTING
# masquerade fw-WAN
iptables -A POSTROUTING -t nat -j MASQUERADE -o vmbr0 -s 10.0.0.0/30