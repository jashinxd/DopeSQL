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
    if (request.method == "POST"):
    	Append.comment(request.form["button"],request.form["comment"],datetime.date.today().strftime("%B %d, %Y"))
    connection = MongoClient()
    db = connection['StoryBase']
    connectionComments = MongoClient()
    dbComments = connectionComments['Comments']
    MainHTML = ""
    result = Append.getStory()
    for r in result:
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
        <input type="submit" name="button" value=%s>
        </form>
        Comments: <br><hr>""" % (r["uname"])
        comments = Append.getComments()
    	for y in comments:
    		StoryHTML += '<p style="font-size:70%">'
    		commentHTML = """
    		%s <span style="color: #ff0000"> on %s </span>
                <hr>
                """ % (y["CContent"],y["Date"])
		commentHTML += "</p>"
    		StoryHTML = StoryHTML + commentHTML
		MainHTML = MainHTML + StoryHTML    		
    return render_template("storypage.html", result=MainHTML)

@app.route("/addStory",methods=["GET","POST"])
def addStory():
        if 'n' not in session:
                return redirect("/login")
        if (request.method=="GET"):
                return render_template("addStory.html")
        else:
                Story = request.form["Story"]
                Title = request.form["Title"]
                
                Append.addStory(Story,Title,session['n'],datetime.date.today().strftime("%B,%d,%Y"))
                return redirect(url_for("storypage"))
                
if (__name__ == "__main__"):
        app.debug = True
        app.secret_key = "secret"
        app.run(host='0.0.0.0', port=8000)
