import pymongo
import urllib


class Database:

    DATABASE = 'trufla'
    URL = f'mongodb://trufla_admin:P%40ssw0rd@localhost:27017/'

    def __init__(self):
        self.conn = pymongo.MongoClient(self.URL)
        self.db = self.conn[self.DATABASE]

    def insert(self, files_content, collection):

        for f_content in files_content:

            self.db[collection].insert(f_content)


