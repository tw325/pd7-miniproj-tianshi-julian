from flask import Flask, render_template, request

import utils

app = Flask(_name_)

@app.route("/", methods = ["GET", "POST"])
@app.route("/home", methods = ["GET","POST"])
def home():
    #

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method=="POST":
        return render_template("login.html",
    
@app.route("/register", methods = ["GET", "POST"])
def register():
    #

@app.route("/logout", methods = ["GET"])
def logout():
    #

if _name_=="_main_":
    app.debug=True
    app.run()
