#!/usr/bin/env python

#This script guides the user through the various steps needed to install ShodanCLI 
#Simply run this script and follow the prompts

import os
import signal
import sys
import time
import subprocess
import shlex

def API_key(*varargs):

    print("Do you have your Shodan API key ready to go?\ny for yes; n for no")
    key_ready=raw_input('')
    if key_ready == 'y':
        print("Cool - we can initialise it right now. Do you want to proceed?\ny for yes; n for no")
        key_proceed=raw_input('')
        if key_proceed == 'y':
            print('Enter the key now:')
            key_API=raw_input('')
            print('Initilising now....')
            subprocess.call(shlex.split("shodan init %key_API"))
        elif key_proceed == 'n':
            print("Ok - next time.")
    else:
        print("You dont know what you're missing :)\n Laterz!")
        exit()

    return;

print("Welcome to Shodan CLI installer!")
print("#########################################")
print("You need PIP installed for this to work - do you have PIP installed?\ny for yes; n for no")



#Get UserInput for PIP installation
pip_installed=raw_input('')



if pip_installed == 'y':
    print("Cool. Moving to the next step.")
    print("Starting the Shodan CLI install now....")
    subprocess.call(shlex.split("pip install shodan"))
    API_key()

elif pip_installed == 'n':
        print("No worries, do you want to install it now?\ny for yes; n for no")
        pip_get = raw_input('')

        if pip_get == 'y':
            print("Ok, let's get PIP installed.")
            subprocess.call(shlex.split("sudo apt-get install python-pip"))
            API_key()

        elif pip_get == 'n':
            print("Cool. Stopping the script now...")
            exit()

else:
    print("That is not an option dude... Pick y or n!")
    exit()
