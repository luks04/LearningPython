from pymongo import MongoClient
from pymongo.collection import Collection

def connect(db_name):
    try:
        client = MongoClient("mongodb+srv://admin:admin@learning-cluster.dkrsz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        return client[db_name]
    except Exception as error:
        print("Error: ", error)

def drop_collection(collection: Collection):
    try:
        collection.drop()
    except Exception as error:
        print("Error: ", error)

if __name__ == "__main__":
    conn = connect('LearningDB')
    drop_collection(conn['users'])