# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 00:44:48 2020

@author: Gaurav Kumar
"""


import pymongo   #This will help to interact with MangoDB , Collection ,Database

client=pymongo.MongoClient('mongodb+srv://gaurav:456123@mydb.wlscn.mongodb.net/test')

mydb=client['Gaurav']
information = mydb.biodata
data={"Course":"Data Science","GPA":"3.76","Passion":"Hardworking"}

information.insert_one(data)

# As a list , multiple nested array has to be created 
add =[{"First":"Rohan","Second":"Dontknow"},{"First":"Sohan","Second":"Know"}]
information.insert_many(add)

# Select * from employee information
information.find({})

for i in information.find({}):
    print(i)
    
# Query the json dcoument based on equality condition 
for i in information.find({"First":"Rohan"}):
    print(i)
    
## Query documents using query operators ($in,$lt,$gt)

for j in information.find({"Second":{'$in':['Know','Dontknow']}}):
    print(j)

information.insert_one({"First":"Chintu","Last":"Soni","Age":"36"})
information.insert_one({"First":"Chintu","Last":"Verma","Age":"38"})

#Check for And and Query Operator 
for record in information.find({"First":"Chintu","Age":{'$gt':"35"}}):
                                print(record)

# This is for or condition                                 
for record in information.find({'$or':[{"First":"Chintu"},{"First":"Rohan"}]}):
                                print(record)

# Similarly for and condition
for record in information.find({'$and':[{"First":"Chintu"},{"Age":"36"}]}):
                                print(record)     
                                

# How to work with Nested Nested JSON documents
inventory=mydb.inventory
inventory.insert_many([{'item':'Roti','Rice':'Basmati','Paratha':{'In':'Aloo','Taste':'Paneer','ExtraIn':'Palak'}},
                       {'item':'Roti','Rice':'Basmati','Paratha':{'In':'Aloo','Taste':'Spicy','ExtraIn':'Palak'}},
                      {'item':'Fulka','Rice':'Basmati','Paratha':{'In':'Aloo','Taste':'Paneer','ExtraIn':'Daal'}}])

# Good query for nested documents 
for k in inventory.find({'Paratha':{'In':'Aloo','Taste':'Paneer','ExtraIn':'Palak'}}):
    print(k)
                                
                                
# Learning to update records JSON:
# MongoDb with python updating JSON document 
# Functions to discuss 
# update_one(),update_many(),replace_one()

import pymongo 
inventory.insert_many([{'item':'Jwara','Rice':'Sona','Paratha':{'In':'Aloo','Taste':'Paneer','ExtraIn':'Palak'}},
                       {'item':'Bazara','Rice':'Basmati','Paratha':{'In':'Ghobi','Taste':'Spicy','ExtraIn':'Palak'}},
                      {'item':'Makka','Rice':'normal','Paratha':{'In':'Mutter','Taste':'Paneer','ExtraIn':'Daal'}}])

for j in inventory.find({}):
    print(j)


# Try to update the records , this is how you update for nested Json
# Using the query operator to update the Data and time so as to see when the change was made
inventory.update_one(
 {"item":"Roti"},{"$set":{"Paratha.In":"Waste"},"$currentDate":{"lastModified":True}}  
    )

inventory.update_many({'item':'Roti'}, {"$set":{"Rice":"NewBasmati"}})

# Replace 
inventory.replace_one({"item":"Makka"},{"item":"Check","Must":{"Dekho":"Done"}})

# MongoDb avg,Sum and Product 
# First create the database 
medb=client['NStudent']
rec=medb.result
rec.insert_many([{"Name":"Gaurav","Subject":"Maths","Score":90},
                 {"Name":"Vipin","Subject":"Bio","Score":100},
                  {"Name":"Raj","Subject":"Probability","Score":80},
                   {"Name":"Sneh","Subject":"Psychology","Score":100}])


# Find Gaurav and Vipin total subjects 
total_sub=rec.aggregate([{"$group":{"_id":"$Name","Total":{"$sum":1}}}])

for i in total_sub:
    print(i)
 
# Use the aggregate and do the total 
# Scores based on the user    
total_subj=rec.aggregate([{"$group":{"_id":"$Name","Total":{"$sum":"$Score"}}}])  
    
for j in total_subj:
    print(j)
   
# Calculate the average score based on user 
# Just change the groupby function

total_subj=rec.aggregate([{"$group":{"_id":"$Name","Total_average":{"$avg":"$Score"}}}])  
    
for j in total_subj:
    print(j)  
    
 # To work on date time import Date time 
import datetime as datetime

### Create a new collection 
data=[{"item":"abc","price":5,"quantity":2,"date":datetime.datetime.utcnow()},
      {"item":"xyz","price":6,"quantity":3,"date":datetime.datetime.utcnow()},
      {"item":"abc","price":4,"quantity":6,"date":datetime.datetime.utcnow()}]    
    
mycollection=medb.sntores    
mycollection.insert_many(data)    

agg_result= mycollection.aggregate([{"$group":{"_id":"$item","avgamount":{"$avg":{"$multiply":["$price","$quantity"]}},"avgquant":{"$avg":"$quantity"}}}])

for h in agg_result:
     print(h)    
    
# Create Projects 
# Multiple records in data in the form of list should be given 
data=[{'item':'Jwara','Rice':'Sona','Paratha':{'In':'Aloo','Taste':'Paneer','ExtraIn':'Palak'}},
                       {'item':'Bazara','Rice':'Basmati','Paratha':{'In':'Ghobi','Taste':'Spicy','ExtraIn':'Palak'}},
                      {'item':'Makka','Rice':'normal','Paratha':{'In':'Mutter','Taste':'Paneer','ExtraIn':'Daal'}}]

che=medb.books
    
che.insert_many(data)

# This project is like a select fucnt
for r in che.aggregate([{"$project":{"Rice":1,"item":1}}]):
    print(r)


input("What is your name?")
a=int(input("Enter first number"))
b=int(input("Enter second number"))
sum=a+b
print("The sum is:",sum)







