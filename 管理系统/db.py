import pymongo


class DB_Utils:
    def __init__(self):
        self.db = pymongo.MongoClient("www.4yewu.cn", 27017)['classmates']
