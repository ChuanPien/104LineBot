# 載入 LINE Message API 及 flask 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    URIAction,
    TextMessage,
    MessageEvent,
    PostbackEvent,
    ButtonsTemplate,
    TextSendMessage,
    TemplateSendMessage,
    PostbackTemplateAction,
)
from flask import Flask, request, abort
from DB import db
import json

# 讀取設定檔
with open("config.json", "r", encoding="utf8") as J:
    j = json.load(J)

app = Flask(__name__)
line_bot_api = LineBotApi(j["token"])
handler = WebhookHandler(j["secret"])
bg = "https://raw.githubusercontent.com/ChuanPien/104LineBot/main/lib/bg.jpg"


# 基底碼
@app.route("/", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]  # 加入回傳的 headers
    body = request.get_data(as_text=True)  # 取得收到的訊息內容
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


# 接收Line客戶端訊息
@handler.add(MessageEvent, message=TextMessage)  # 如果訊息是文字
def message(event):
    msg = event.message.text  # 將收到的文字放入msg中
    id = event.source.user_id  # 抓取使用者id
    name = line_bot_api.get_profile(id).display_name  # 抓取使用者姓名
    if msg.startswith("##,"):  # 如果開頭是##,
        remsg = db.main(id, name, msg)  # 呼叫函式，並取得remsg回傳
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=remsg))
    elif msg == "#主選單":
        remsg = ButtonsTemplate(
            thumbnail_image_url=bg,
            title="主選單",
            text="請選擇功能",
            actions=[
                URIAction(label="資料填寫表", uri="https://liff.line.me/2000268560-PDBzXMGm"),
                PostbackTemplateAction(label="更改是否進行爬蟲", data="#crawler")
            ],
        )
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(alt_text="Buttons template", template=remsg),
        )
        remsg = "成功送出"

    db.log_db(id, name, msg, remsg)  # 呼叫log函式


@handler.add(PostbackEvent)
def event(event):
    data = event.postback.data  # 將收到的資料放入data中
    id = event.source.user_id  # 抓取使用者id
    name = line_bot_api.get_profile(id).display_name # 抓取使用者資料
    if data == "#crawler_yes":
        remsg = db.crawler_db(id, 'yes')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=remsg))
    elif data == "#crawler_no":
        remsg = db.crawler_db(id, 'no')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=remsg))
    elif data == "#crawler":
        try:
            remsg = ButtonsTemplate(
                thumbnail_image_url=bg,
                title="爬蟲通知",
                text="請選擇功能",
                actions=[
                    PostbackTemplateAction(label="允許", data="#crawler_yes"),
                    PostbackTemplateAction(label="不允許", data="#crawler_no"),
                ],
            )
        except:
            remsg = "發生錯誤"
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TemplateSendMessage(alt_text="Buttons template", template=remsg),
            )
            remsg = "成功送出"
    db.log_db(id, name, data, remsg)  # 呼叫log函式


if __name__ == "__main__":
    app.run()
