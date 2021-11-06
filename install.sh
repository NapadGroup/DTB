#!/bin/bash

GREEN=`tput setaf 2`

clear

sudo rm /usr/share/DTB

sudo mkdir /usr/share/DTB

sudo cp -T -f ./src/DTB.py  /usr/share/DTB/DTB.py

sudo cp -T -f dtb /usr/bin/dtb

sudo chmod +x /usr/bin/dtb

echo "${GREEN}Use dtb Command to Run DTB"