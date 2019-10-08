#雛形: Qiita「【Python3】WebAPIを叩く【requests】
#<https://qiita.com/shunyooo/items/b408b8d61f9f73b21da7>

import requests
import json

# APIキーの指定
apikey = "My API Key"

# 天気を調べたい都市の一覧 
cities = ["Kumagaya,JP","Tokyo,JP", "London,UK", "New York,US"]
# APIのひな型
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 温度変換(ケルビン→摂氏)
k2c = lambda k: k - 273.15

# 各都市の温度を取得する
for name in cities:
    # APIのURLを得る
    url = api.format(city=name, key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する
    r = requests.get(url)
    # 結果はJSON形式なのでデコードする
    data = json.loads(r.text)
    # 元データを出力
    #print(data) 
    # 結果を出力
    print("+ 都市　　　=", data["name"])
    print("| 国   　　=", data["sys"]["country"])
    print("| 天気　　　=", data["weather"][0]["description"])
    print("| 最低気温=", k2c(data["main"]["temp_min"]))
    print("| 最高気温=", k2c(data["main"]["temp_max"]))
    print("| 湿度　　　=", data["main"]["humidity"])
    print("| 気圧　　　=", data["main"]["pressure"])
    #print("| 風向き=", data["wind"]["deg"])
    print("| 風速度  =", data["wind"]["speed"])
    print("")