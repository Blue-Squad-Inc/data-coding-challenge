from pymongo import MongoClient

class Mongo:
    def __init__(self, host, port, username, password, database):
        self.connection_args = {
            'host': host,
            'port': port,
            'username': username,
            'password': password,
            'authSource': database
        }
        self.database = database
        
        self.connection = MongoClient(**self.connection_args)

    def get_db_connection(self):
        return self.connection[self.database]
    
    def disconnect(self):
        self.connection.close()