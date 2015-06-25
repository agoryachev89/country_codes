import json
from pymongo import MongoClient

db_countries = MongoClient('localhost', 27017).countries.countries

with open('countries.json') as data_file:
    data = json.load(data_file)

db_countries.insert_many(data, False)

print "success"
