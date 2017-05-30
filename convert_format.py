#!/usr/bin/env python
# Shodan IOC downloader for malware
# Vishal Thakur
# Released under MIT license
# This script converts the Shodan report into a new CSV with one column that has the indicators only.
# Useful for ingesting the IOCs into other platforms such as ThreatConnect
import csv
File1='malware-report.csv'
File2='change-my-name.csv'
outdata=[]
input_file=open(File1,'rb')
output_file=open(File2, 'wb')
reader=csv.reader(input_file, delimiter=',')
writer=csv.writer(output_file,delimiter=',')
for row in reader:
    print("row: ", row)
    outdata.append([row[3]])
print(outdata)
writer.writerows(outdata)
exit()


