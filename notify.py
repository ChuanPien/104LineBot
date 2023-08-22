import requests, json
from Crawler.main import main
from DB import db

# 讀取設定檔
with open("config.json", "r", encoding="utf8") as J:
    j = json.load(J)

token = j["N_token"]
userid = db.check_crawler_db()
for i in userid:
    userData = db.check_db(i[0], True)
    remsg = main(userData[2:])
    # HTTP 標頭參數與資料
    headers = {"Authorization": "Bearer " + token}
    data = {"message": remsg}

    # # 以 requests 發送 POST 請求
    requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)
