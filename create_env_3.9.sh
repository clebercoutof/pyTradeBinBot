#!/bin/sh
## HEADER FOR SHELL SCRIPT

# PYTHON 3.7 VENV INSTALL
# sudo apt install python3.7-venv

## GETS CURRENT DIRECTORY AS SYSTEM VARIABLE
CURRENT_DIR=$(pwd)
STR_DIR="CURRENT DIRECTORY:"
## PRINTS CURRENT DIRECTORY
#echo $STR_DIR
#echo $CURRENT_DIR

## READS ENV NAME AND CREATES ENV FULL PATH
read -p "Enter Your VIRTUAL ENV name: " venv_name

## Print example with concatenating variables
#echo "Full Path: ${CURRENT_DIR}/${venv_name}"
NEW_PATH=$(realpath ${CURRENT_DIR})/${venv_name}

#ENV_PATH= $CURRENT_DIR + "/" + $venv_name
echo "Output Path: ${NEW_PATH} "
python3.9 -m venv ${NEW_PATH}

## ADD A BLANK LINE IN ORDER TO WRITE THE ALIAS
BASH_FILE=/home/${USER}/.bashrc
echo "" >> $BASH_FILE
echo "alias activate_${venv_name}='source ${NEW_PATH}/bin/activate'" >> $BASH_FILE
echo "" >> $BASH_FILE
chmod a+x $BASH_FILE

## THIS COMMAND FORCES RELOAD OF BASH FILES AND REMOTE USER MANUALLY CONFIGURED VARIABLES
exec bash
