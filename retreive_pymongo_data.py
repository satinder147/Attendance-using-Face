'''from pymongo import MongoClient

client=MongoClient()
db=client.dbms
x=db.col.find({'arrat':3})
y=[]
for s in x:
    y.append(s)
a=y[0]
s=a['arrat']
print(s)
final=[]
for i in s:
    final.append(float(i))
print(final)
sum=0

for i in final:
    sum=sum+i
print(sum)'''
from pymongo import MongoClient
client=MongoClient()
db=client.dbms

s=db.col.find()
l=[]
for i in s:
    l.append(i)
print(l)
