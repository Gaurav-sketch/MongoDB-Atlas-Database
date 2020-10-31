# MongoDB-Atlas-Database
<img src = "https://techcrunch.com/wp-content/uploads/2019/06/MongoDB_Logo_FullColorBlack_RGB.png" />

Work on MongoDB Atlas Database( NoSQL) using Python

MySQL: In MySQL if you want to add more feature -lot of structuring , schema is srict in MySQL 

MongoDB:Schema is dynamic , data stored in document form , JSON document (Key : Value pair) , the retrieval is very fast 
if we have collection of student , add property to it .This is dynamic schema ,This supports GEO Spatial query , this GIO location means longitude and latitude
,also cover radius using 5KM say.This is amazing.

It can also integrated with BIG DATA Hadoop MapReduce(map data and reduce in some fromat , kinda reduce) , MongoDB has this property inside it, Since data is stored in document based approach
the way of query is powerful as Mysql , this MangoDB is highly scalable .
JavaScript Object Notation - JSON
Limitation of MangoDB:
High Transaction - dont use MongoDB schema as it is not fixed , always use strict schema 


MongoDB Compass:

Install MongoDB Community server :
once mongodb installed , create database through command prompt , through Mongo prompt , what is being stored in the database , can be seen through MongoDB compass
mongodb://127.0.0.1:27017

How you can do it with MongoDB Shell
->Creating Databases , Inserting records and fetching details.
In SQL ->Database->tables->Add records
In MongoDB -> Database->Collection ->JSON Documents

db.collection.insertOne({"key":"value","key":"value"})

***More than 1 record*** 
db.collection.insertMany :This will create that many Object ID

db.collection.find({}) Select * from tablename

db.collection.find({"Key":"Value"}) , SElect * fRom table where

MongoDB as a service is hosted on the Cloud 
So many Cloud platforms are there , and these databases can be hosted there as Database as a service 
This is a free version of MongoDB Atlas using to just practice but the companies take the paid version of it .
There will be cluster of databases , and based on the query/traffic you will see that from which database the results are coming. 
You can use it in Azure , AWS and Google Cloud Platform.
This database is handled by these cloud platforms , handles scalability , database and other configurations,also handles data security.Physical software , hardware not required then.
Shared Cluster : This will create cluster of Databases
