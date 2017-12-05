#!/bin/bash

. wifiCommon.sh
. workflowHandler.sh

INFO=$($AIRPORT --getinfo)
SAVED_APS=$(networksetup -listpreferredwirelessnetworks $INTERFACE)
ACTIVE_BSSID=$(getBSSID "$INFO")

# Sort scan lines and remove header
SORTED=$(echo "$($AIRPORT --scan)" | awk 'NR>1' | sort)

if [ "$SORTED" == "" ]; then
  # Handle no wifi access points found
  addResult "" "Null" "No access points found" "" "$ICON_WIFI_ERROR"
else
  # Parse sorted scan lines
  while read -r LINE; do
    OUTPUT=$(getAPDetails "$LINE" "$ACTIVE_BSSID" "$SAVED_APS")
    IFS='~' read -r -a ARRAY <<< "$OUTPUT"

    addResult "" "${ARRAY[0]}" "${ARRAY[0]}" "RSSI ${ARRAY[2]} dBm, channel ${ARRAY[3]}" "${ARRAY[5]}"
  done <<< "$SORTED"
fi

getXMLResults
