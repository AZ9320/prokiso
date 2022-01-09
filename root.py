#とりあえず必要そうなの全部インポート
from typing import DefaultDict
from flask import Flask,url_for
from flask import render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bootstrap import Bootstrap
import os
import pytz

#おまじない
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elewatch.db'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

#データベースの定義
class Data(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(),nullable=False)
    stairs = db.Column(db.Integer(),nullable=False)
    capacity = db.Column(db.Integer())
    number = db.Column(db.Integer())
    time = db.Column(db.String(),default="{time-1:1}")

#登録画面その１
@app.route("/",methods=["GET","POST"])
def basic():
    #フォームが送信されていないときは入力画面その１を表示
    if request.method=="GET":
        return render_template("basic.html")
    #フォームが送信されたとき
    else:
        #フォームの入力内容を取得
        name = request.form.get("name")
        stairs = request.form.get("stairs")
        capacity = request.form.get("capacity")
        number = request.form.get("number")
        #データベースにデータを追加
        data = Data(name=name,stairs=stairs,capacity=capacity,number=number)
        db.session.add(data)
        db.session.commit()
        #階数によって次のページの表示を変更
        return redirect(f"/basic/{stairs}")

#入力画面その２
@app.route("/basic/<int:stairs>",methods=["GET","POST"])
def basic2(stairs):
    #フォームが入力されていない時
    if request.method=="GET":
        return render_template("basic2.html",stairs=stairs)
    #フォームが送信されたとき
    else:
        #timeのデフォルト値を更新する
        time = str(request.form)
        row = Data.query.get(1)
        row.time = time
        db.session.commit()
        #表示画面に遷移
        return render_template("index.html")

@app.route("/index",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html")

#ここから下はflask起動中にCSSやjsの変更が反映されるような設定
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)



