import pandas as pd
import sys
from pprint import pprint

fileName = sys.argv[1] 
numberOfRows = 10
#fileName = 'yellow_tripdata_2014-04.csv'
df = pd.read_csv(fileName, nrows = numberOfRows)
#df = pd.read_csv(fileName)
colcount = 0
for i in df.columns.values: 
    print(colcount,'\t',i)
    colcount+=1




'''
Note that for green taxi dataset, we have to remove all these columns
{
'VendorID',
'store_and_fwd_flag',
'RatecodeID',
'extra',
'mta_tax',
'tolls_amount',
'ehail_fee',
'improvement_surcharge',
'payment_type',
'trip_type',
'tip_amount'
}
and for yellow taxi dataset 
{
  'VendorID',
  'store_and_fwd_flag',
  'RatecodeID',
  'extra',
  'mta_tax',
  'tolls_amount',
  'improvement_surcharge',
  'payment_type',
  'tip_amount',
}
Finally, U
'''