from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

@app.route("/") # Define a rota para a página inicial
@app.route("/index")

# Connect to the SQLite database

def index():
    con = sql.connect("form_db.db")
    con.row_factory = sql.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM users")
    data=cur.fetchall()
    return render_template("index.html", datas=data)

@app.route("/add_user", methods=["POST", "GET"]) # Define a rota para adicionar um novo item
def add_user():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("INSERT INTO users(name, email, phone) VALUES(?,?,?)", (name, email, phone))
        con.commit()
        flash("Usuário cadastrado com sucesso!", "success")
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<id>", methods=["POST", "GET"]) # Define a rota para editar um item
def edit_user(id):
    con = sql.connect("form_db.db")
    con.row_factory = sql.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM users WHERE id=?", (id,))
    data=cur.fetchone()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        cur.execute("UPDATE users SET name=?, email=?, phone=? WHERE id=?", (name, email, phone, id))
        con.commit()
        flash("Usuário editado com sucesso!", "success")
        return redirect(url_for("index"))
    return render_template("edit_user.html", datas=data)

index()