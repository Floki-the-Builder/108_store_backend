import pymongo


import pymongo
import certifi


con_str = 'mongodb+srv://ardany:RAMazon66@cluster0.5iuoemr.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("SouthpawStore")
