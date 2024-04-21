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
    
    
    def reguser(self,fname,lname,uid,psw):
        client=MongoClient("mongodb+srv://dbrokade:dnyan2399@dnyancluster.mf0zeqn.mongodb.net/?retryWrites=true&w=majority&appName=DnyanCluster")
        db=client["dnyandb"]
        coll=db["registeruser"]
        existing_user=coll.find_one({"uid": uid})
        if existing_user:
            return HttpResponse("User already exists!")
        else:
            new_user = {
                "fname": fname,
                "lname": lname,
                "uid": uid,
                "psw": psw
            }
            coll.insert_one(new_user)
            return
        
    def addnewbook(self,id,title,genre,author,published_year,isbn,pages,language,publisher):
        client=MongoClient("mongodb+srv://dbrokade:dnyan2399@dnyancluster.mf0zeqn.mongodb.net/?retryWrites=true&w=majority&appName=DnyanCluster")
        db=client["dnyandb"]
        coll=db["books"]
        dic={}
        dic['id']=id
        dic['title']=title
        dic['genre']=genre
        dic['author']=author
        dic['published_year']=published_year
        dic['isbn']=isbn
        dic['pages']=pages
        dic['language']=language
        dic['publisher']=publisher
        coll.insert_one(dic)
        return
    
    def updatedata(self,bid,title,genre,author,published_year,isbn,pages,language,publisher):
        client=MongoClient("mongodb+srv://dbrokade:dnyan2399@dnyancluster.mf0zeqn.mongodb.net/?retryWrites=true&w=majority&appName=DnyanCluster")
        db=client["dnyandb"]
        coll=db["books"]
        dic={}
        dic['id']=bid

        ch={}
        ch["title"]=title
        ch['genre']=genre
        ch['author']=author
        ch['published_year']=published_year
        ch['isbn']=isbn
        ch['pages']=pages
        ch['language']=language
        ch['publisher']=publisher

        upd={'$set':ch}
        coll.update_one(dic,upd)
        return
    
    

