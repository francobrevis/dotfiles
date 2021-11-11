#!/bin/sh
if [ $(bluetoothctl show | grep "Powered: yes" | wc -c) -eq 0 ]
then
  #echo "%{F#66ffffff}"
  echo "%{F#66ffffff}TRUE"
else
  if [ $(echo info | bluetoothctl | grep 'Device' | wc -c) -eq 0 ]
  then 
    #echo ""
    echo "FALSE"
  fi
  #echo "%{F#2193ff}"
  echo "%{F#2193ff}TREE"
fi

