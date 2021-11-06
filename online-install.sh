#!/bin/bash

GREEN=`tput setaf 2`

clear

sudo rm /usr/share/DTB

sudo mkdir /usr/share/DTB

sudo wget https://raw.githubusercontent.com/GodratGroup/DTB/main/src/DTB.py -O  /usr/share/DTB/DTB.py

sudo wget https://raw.githubusercontent.com/GodratGroup/DTB/main/dtb -O /usr/bin/dtb

sudo chmod +x /usr/bin/dtb

echo "${GREEN}Use dtb Command to Run DTB"