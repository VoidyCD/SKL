from pymongo import MongoClient
from gridfs import GridFS
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

# Download the Python file




# Connect to the MongoDB server
uri = "mongodb+srv://SKL-USER:mGKEgzZbcUPu2iwM@skl.jdigidi.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

database = client.get_database("SKL-Keys")

fs = GridFS(database)
collection = database["python-file"]

with open('Logger.py', 'rb') as f:
    file_id = fs.put(f, filename='Logger.py')
    
    
# Download the Python file

with open('cock.py', 'wb') as f:
    f_id = ObjectId("64e64b0bc289ef903ecf669b")
    file = fs.get(file_id)
    f.write(file.read())

print("File downloaded from MongoDB.")

print("File uploaded to MongoDB.")


