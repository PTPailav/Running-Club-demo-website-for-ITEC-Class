from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/us")
def us():
    return render_template("aboutus.html")

@app.route("/merch")
def merch():
    return render_template("merch.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

if __name__ == "__main__":
    app.run(debug=True)