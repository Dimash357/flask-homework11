import random
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    for i in range(1, 1001):
        i = random.randrange(1, 1001)
        return f"<p>{i}</p>"

