import csv
import json

csvfile = open('uber-raw-data-apr14.csv', 'r')
jsonfile = open('uber-raw-data-apr14.json', 'w')

fieldnames = ("Date/Time","Lat","Lon","Base")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')