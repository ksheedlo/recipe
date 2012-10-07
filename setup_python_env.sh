#!/bin/bash

check(){
    if [[ "$?" -ne "0" ]]
    then
        echo "$0 FAILED"
        exit 1
    fi
}

virtualenv python_env
. python_env/bin/activate

pip install Django==1.4.1
check

echo "################################################################################"
echo "#"
echo "# The Python virtual environment is ready to use. To start it,"
echo "#"
echo "# $ . python_env/bin/activate"
echo "#"
echo "################################################################################"
