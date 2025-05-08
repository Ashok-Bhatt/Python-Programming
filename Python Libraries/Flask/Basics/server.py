
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "I'm Home."

@app.route("/about/<name>")
def about(name):
    return f"{name} is SDE-2 at Amazon, India"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("about", name="Ashok"))

if __name__ == "__main__":
    app.run(debug=True)