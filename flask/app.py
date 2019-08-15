from flask import Flask, render_template

app = Flask(__name__,template_folder='template')


@app.route("/index")
def index():
    return "hello"


@app.route("/<string:name>")
def eo(name):
    name=name.capitalize()
    return f"Hello {name}"


@app.route("/")
def temp():
    return render_template("a1.html")

@app.route("/panda")
def second():
    return render_template("sd.html",text='hello')
