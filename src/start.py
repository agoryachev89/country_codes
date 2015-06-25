import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.mopub

with open('countries.json') as data_file:
    data = json.load(data_file)

for obj in data:
    db.countries.insert(obj)

print "success"
