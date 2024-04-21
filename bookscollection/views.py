from django.shortcuts import render
from pymongo import MongoClient
from django.http import HttpResponse, HttpResponseRedirect
from .models import BookOperations 

def home(request):
    return render(request,"index.html")

def loginpage(request):
    return render(request,"login.html")


def login(request):
    page=None
    if request.method=="POST":
        id=request.POST.get("uid")
        ps=request.POST.get("psw")
        obj=BookOperations()
        page=obj.checkuser(id,ps)       
    return render(request, page)

def registerpage(request):
    return render(request,"Register.html")
   
def register(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        uid=request.POST.get("uid")
        psw=request.POST.get("psw")
        
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
            return HttpResponseRedirect("/loginpage/")
        
    return HttpResponse("Method not allowed.")



def searchbook(request):
     return render(request,"Searchbook.html")

def searchbookonid(request):
    if request.method=="POST":
        bid=request.POST.get("bookid")
        dic={'id':bid}        
        client=MongoClient("mongodb+srv://dbrokade:dnyan2399@dnyancluster.mf0zeqn.mongodb.net/?retryWrites=true&w=majority&appName=DnyanCluster")
        db=client["dnyandb"]
        coll=db["books"]

        book=coll.find_one(dic)
        def sample(request): 
            if request.method != "POST":       
                return render(request,"Booksearchdata.html")
            else:
                return render(request,"failure.html")
            
    return render(request,"Booksearchdata.html",book)


def searchid(request):
     return render(request,"Searchbook.html")

def adminpage(request):
    return render(request,"Admin.html")

def addbookpage(request):
    return render(request,"Addbook.html")

def addbook(request):
    if request.method=="POST":
       id=request.POST.get('id')
       title=request.POST.get('title')
       author=request.POST.get('author')
       genre=request.POST.get('genre')
       published_year=request.POST.get('published_year')
       isbn=request.POST.get('isbn')
       pages=request.POST.get('pages')
       language=request.POST.get('language')
       publisher=request.POST.get('publisher')
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
    return render(request,"Admin.html")

def deletebook(request):
    if request.method=="POST":
        bid=request.POST.get("bookid")
        dic={}
        dic['id']=bid
        print(dic)
        client=MongoClient("mongodb+srv://dbrokade:dnyan2399@dnyancluster.mf0zeqn.mongodb.net/?retryWrites=true&w=majority&appName=DnyanCluster")
        db=client["dnyandb"]
        coll=db["books"]
        coll.delete_one(dic)
    return render(request,"deletebook.html")

def all_books(request):
    obj = BookOperations()
    data = obj.get_all_books()
    return render(request, "showallbooks.html", {'bookdata': data})


def searchforupdate(request):
    return render(request,"searchforupdate.html")

def searchupdatebookonid(request):
    if request.method=="POST":
        bid=request.POST.get("bookid")
        dic={}
        dic['id']=bid
        print(dic)
        client=MongoClient("mongodb+srv://dbrokade:dnyan2399@dnyancluster.mf0zeqn.mongodb.net/?retryWrites=true&w=majority&appName=DnyanCluster")
        db=client["dnyandb"]
        coll=db["books"]
        for book in coll.find(dic):
            print(book)
    
    return render(request,"bookupdatedata.html",book)

def updateform(request):
    return render(request,"updatebookform.html")
    

def update(request):
    if request.method=='POST':
        bid=request.POST.get("bookid")
        title=request.POST.get('title')
        author=request.POST.get('author')
        genre=request.POST.get('genre')
        published_year=request.POST.get('published_year')
        isbn=request.POST.get('isbn')
        pages=request.POST.get('pages')
        language=request.POST.get('language')
        publisher=request.POST.get('publisher')
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
    return render(request,"Admin.html")

        
        


   

    








            
