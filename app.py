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
remsg = ''

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
def message(event, remsg):
    msg = event.message.text  # 將收到的文字放入msg中
    id = event.source.user_id  # 抓取使用者id
    name = line_bot_api.get_profile(id).display_name  # 抓取使用者姓名

    # 如果開頭是##,
    if msg.startswith("##,"):
        remsg = db.main(id, name, msg)  # 呼叫函式，並取得remsg回傳
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=remsg))
    # 如果信息是#主選單
    elif msg == "#主選單":
        try:
            #圖文選單
            remsg = ButtonsTemplate(
                thumbnail_image_url=bg,
                title="主選單",
                text="請選擇功能",
                actions=[
                    URIAction(label="資料填寫表", uri="https://liff.line.me/2000268560-PDBzXMGm"),
                    PostbackTemplateAction(label="更改爬蟲通知", data="#crawler",text="更改爬蟲通知"),
                    PostbackTemplateAction(label="查看資料", data="#check",text="查看資料"),
                    PostbackTemplateAction(label="刪除資料", data="#delete",text="刪除資料")
                ],
            )
            #送出圖文選單
            line_bot_api.reply_message(
                event.reply_token,
                TemplateSendMessage(alt_text="Buttons template", template=remsg),
            )
        #將回復狀態簡化，以便於記錄到log
        except:
            remsg = "發生錯誤"
        else:
            remsg = "成功送出"

    db.log_db(id, name, msg, remsg)  # 呼叫log函式


@handler.add(PostbackEvent)
def event(event, remsg):
    data = event.postback.data  # 將收到的資料放入data中
    id = event.source.user_id  # 抓取使用者id
    name = line_bot_api.get_profile(id).display_name # 抓取使用者資料

    #如果資料是#crawler_yes，呼叫更改通知函式
    if data == "#crawler_yes":
        remsg = db.updata_crawler_db(id, '是')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=remsg))
    #如果資料是#crawler_no，呼叫更改通知函式
    elif data == "#crawler_no":
        remsg = db.updata_crawler_db(id, '否')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=remsg))
    #如果資料是#check，呼叫查看資料函式
    elif data == "#check":
        remsg = db.check_db(id)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=remsg))
    #如果資料是#delete，再回傳一次圖文選單進行二次確認
    elif data == "#delete":
        try:
            #圖文選單
            remsg = ButtonsTemplate(
                thumbnail_image_url=bg,
                title="資料刪除",
                text="是否確定要刪除資料?",
                actions=[
                    PostbackTemplateAction(label="確定", data="#del", text="確定"),
                    PostbackTemplateAction(label="取消", data="#cen", text="取消"),
                ],
            )
            #送出圖文選單
            line_bot_api.reply_message(
                event.reply_token,
                TemplateSendMessage(alt_text="Buttons template", template=remsg),
            )
        #將回復狀態簡化，以便於記錄到log
        except:
            remsg = "發生錯誤"
        else:
            remsg = "確認刪除"
    #如果資料是#del，呼叫刪除函式
    elif data == "#del":
        remsg = db.delete_db(id)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=remsg))
    elif data == "#crawler":
        try:
            #圖文選單
            remsg = ButtonsTemplate(
                thumbnail_image_url=bg,
                title="爬蟲通知",
                text="請選擇功能",
                actions=[
                    PostbackTemplateAction(label="允許", data="#crawler_yes",text="允許"),
                    PostbackTemplateAction(label="不允許", data="#crawler_no",text="不允許"),
                ],
            )
        except:
            remsg = "發生錯誤"
        else:
            #先回覆圖文選單，再將回復狀態簡化，以便於記錄到log
            line_bot_api.reply_message(
                event.reply_token,
                TemplateSendMessage(alt_text="Buttons template", template=remsg),
            )
            remsg = "成功送出"
    
    db.log_db(id, name, data, remsg)  # 呼叫log函式


if __name__ == "__main__":
    app.run()
