
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://sangamgowdahm24:sangam247@cluster0.i9pz1.mongodb.net/networksecurity?retryWrites=true&w=majority&authSource=admin"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)