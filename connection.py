import pymongo

client = pymongo.MongoClient()
mydb = client["Bilingsystem"]
mycol = mydb["admin"]
menucol = mydb["orders"]
