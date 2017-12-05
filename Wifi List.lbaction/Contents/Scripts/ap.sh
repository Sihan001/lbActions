#!/bin/bash

. wifiCommon.sh
. workflowHandler.sh

# Handle action
if [ "$1" != "" ]; then
  if [ "$1" == "Null" ]; then
    exit
  fi

  # Extract password for AP, which is needed by networksetup
  PASS=$(security 2>&1 >/dev/null find-generic-password -ga "$1" \
    | awk '/ / {print $2}' | tr -d '"')
  networksetup -setairportnetwork $INTERFACE $1 $PASS
  exit
fi