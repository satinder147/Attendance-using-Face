
from pymongo import MongoClient
client=MongoClient()
db=client.dbms

s=db.col.find()
l=[]
for i in s:
    l.append(i)
print(l)
