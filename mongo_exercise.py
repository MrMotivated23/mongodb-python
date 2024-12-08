from pymongo import MongoClient
user = 'root'
password = 'vHxrZjxcE9xgCJxMgzYIunAs' # CHANGE THIS TO THE PASSWORD YOU NOTED IN THE EARLIER EXCERCISE - 2
host='mongo'
#create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)


connection = MongoClient(connecturl)

# Selecting the training database
db = connection.training

# Selecting the mongodb_glossary
collection = db.mongodb_glossary

list_of_inserts = [{"database": "a database contains collections"},
                   {"collection": "a collection stores the documents"},
                   {"document": "a document contains the data in the form of key value pairs."}
                   ]

# Inserting all the documents in the collection
for insertion in list_of_inserts:
    db.collection.insert_one(insertion)  

docs = db.collection.find()

print("Printing the documents in the collection.")

for document in docs:
    print(document)

# close the server connecton
print("Closing the connection.")
connection.close()





