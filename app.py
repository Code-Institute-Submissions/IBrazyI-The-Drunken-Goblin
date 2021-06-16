from logging import debug
import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to The Drunken Goblin"


if __name__ == "__main__":
    app.run(host=os.os.environ.get("IP"),
        port=int(os.os.environ.get("PORT")),
        debug=True)