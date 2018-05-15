#!/usr/bin/env python
# Use this script to bulk add IOCs to ThreatConnect from a CSV
# IMPORTANT!!
# Change the 'owner' to the one that you want the IOCs to be ingested under
# Make sure you change the 'Description' and the 'tag' appropriately

import csv
try:
    import ConfigParser
except:
    import configparser as ConfigParser
import sys

from threatconnect import ThreatConnect

config = ConfigParser.RawConfigParser()
config.read("./tc.conf")

try:
    api_access_id = config.get('threatconnect', 'api_access_id')
    api_secret_key = config.get('threatconnect', 'api_secret_key')
    api_default_org = config.get('threatconnect', 'api_default_org')
    api_base_url = config.get('threatconnect', 'api_base_url')
except ConfigParser.NoOptionError:
    print('Could not read configuration file.')
    sys.exit(1)
tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)

# instantiate Indicators injest function
# This is the main function - all the shit happens in here - be careful when editing!

def tc_ingest(*varargs):
    indicators = tc.indicators()
    # Define the 'owner' here - this where the IOCs are going under
    owner = raw_input("Enter the owner:")
    # create a new Indicator in the given owner
    indicator = indicators.add(new_indicator, owner)
    # add a description attribute
    indicator.add_attribute('Description', raw_input("Enter description:"))
    # set the confidence rating for the Indicator
    indicator.set_confidence(50)
    # set the threat rating for the Indicator
    indicator.set_rating(raw_input("Enter rating (1-5):"))
    # add a tag - be careful, this is kinda real important
    indicator.add_tag(raw_input("Enter tag:"))
    # add a security label
    indicator.set_security_label(raw_input("Enter security label (eg. TLP Green):"))
    try:
        # create the Indicator
        indicator.commit()
        return
    except RuntimeError as e:
        print('Error: {0}'.format(e))
        sys.exit(1)
with open(raw_input("Enter the CSV absolute path:"),'r') as csvFile:
    reader=csv.reader(csvFile,delimiter=',')
    reader.next()
    for row in reader:
        new_indicator = (row[0])
        tc_ingest()
        print("IOCs added successfully. Exiting now.")
exit()
