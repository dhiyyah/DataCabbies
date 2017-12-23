#from string to datetime, float, int
def convert_from_string(date_format, collection):
    cursor = collection.find()
    for record in cursor:
        passenger_count = int(record['passenger_count'])
        trip_distance = float(record['trip_distance'])
        total_amount = float(record['total_amount'])
        pickup_datetime = datetime.strptime(record['pickup_datetime'],date_format)
        dropoff_datetime = datetime.strptime(record['dropoff_datetime'],date_format)
        collection.update_one({'_id':record['_id']},\
                              {'$set':{'passenger_count' : passenger_count,\
                                       'trip_distance' : trip_distance,\
                                       'total_amount' : total_amount,\
                                       'pickup_datetime' : pickup_datetime,\
                                       'dropoff_datetime' : dropoff_datetime}})
    return



#from datetime, float, int to string
def convert_to_string(date_format, collection):
    cursor = collection.find()
    for record in cursor:
        passenger_count = str(record['passenger_count'])
        trip_distance = str(record['trip_distance'])
        total_amount = str(record['total_amount'])
        pickup_datetime = datetime.strftime(record['pickup_datetime'],date_format)
        dropoff_datetime = datetime.strftime(record['dropoff_datetime'],date_format)
        collection.update_one({'_id':record['_id']},\
                              {'$set':{'passenger_count' : passenger_count,\
                                       'trip_distance' : trip_distance,\
                                       'total_amount' : total_amount,\
                                       'pickup_datetime' : pickup_datetime,\
                                       'dropoff_datetime' : dropoff_datetime}})
    return


#date_format = '%Y-%m-%d %H:%M:%S'
#collection = db['sy_apr-14']
#convert_to_string(date_format, collection)
#collection.find_one()
#convert_from_string(date_format, collection)
#collection.find_one()