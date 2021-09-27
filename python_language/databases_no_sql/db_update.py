from pymongo import MongoClient
from pymongo.collection import Collection

def connect(db_name):
    try:
        client = MongoClient("mongodb+srv://admin:admin@learning-cluster.dkrsz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        return client[db_name]
    except Exception as error:
        print("Error: ", error)

def update_record(collection: Collection, new_user_data: dict):
    try:
        where = { "name": { "$regex": "^F" } }
        collection.update_one(where, { "$set": new_user_data })
    except Exception as error:
        print("Error: ", error)

if __name__ == "__main__":
    conn = connect('LearningDB')
    new_user_data = {'name': 'Frank Martinez Pedraza'}
    update_record(conn['users'], new_user_data)