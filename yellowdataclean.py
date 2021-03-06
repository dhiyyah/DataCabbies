# Use the below code for Cleaning yellow data set january 2017:

import pandas as pd
def readCSVFile( fileName, numberofRows):

#read CSV File and save to dataframe
df = pd.read_csv('yellow_tripdata_2017-01.csv', nrows=10)
#remove any space from column name
df.columns = df.columns.str.replace('\s+','')
return df
def green_removeColumn(df):
df.drop('VendorID', axis=1, inplace = True)
df.drop('store_and_fwd_flag', axis=1, inplace = True)
df.drop('RatecodeID', axis=1, inplace = True)
df.drop('extra', axis=1, inplace = True)
df.drop('mta_tax', axis=1, inplace = True)
df.drop('tolls_amount', axis=1, inplace = True)
df.drop('improvement_surcharge', axis=1, inplace = True)
df.drop('payment_type', axis=1, inplace = True)
df.drop('tip_amount', axis=1, inplace = True)
return df
fileName = 'yellow_tripdata_2017-01.csv'
numberofRows = 10
data = readCSVFile( fileName, numberofRows)
data = green_removeColumn(data)
print(data)
