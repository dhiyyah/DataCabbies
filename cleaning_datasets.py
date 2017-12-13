import pandas as pd
import json
import csv


class CSVfile:
	# read a specific rows 
	def readCSVFile(self,fileName,numberOfRows):
		# read csv file and save it as dataFram
		df = pd.read_csv(fileName,  nrows= numberOfRows)
		# remove any space from colum name
		df.columns = df.columns.str.replace('\s+', '') 
		return df
	# read all CSV file
	def readAllCSVFile(self,fileName):
		# read csv file and save it as dataFram
		df = pd.read_csv(fileName)
		# remove any space from colum name
		df.columns = df.columns.str.replace('\s+', '')  
		return df

	def removeColumn(self,df,list_column_name):
		counter =0
		for c in list_column_name:
			df.drop(df.columns[c-counter],axis=1,inplace=True)
			counter=counter+1
		return df

	def printHead(self,df):
		print(df.head())

	def summaryStatistics(self,df):
		print(df.describe())

	def printColumn_name(self,df):
		print(df.columns.values)

	def convertDataFrameToCSV(self,df):
		filename = 'temp.csv'
		return df.to_csv(filename)

	def convertFromDataFrame_To_Json(self,df,fileName):
		myJSON = df.to_json(path_or_buf = None, 
							orient = 'records',
							 date_format = 'epoch', 
							 double_precision = 10, 
							 force_ascii = True, 
							 date_unit = 'ms', 
							 default_handler = None)

		with open(f,"w+") as output_file:
			output_file.write(myJSON)

	def convertFromDataFrame_To_CSV(self,df,fileName):
		with open(fileName, 'a') as f:
			df.to_csv(f)

		


# this list will be changed depanding on the indexes which want to remove.
list_column_name_yellow = [0,7,8,11,16]
# Namber of rows which you want to read from CSV file  # Note that # you might want to read all csv file so you don't need this varible.
numberOfRows = 50
# a specific CSV file which you want to read it.
fileName_yellow = 'yellow_tripdata_2014-04.csv'
# creat object from class
object_yellow = CSVfile()
# convert CSV file to DataFram
# convert a specific rows of the CSV file
#data = object_yellow.readCSVFile(fileName_yellow,numberOfRows)
#or you can read all the file 
data = object_yellow.readAllCSVFile(fileName_yellow)
# Remove colums you don't need it 
data = object_yellow.removeColumn(data,list_column_name_yellow)
#check columns name in order to be sure you removed the specific columns
object_yellow.printColumn_name(data)
# creat varible for output file.
output_file= 'output.csv'
# convert dataFrame to CSV file and you can find  the file at the same folder.
object_yellow.convertFromDataFrame_To_CSV(data,output_file)


















