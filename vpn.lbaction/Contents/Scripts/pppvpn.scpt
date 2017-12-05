set vpn_server to system attribute "query"
tell application "System Events"
	tell current location of network preferences
		set VPN to service vpn_server
		if connected of current configuration of VPN then
			disconnect VPN
			set result to "Disconnecting to VPN " & vpn_server
		else
			connect VPN
			set result to "Connecting to VPN " & vpn_server
		end if
	end tell
end tell