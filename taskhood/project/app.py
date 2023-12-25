from flask import redirect, Flask, render_template, request, session, url_for
from cs50 import SQL
from flask_session import Session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"]= "filesystem"
app.config["SECRET_KEY"] =  "nakjdnadnndklqnoijdiadnaa/x15a131d6a5é'(é(-éu_çuçài)indzojkjqbq31)"
Session(app)
bcrypt = Bcrypt(app)
db = SQL("sqlite:///project.db")

@app.route("/")
def index():
    if session.get("user_name") is None:
        return redirect("/login")
    task = db.execute("SELECT * FROM tasks WHERE user = ?", session["user_name"])
    return render_template("index.html", tasks=task)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/login",methods=["GET", "POST"])
def login():
    if session.get("user_name"):
        return redirect("/")
    if request.method == "GET":
        return render_template("login.html")
    else:
        row = db.execute("SELECT * FROM users WHERE name = ?", request.form.get("usr_name"))
        if len(row) != 1:
            mess = "acount not found"
            return render_template("login.html",message=mess)
        if (51 < len(request.form.get("usr_name")) or len(request.form.get("usr_name")) < 2) or (12 < len(request.form.get("usr_pswrd")) or len(request.form.get("usr_pswrd")) < 6) :
            mess = "you thought you're a hacker or what ?"
            return render_template("login.html",message=mess)
        if bcrypt.check_password_hash(row[0]["password"], request.form.get("usr_pswrd")):
            session["user_name"] = request.form.get("usr_name")
            return redirect("/")
        else:
            mess = "wrong password"
            return render_template("login.html",message=mess)

@app.route("/register", methods=["GET", "POST"])
def register():

    if session.get("user_name"):
        return redirect("/")

    if request.method == "GET":
        return render_template("register.html")
    else:
        print("Name length:", len(request.form.get("usr_name")))
        print("Password length:", len(request.form.get("usr_pswrd")))
        row = db.execute("SELECT * FROM users WHERE name = ?", request.form.get("usr_name"))
        if len(row) == 1:
            mess = "name already taken"
            return render_template("register.html",message=mess)
        if (51 < len(request.form.get("usr_name")) or len(request.form.get("usr_name")) < 2) or (12 < len(request.form.get("usr_pswrd")) or len(request.form.get("usr_pswrd")) < 6) :        
            mess = "you thought you're a hacker or what ?"
            return render_template("register.html",message=mess)
        db.execute("INSERT INTO users(name, password) values(?, ?)", request.form.get("usr_name"), bcrypt.generate_password_hash(request.form.get("usr_pswrd")).decode('utf-8'))
        session["user_name"] = request.form.get("usr_name")
        return redirect("/")

@app.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if request.form.get("task") :
            db.execute("INSERT INTO tasks(user, task) VALUES(?, ?)", session["user_name"], request.form.get("task"))
        for check in request.form.getlist("check"):
            db.execute("DELETE FROM tasks WHERE user = ? AND task = ?", session["user_name"], check)
        return redirect("/")
        
@app.route("/board", methods=["GET", "POST"])
def board():
    if request.method == "GET":
        if session.get("user_name"):
            return render_template("board.html")
        else:
            redirect("/login")