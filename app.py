from logging import debug
import os
import re
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import pymongo
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
        returning_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if returning_user:
            if check_password_hash(
                returning_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash ("Welcome to the Tavern, {}".format(request.form.get("username")))
                    return redirect(url_for("tavern"))
            else:
                flash("Username and/or Password Incorrect. Please try again.")
                return redirect(url_for("landing", username=session["user"]))

        else:
            flash("Username and/or Password Incorrect. Please try again.")
            return redirect(url_for("landing"))
            
    return render_template("landing.html")



@app.route("/register.html", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        returning_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        returning_email = mongo.db.users.find_one(
            {"email": request.form.get("email")})
        if returning_user:
            flash("Username already in use")
            return redirect(url_for("register"))
        if returning_email:
            flash("Email already in use")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Thank you for registering with us!")
        return redirect(url_for("profile.html", username=session["user"]))
            
    return render_template("register.html")


@app.route("/create")
def create():
    if request.method =="POST":
        character = {
            "character_name": request.form.get("character_name"),
            "character_race": request.form.get("character_race"),
            "character_class": request.form.get("character_class"),
            "character_likes": request.form.get("character_likes"),
            "character_dislikes": request.form.get("character_dislikes"),
            "character_bio": request.form.get("character_bio"),
        }
        mongo.db.characters.insert_one(character)
        flash("{{ character_name }} Added")
        return redirect(url_for("profile"))


    races = mongo.db.races
    races_list = races.find().sort("race_name", 1)

    classes = mongo.db.classes
    classes_list = classes.find().sort("class_name", 1)
    
    return render_template("create.html", races_list=races_list, classes_list=classes_list)


@app.route("/edit")
def edit():
    return render_template("")


@app.route("/profile.html", methods=["GET", "POST"])
def profile():
    if session.get("user"):
        return render_template("profile.html", username=session["user"])

    return redirect(url_for("landing"))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("landing"))


@app.route("/tavern.html")
def tavern():
    characters = list(mongo.db.characters.find())
    return render_template("tavern.html", characters=characters)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)