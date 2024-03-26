MongoDB and PyMongo Project

Welcome to the MongoDB and PyMongo project! This project is designed to enhance your understanding and proficiency in working with MongoDB, a popular NoSQL database, and PyMongo, the Python driver for MongoDB. Below, you will find detailed explanations of each task along with the requirements for completing them.
Overview

MongoDB is a document-oriented NoSQL database that provides high performance, high availability, and easy scalability. PyMongo is the official Python driver for MongoDB, allowing Python developers to interact with MongoDB databases efficiently.
Tasks
1. List all databases

Description: In this task, you will develop a script to retrieve a list of all databases present in the MongoDB server. This involves connecting to the MongoDB server and executing a command to list all databases.

Details: The script should establish a connection to the MongoDB server using PyMongo. Upon successful connection, it should execute a command to list all databases available on the server.
2. Create a database

Description: You will write a script to create a new database in MongoDB. This task involves establishing a connection to the MongoDB server and issuing a command to create a new database.

Details: The script should connect to the MongoDB server using PyMongo and specify the name of the new database to create. After establishing the connection, it should execute a command to create the specified database if it does not already exist.
3. Insert document

Description: Develop a script to insert a new document into a specified collection within a MongoDB database. This task requires establishing a connection to the MongoDB server, selecting the appropriate database and collection, and inserting a new document into the collection.

Details: The script should connect to the MongoDB server using PyMongo and select the target database and collection. It should then insert a new document into the selected collection, providing the necessary data for the document to be inserted.
4. List all documents

Description: Write a script to retrieve and display all the documents from a specific collection in the MongoDB database. This involves connecting to the MongoDB server, selecting the database and collection, and fetching all documents from the collection.

Details: The script should establish a connection to the MongoDB server using PyMongo and select the target database and collection. It should then fetch all documents from the selected collection and display them to the user.
5. List all documents with matching criteria

Description: Develop a script to list only the documents that match certain criteria specified by the user. This task requires querying the MongoDB collection with specific criteria and returning the matching documents.

Details: The script should prompt the user to enter the criteria for filtering documents. It should then connect to the MongoDB server using PyMongo, query the collection with the specified criteria, and return the matching documents.
6. Count documents

Description: Write a script to count the number of documents in a collection, either based on certain criteria or all documents. This task involves executing a count operation on the MongoDB collection and returning the total count of documents.

Details: The script should connect to the MongoDB server using PyMongo and select the target collection. It should then execute a count operation on the collection, optionally specifying criteria for filtering documents, and return the total count of documents.
7. Update documents

Description: Develop a script to update one or more existing documents in a collection. This task requires identifying the documents to update and applying the necessary modifications to them.

Details: The script should connect to the MongoDB server using PyMongo and select the target collection. It should then identify the documents to update, specify the modifications to be applied, and execute an update operation on the collection.
8. Delete documents

Description: Write a script to delete one or more documents from a collection based on certain criteria. This involves identifying the documents to delete and executing a delete operation on them.

Details: The script should connect to the MongoDB server using PyMongo and select the target collection. It should then identify the documents to delete based on specified criteria and execute a delete operation on the collection.
9. List all documents in Python

Description: Develop a Python script to connect to a MongoDB database and retrieve all documents from a specific collection. This task requires using PyMongo to establish a connection and fetch all documents from the collection.

Details: The script should use PyMongo to establish a connection to the MongoDB server and select the target database and collection. It should then fetch all documents from the selected collection and return them as Python objects.
10. Insert a document in Python

Description: Write a Python script to insert a new document into a MongoDB collection. This involves using PyMongo to establish a connection and insert a new document into the specified collection.

Details: The script should use PyMongo to connect to the MongoDB server and select the target collection. It should then insert a new document into the collection, providing the necessary data for the document to be inserted.
11. Update topics of a school document

Description: Develop a script to update the topics field of a specific document in a school collection. This task requires identifying the document by a unique identifier and updating its topics field.

Details: The script should connect to the MongoDB server using PyMongo and select the target collection. It should then identify the document to update based on a unique identifier, specify the new topics to be assigned, and execute an update operation on the collection.
12. Provide stats about Nginx logs stored in MongoDB

Description: Write a script to extract statistical information from Nginx logs stored in MongoDB, such as the number of requests, status codes, or IP addresses. This task involves querying the MongoDB collection containing Nginx logs and aggregating the required statistics.

Details: The script should connect to the MongoDB server using PyMongo and select the collection containing Nginx logs. It should then execute aggregation operations to calculate and return statistical information about the Nginx logs, such as the total number of requests, distribution of status codes, or top IP addresses.
13. List documents with name starting by Holberton

Description: Develop a script to retrieve all documents from a collection where the name field starts with "Holberton". This task involves querying the MongoDB collection with a regular expression to filter documents based on the name field.

Details: The script should connect to the MongoDB server using PyMongo and select the target collection. It should then query the collection with a regular expression to filter documents based on the name field starting with "Holberton" and return the matching documents.
14. Return all students sorted by average score

Description: Write a script to query a collection containing student data, calculate the average score for each student, and return the results sorted by the average score. This task involves aggregation operations to calculate the average score and sorting the results accordingly.

Details: The script should connect to the MongoDB server using PyMongo and select the collection containing student data. It should then execute aggregation operations to calculate the average score for each student and sort the results based on the average score.
15. Enhanced log stats with top 10 most present IPs

Description: Develop a script to enhance the statistical information from Nginx logs to include the top 10 most frequently occurring IP addresses. This task involves aggregating the IP addresses from the Nginx logs and selecting the top 10
