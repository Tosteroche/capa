#!/bin/bash

IPTABLES="/sbin/iptables"
INT="eth0:0"
EXT="eth0"
SRV="192.168.1.1"
SPRT="80"
DPRT="8000"


# Clean rule
$IPTABLES -F
$IPTABLES -t nat -F
$IPTABLES -t nat -X mac_check


# Create rule for mac check
$IPTABLES -t nat -N mac_check
$IPTABLES -t nat -A mac_check -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
$IPTABLES -t nat -A mac_check -p tcp -m tcp --dport $SPRT -j DNAT --to-destination $SRV:$DPRT

# Create rule for internet access
$IPTABLES -t nat -A PREROUTING -j mac_check
$IPTABLES -t nat -A POSTROUTING -o $EXT -j MASQUERADE

