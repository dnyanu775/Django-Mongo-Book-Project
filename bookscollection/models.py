from pymongo import MongoClient

class BookOperations:
    def checkuser(self,id,ps):
        client=MongoClient("mongodb+srv://dbrokade:dnyan2399@dnyancluster.mf0zeqn.mongodb.net/?retryWrites=true&w=majority&appName=DnyanCluster")
        db=client["dnyandb"]
        coll=db["registeruser"]
        user=coll.find_one({"uid": id, "psw": ps})
        if user:
            page="Admin.html"
        else:
            page="failure.html"
        return page


    def __init__(self):
        self.client = MongoClient("mongodb+srv://dbrokade:dnyan2399@dnyancluster.mf0zeqn.mongodb.net/?retryWrites=true&w=majority&appName=DnyanCluster")
        self.db = self.client["dnyandb"]
        self.coll = self.db["books"]
    def get_all_books(self):
        data = self.coll.find()
        return data
    
    
    

