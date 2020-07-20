# coding:utf-8

from flask import Flask, flash, request, redirect, render_template, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ecsite'
from mysql.connector import errorcode
import mysql.connector
from model.const import DB
from model.user import User

# DBに接続
def get_connection():
    cnx = mysql.connector.connect(host=DB["DB_HOST"], user=DB["DB_USER_NAME"], password=DB["DB_PASSWORD"], database=DB["DB_NAME"])
    cursor = cnx.cursor()
    return cursor, cnx

# アカウント新規作成ページを表示
@app.route("/", methods=["GET", "POST"])
def show_user_registration_page():
    flash("ようこそ、新規登録ページへ")
    return render_template("user_registration.html")

# ユーザー登録リクエストを受ける
def user_registration_request():
    user_name = request.form.get("user_name", "")
    user_pass = request.form.get("user_pass", "")
    return user_name, user_pass

# アカウント名とパスワードが正しく入力されているかチェック
def is_valid_registration_request(user_name, user_pass):
    cursor, cnx = get_connection()
    if user_name == "" or user_pass == "":
        flash("アカウント名とパスワードを入力してください", "")
    else:
        get_user_registration_query = f"INSERT INTO user_table (user_name, password) VALUES ('{user_name}', '{user_pass}') "
        cursor.execute(get_user_registration_query)
        cnx.commit()
        flash("アカウント作成に成功しました")

# 新規アカウント作成
@app.route("/create_user", methods=["GET", "POST"])
def create_user():
    user_name, user_pass = user_registration_request()
    is_valid_registration_request(user_name, user_pass)

    return redirect("/")

# ログインページを表示
@app.route("/show_login_page", methods=["GET", "POST"])
def show_login_page():
    return render_template("login.html")

# ログインに成功したら、user_management、失敗ならredirect
@app.route("/login", methods=["GET", "POST"])
def login_user():
    cursor, cnx = get_connection()
    user_name = request.form.get("user_name", "")
    user_pass = request.form.get("user_pass", "")

    get_user_information_query = f"SELECT user_name, password FROM user_table WHERE user_name = '{user_name}' AND password = '{user_pass}' "
    cursor.execute(get_user_information_query)
    
    login_user = []
    for (user_name, password) in cursor:
        profile = User(user_name, password)
        login_user.append(profile)

    is_valid_login_user(user_pass, user_name, login_user)
    return render_template("user_management.html", login_user=login_user)

# アカウント名とパスワードが正しく入力されているかのチェック
def is_valid_login_user(user_pass, user_name, login_user):
    if user_pass == "" or user_name == "":
        flash("アカウント名とパスワードを入力してください")
    elif len(login_user) == 0:
        flash("アカウント名かパスワードが間違っています", "")
    else:
        flash("ログイン成功！", "")
    