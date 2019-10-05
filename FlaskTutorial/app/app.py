#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request
from models.models import KitsuneContest

from models.database import db_session
from datetime import datetime


#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"


#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    name = request.args.get("name")
    #song = ["こぶた","たぬき","きつね🦊","ねこ"]

    all_contests = KitsuneContest.query.all()
    return render_template("index.html", name=name, all_contests=all_contests)

@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    #song = ["こぶた", "たぬき", "きつね🦊", "ねこ"]
    all_contests = KitsuneContest.query.all()
    return render_template("index.html", name=name, all_contests=all_contests)

@app.route("/add",methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = KitsuneContest(title,body,datetime.now())
    db_session.add(content)
    db_session.commit()
    return index()

@app.route("/update",methods=["post"])
def update():
    content = KitsuneContest.query.filter_by(id=request.form["update"]).first()
    content.title = request.form["title"]
    content.body = request.form["body"]
    db_session.commit()
    return index()

@app.route("/delete",methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = KitsuneContest.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return index()

#おまじない
if __name__ == "__main__":
    app.run(debug=True)