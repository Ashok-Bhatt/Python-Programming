from flask import Flask, url_for, render_template, request, redirect, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "ashok"
app.permanent_session_lifetime = timedelta(minutes=3)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # session.permanent = True
        user = request.form["name"]
        session["user"] = user
        return redirect(url_for("user", usr=user))
    elif "user" in session:
        return redirect(url_for("user"))
    else:
        return render_template("login.html")
    
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)