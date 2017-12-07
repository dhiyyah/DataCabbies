import csv
import json

csvfile = open('yellow_tripdata_2014-04.csv', 'r')
jsonfile = open('yellow_tripdata_2014-04.json', 'w')

fieldnames = ("vendor_id","pickup_datetime","dropoff_datetime","passenger_count",
"trip_distance","pickup_longitude","pickup_latitude","rate_code",
"store_and_fwd_flag","dropoff_longitude","dropoff_latitude","payment_type",
"fare_amount","surcharge","mta_tax","tip_amount","tolls_amount","total_amount")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')