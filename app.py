from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    multi1=2344
    pro=multi1/2
    return render_template('index.html',multi1=multi1,pro=pro)