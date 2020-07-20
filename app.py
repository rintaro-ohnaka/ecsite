# coding:utf-8

from flask import Flask, flash, request, redirect, render_template
app = Flask(__name__)
from mysql.connector import errorcode

def get_connection():
    cnx = mysql.connector.connect(host=DB["DB_HOST"], user=DB["DB_USER_NAME"], password=DB["DB_PASSWORD"], database=DB["DB_NAME"])
    cursor = cnx.cursor()
    return cursor, cnx

@app.route("/", methods=["GET", "POST"])
def create_user():
    user_name = request.form.get("user_name", "")
    user_mail = request.form.get("user_mail", "")
    user_pass = request.form.get("user_pass", "")

    get_user_registration_query = "INSERT"

    return render_template("user_registration.html")

@app.route("/login", methods=["GET", "POST"])
def login_user():
    return render_template("login.html")