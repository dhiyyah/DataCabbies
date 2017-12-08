import sys
import csv
import json

arguments = sys.argv[1:]
count = len(arguments)
if (count<1):
    sys.exit("csv filename needed")

csvfilename = arguments[0]
if (count<2):
    jsonfilename = csvfilename.replace(".csv", ".json")
else:
    jsonfilename = arguments[1]

csvfile = open(csvfilename, 'r')
jsonfile = open(jsonfilename, 'w')

# Pass field names from the script before this
#fieldnames = arguments[2]

reader = csv.DictReader( csvfile, fieldnames)
header_line = next(reader)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
print("Done")