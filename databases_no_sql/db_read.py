from pymongo import MongoClient
from pymongo.collection import Collection

def connect(db_name):
    try:
        client = MongoClient("mongodb+srv://admin:admin@learning-cluster.dkrsz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        return client[db_name]
    except Exception as error:
        print("Error: ", error)

def read_collection(collection: Collection):
    try:
        rs = collection.find()
        # rs = collection.find().limit(10)
        for record in rs:
            print(record)
    except Exception as error:
        print("Error: ", error)

if __name__ == "__main__":
    conn = connect('LearningDB')
    read_collection(conn['users'])