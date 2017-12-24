#Checks how many headers has Nulls
def check_Nulls(collection):
    document = collection.find_one()
    print('total\t',collection.count())
    for header in document:
        filter = {header: None}
        print(header,'\t',collection.count(filter))
    return


#Checks how many headers has String Type
def check_Strings(collection):
    print('total\t',collection.count())
    document = collection.find_one()
    for header in document:
        filter = {header: {'$type': 2}}
        print(header,'\t',collection.count(filter))
    return

