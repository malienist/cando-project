#!/usr/bin/env python
# Shodan IOC downloader for malware
# Vishal Thakur
# Released under MIT license
import os
import signal
import sys
import time
import subprocess
import shlex

def start_downloader(*varargs):
    dl_proceed_limit=raw_input("Please enter the number of results you want to limit this download to:\n"
          "(Eg. 10000 results cost one Credit) ")

    dl_proceed_category=raw_input("Enter the category:\n(pick one 'malware' OR 'ics'):")
    dl_proceed_filename=raw_input("Enter the filename for the new report:")

    subprocess.call(shlex.split('shodan download --limit '+dl_proceed_limit, + dl_proceed_filename, 'category:'+ dl_proceed_category))


print("Welcome to Shodan IOC Downloader")
print("#########################################")
print("You need Shodan CLI Installed in order for this script to run successfully."
    "\n"
      "\nIf you do not have it installed, please install it and then run this script again."
      "\nYou can get the Shodan CLI Installer here: https://github.com/vithakur/shodan-tools ")
print("\nYou can proceed to download IOC from Shodan by using your existing Credits - do you have at least 1 Shodan Credit?\ny for yes; n for no")

#Get UserInput to proceed
dl_proceed=raw_input('')

if dl_proceed == 'y':
    print("Cool. Moving to the next step.")
    print("Starting the Shodan CLI now....")
    start_downloader()
else:
    print("Need to register with Shodan and get Credits: http://shodan.io")
    exit()





