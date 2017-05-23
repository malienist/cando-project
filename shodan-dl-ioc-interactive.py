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
#Start the downloading process
def start_downloader(*varargs):
    #User input for various options
    dl_proceed_limit=raw_input("Please enter the number of results you want to limit this download to:\n"
          "(Eg. 10000 results cost one Credit ) ")
    dl_proceed_category=raw_input("Enter the category:\n(pick one 'malware' OR 'ics'):")
    dl_proceed_filename=raw_input("Enter the filename for the new report: ")
    #Used for conversion to CSV later on#Used for conversion to CSV later on
    suffix=".json.gz"
    #The actual command used, with all the options
    subprocess.call(['shodan', 'download', '--limit', dl_proceed_limit, dl_proceed_filename, 'category:', dl_proceed_category])
    print("Do you want to convert the results into a CSV file?\n (Press y for YES, n for NO: ")
    #Converting the JSON file into CSV
    dl_convert=raw_input('')
    if dl_convert == 'y':
        subprocess.call(['shodan', 'convert', dl_proceed_filename + suffix , 'csv'])
    elif dl_convert == 'n':
        print("Thanks for using this script! End of program.")

    else:
        print("Input not recognised by the script. Exiting.")
        exit()
    return
#Start of the program - welcome script
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





