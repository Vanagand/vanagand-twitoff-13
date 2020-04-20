# hello.py

import flask from Flask

app = Flask(__name__)

@app.route("/") # handle requests to the home page
def hello_world():
    return "Hello, World!"

@app.route("/about")
def about():
    x = 2 + 2
    return f"About me {x}"

""" Foot notes
    * CTRL + C will refresh server in command line
"""