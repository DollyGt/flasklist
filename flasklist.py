import os
from flask import Flask, request, render_template, redirect
from random import choice

app = Flask(__name__)

welcome_messages = ["Hi", "Hello", "Bonjour", "Ciao","Hola","Dumela"]

items = [
    "Buy Computer",
    "Learn Python"
    ]

@app.route("/")
def get_index():
    welcome = choice(welcome_messages)
    return render_template("index.html", tasks=items)

@app.route("/new_task", methods=["POST"])
def create_task():
    task= request.args["task_to_do"]
    items.append(task)
    return redirect("/")


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)