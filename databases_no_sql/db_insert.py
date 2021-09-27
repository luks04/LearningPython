from pymongo import MongoClient
from pymongo.collection import Collection

def connect(db_name):
    try:
        client = MongoClient("mongodb+srv://admin:admin@learning-cluster.dkrsz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        return client[db_name]
    except Exception as error:
        print("Error: ", error)

def insert_to_collection(collection: Collection, new_user: dict):
    try:
        collection.insert_one(new_user)
    except Exception as error:
        print("Error: ", error)

if __name__ == "__main__":
    conn = connect('LearningDB')
    new_user = {'name': 'Frank', 'phone': '3132332997'}
    insert_to_collection(conn['users'], new_user)