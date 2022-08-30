from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

class DatabaseManager:
    def start(self):
        try:
            client  = MongoClient(config["DB_CONN_STRING"])
            print("Database Connected successfully!!!")
            return client[config['DB_NAME']]
        except:
            print("Could not connect to MongoDB")

    