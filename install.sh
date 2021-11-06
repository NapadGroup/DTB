#!/bin/bash

clear

# colors
RED=`tput setaf 1`
GREEN=`tput setaf 2`
YELLOW=`tput setaf 3`
BLUE=`tput setaf 4`
PURPLE=`tput setaf 5`
CYAN=`tput setaf 6`
WHITE=`tput setaf 7`
BLACK=`tput setaf 8`
ORANGE=`tput setaf 9`

echo "${YELLOW}Checking Dependencies..."

# Check if the user is root
if [ $EUID -ne 0 ]; then 
    echo "${RED}We are so sorry, you should use this software as root user."
    exit
fi

function file_path()
{
    FULL_PATH="/usr/local/bin/dtb"
    echo -e "${BLUE}Choose your intallation ->\n1) Online installation\n2) Offline installation"
    read -p "${RED}Enter something >>" method

    if [ -f $FULL_PATH ]; then
        :
    fi

    if [ "$method" == "2" ]; then
            cp src/DTB.py $FULL_PATH
            echo "${GREEN}Use dtb Command to Run DTB"

    elif [ "$method" == "1" ]; then
        wget https://raw.githubusercontent.com/GodratGroup/DTB/main/src/DTB.py -O $FULL_PATH
        chmod +x $FULL_PATH
        echo "${GREEN}Use dtb Command to Run DTB"}

    else
        echo -e "${RED} Wrong input."
        exit
    fi
}

# Check package manager
function run_installation()
{
    echo -e "${ORANGE} Installing in proccess, don't do something that fucks the installation please."
    if [ $(command -v apt) &> /dev/null ]; then
        apt install -y $1 1> /dev/null
    elif [ $(command -v pacman) &> /dev/null ]; then
        pacman -S $1 --confirm 1> /dev/null
    elif [ $(command -v dnf) &> /dev/null ]; then
        dnf install -y $1 1> /dev/null
    elif [ $(command -v zypper) &> /dev/null ]; then
        zypper in $1 -n 1> /dev/null
    elif [ $(command -v rpm) &> /dev/null ]; then
        rpm install -y $1 1> /dev/null
    elif [ $(command -v eopkg) &> /dev/null ]; then
        eopkg it $1 -y 1> /dev/null
    else
        echo -e "${RED}Sorry we can't support your distro right now, please install the $1 package manually.\n Thanks for supporting us."
    fi
}

### check python
function check_python()
{
    if [ $(command -v python3) &> /dev/null ]; then
        echo -e "${GREEN}Python is already installed."

    else
        echo -e "${RED}Looks like python is not found on your system.\nNo matter, I'll try to install it."
        if run_installation python3; then
            echo "Booyah, successfully installed."
        fi
    fi
}

function install_binutils()
{
    echo -e "${GREEN} Installing binutils in proccess...\nplease wait."
    run_installation binutils
}

function main()
{
    file_path
    check_python
    install_binutils
    python3 $FULL_PATH 1>/dev/null
}

main