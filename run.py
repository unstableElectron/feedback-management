from flask import Flask
from flask import render_template, request, redirect
from flask.wrappers import Request
from db import query_util

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/signup")
def signup():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    form = request.form

    username = form["username"]
    email = form["email"]
    password = form.get("password")
    pincode = form.get("pincode")

    sql = "insert into people(name,email,pincode,password) values(%s, %s, %s, %s)"

    query_util.execute(sql, (username, email, password, pincode))

    print(username, email, password, pincode)

    return render_template("index.html", feedback="Something is wrong!")
    # return redirect("/signup")


if __name__ == "__main__":
    app.run()
