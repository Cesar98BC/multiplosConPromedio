from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    multi1=2344
    multi2=3756
    multi3=5868
    sum=multi1 + multi2 + multi3
    pro=sum/3
    return render_template('index.html',multi1=multi1,multi2=multi2,multi3=multi3,pro=pro)