#!/bin/bash

. wifiCommon.sh
. workflowHandler.sh

str="$1"
wifi=${str:11:3}

# Handle action
if [ "$wifi" != "" ]; then
  if [ "$wifi" == "On" ] || [ "$wifi" == "Off" ]; then
  	networksetup -setairportpower $INTERFACE $wifi
  else
	echo $wifi | tr -d '\n'
  fi
  exit
fi
