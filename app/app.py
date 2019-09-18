#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request

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
    song = ["こぶた","たぬき","きつね🦊","ねこ"]
    return render_template("index.html",name=name,song=song)

@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    song = ["こぶた", "たぬき", "きつね🦊", "ねこ"]
    return render_template("index.html", name=name, song=song)

#おまじない
if __name__ == "__main__":
    app.run(debug=True)