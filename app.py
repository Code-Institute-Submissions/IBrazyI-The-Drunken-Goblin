from logging import debug
import os
import re
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import pymongo
import cloudinary
import cloudinary.uploader
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)




@app.route("/")
@app.route("/landing.html", methods=["GET", "POST"])
def landing():
    if request.method == "POST":
        #Checking that Username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
                #Checking password entered matches
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                #Stores session"user" where the username is passed into the profile function
                return redirect(url_for('profile'))
                
            else:
                #Incorrect Password
                return redirect(url_for('landing'))

        else:
            return redirect(url_for('landing')) 

    return render_template(url_for('landing'))


@app.route("/register.html", methods=["GET", "POST"])
def register():        
    return render_template(url_for('register'))


@app.route("/create.html", methods=["GET", "POST"])
def create():
    return render_template(url_for('create'))


@app.route("/edit.html", methods=["GET", "POST"])
def edit():
    return render_template(url_for('edit'))



@app.route("/profile.html", methods=["GET", "POST"])
def profile():

    usercharacters = mongo.db.characters.find()

    return render_template(url_for('profile'), usercharacters=usercharacters)
    


@app.route("/tavern.html")
def tavern():

    characters = mongo.db.characters.find()

    return render_template('tavern.html', characters=characters)

# App Routes that require REDIRECT


@app.route("/logout")
def logout():

    session.pop("user")

    return redirect(url_for('landing'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)