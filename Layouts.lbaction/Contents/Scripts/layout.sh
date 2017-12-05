#!/bin/bash
# Handle action
if [ "$1" != "" ]; then
	/usr/bin/perl layout.pl "$1"
fi
osascript execute.scpt "$@"
exit 0