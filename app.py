from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import Append
import datetime
from pymongo import MongoClient
from random import randint

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/register", methods=["POST","GET"])
def register():
        if (request.method == "GET"):
                return render_template("register.html")
        else:
                username = request.form["username"]
                password = request.form["password"]
                if Append.validuname(username):
                        error = "Username already exists. Please try again."
                        return render_template("register.html", err = error)
                else:
                        Append.register(username,password)
                        return redirect(url_for("login"))

@app.route("/login", methods = ["POST", "GET"])
def login():
	if (request.method == "GET"):
		return render_template("login.html")
	else:
		username = request.form["username"]
		password = request.form["password"]
		session['username'] = request.form["username"]
                if (Append.authenticate(username, password)):
                        session['n']=username
                        return redirect(url_for("storypage"))
                else:
                        error = "Your Username or Password is incorrect. Please try again."
                        return render_template("login.html", problem = error )
	
@app.route("/storypage", methods=["POST","GET"])
def storypage():
    connection = MongoClient()
    db = connection['StoryBase']
    if (request.method == "POST"):
    	Append.comment(request.form["button"],request.form["comment"],datetime.date.today().strftime("%B %d, %Y"))
    #connectionComments = MongoClient()
    #dbComments = connectionComments['Comments']
    MainHTML = ""
    result = Append.getStory()
    for r in result:
        print r["uname"]
    	StoryHTML = """ 
	<table>
	  <tr>
	    <td style="font-size:200%"> """ + r["title"] + """
	    </td> <td style="font-size:150%">
	    by """+r["uname"]+"""
	    </td> <td style="font-size:150%"> on """ + r["date"] +"""
	    </td> 
	  </tr><tr style="font-size:120%">
	    <td colspan="3">
            """+ r["content"] + """
	    </td>
	  </tr>
	</table>
        <hr> 
        <form method="POST">
        Add a Comment: <input type="text" name="comment">
        <button type="submit" name="button" value=%s>Submit</button>
        </form>
        Comments: <br><hr>""" % (r["storyID"])
        print r["storyID"]
        coms = Append.getCommentsSpec(str(r["storyID"]))
        MainHTML = MainHTML + StoryHTML
    	for y in coms:
                print y["CContent"]
    		commentHTML = '<p style="font-size:70%">'
    		commentHTML += """
    		%s <span style="color: #ff0000"> on %s </span>
                <hr>
                """ % (y["CContent"],y["Date"])
		commentHTML += "</p>"
		MainHTML = MainHTML + commentHTML
    return render_template("storypage.html", result=MainHTML)

@app.route("/addStory",methods=["GET","POST"])
def addStory():
        connection = MongoClient()
        db = connection['StoryBase']
        if 'n' not in session:
                return redirect("/login")
        if (request.method=="GET"):
                return render_template("addStory.html")
        else:
                Story = request.form["Story"]
                Title = request.form["Title"]
                ID = 0
                curs = db.stories.find()
                ID = curs.count()
                Append.addStory(ID,Story,Title,session['n'],datetime.date.today().strftime("%B,%d,%Y"))
                return redirect(url_for("storypage"))
                
if (__name__ == "__main__"):
        app.debug = True
        app.secret_key = "secret"
        app.run(host='0.0.0.0', port=8000)
