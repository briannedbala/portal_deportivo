from flask import Flask, render_template
from config import config

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index')


if __name__ == '__main__':
    app.run()
