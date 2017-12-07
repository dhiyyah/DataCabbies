import csv
import json

csvfile = open('green_tripdata_2014-04.csv', 'r')
jsonfile = open('green_tripdata_2014-04.json', 'w')

fieldnames = ("VendorID","lpep_pickup_datetime","Lpep_dropoff_datetime","Store_and_fwd_flag",
"RateCodeID","Pickup_longitude","Pickup_latitude","Dropoff_longitude",
"Dropoff_latitude","Passenger_count","Trip_distance","Fare_amount",
"Extra","MTA_tax","Tip_amount","Tolls_amount","Ehail_fee","Total_amount","Payment_type","Trip_type")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
  json.dump(row, jsonfile)
  jsonfile.write('\n')