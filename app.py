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
    return render_template("landing.html")



@app.route("/register.html", methods=["GET", "POST"])
def register():        
    return render_template("register.html")


@app.route("/create.html", methods=["GET", "POST"])
def create():
    return render_template("create.html")


@app.route("/edit.html", methods=["GET", "POST"])
def edit():
    return render_template("edit.html")


@app.route("/profile.html", methods=["GET", "POST"])
def profile():
    return redirect(url_for("landing"))


@app.route("/logout")
def logout():
    return redirect(url_for("landing"))


@app.route("/tavern.html")
def tavern():
    return render_template("tavern.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)