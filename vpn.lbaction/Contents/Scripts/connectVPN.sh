#!/bin/bash
vpn=$1
vpnInfo="$(scutil --nc show "${vpn}")"
isConnected="$(echo "${vpnInfo}" | grep Disconnected)"
isL2TP="$(echo "${vpnInfo}" | grep L2TP)"
if [[ -z "$isL2TP" ]]; then
	if [[ -n "$isConnected" ]]; then
		scutil --nc start "${vpn}"
		echo "Connecting to VPN ${vpn}"
	else
		scutil --nc stop "${vpn}"
		echo "Disconnecting to VPN ${vpn}"
	fi
else
	query="${vpn}" osascript ./pppvpn.scpt 
fi
