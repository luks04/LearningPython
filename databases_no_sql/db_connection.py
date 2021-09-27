from pymongo import MongoClient

def connect():
    try:
        client = MongoClient("mongodb+srv://admin:admin@learning-cluster.dkrsz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db_name = 'LearningDB'
        if db_name in client.list_database_names():
            print('Database already exists')
            db = client[db_name]
            collection_name = 'users'
            if collection_name in db.list_collection_names():
                print('Collection already exists')
    except Exception as error:
        print("Error: ", error)

if __name__ == "__main__":
    connect()