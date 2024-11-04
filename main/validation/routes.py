from flask import request, render_template, redirect, Response
from .. import app
from .. import db

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pass"]
        user = db.Query(email=email).first()
        return "Hii"
    return render_template("./validation/login.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    return render_template("./validation/signup.html")