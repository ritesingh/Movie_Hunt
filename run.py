from flask import Flask,render_template,request,redirect,url_for
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def index():
   db=MongoClient().database
   data=db.test
   cursor=data.find()
   list1=[]
   for movie in cursor:
      list1.append(movie)
   
   return render_template("index.html",lists=list1)

@app.route("/movie",methods=['GET','POST'])
def movie():
   if request.method=="POST":
      idm=request.form["movies_name"]
   db=MongoClient().database
   data=db.test
   cursor=data.find({'name':idm})
   dictm={}
   flag=0
   for i in cursor:
      dictm["name"]=i["name"]
      dictm["rating"]=i["rating"]
      dictm["releasing_year"]=i["releasing_year"]
      dictm["cast"]=i["cast"]
      flag=1
   if(flag==0):
      return render_template("error.html")
   else:
      return render_template("movie.html",**dictm)
   


if __name__ == '__main__':
   app.run(debug = True)

