#!/bin/bash

if [ $UID -ne "0" ]
then
    echo "This script requires root privileges. To run it: "
    echo 
    echo " $ sudo $0"
    echo 
    exit 1
fi

apt-get install python-pip
pip install virtualenv


