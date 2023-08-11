import requests, json
from Crawler.main import run
from DB import db

# 讀取設定檔
with open("config.json", "r", encoding="utf8") as J:
    j = json.load(J)

token = j["N_token"]
userid = db.check_crawler_db()
for i in userid:
    userData = db.check_db(i[0], True)
    msg = run(userData[2:9])
    print(msg)
    # # HTTP 標頭參數與資料
    # headers = {"Authorization": "Bearer " + token}
    # data = {"message": msg}

    # # 以 requests 發送 POST 請求
    # requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)
