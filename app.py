from flask import Flask, request, abort
from logs.log import log
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
with open('config.json', 'r', encoding='utf8')as J:
    j = json.load(J)

app = Flask(__name__)
line_bot_api = LineBotApi(j['token'])
handler = WebhookHandler(j['secret'])

@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
    body = request.get_data(as_text=True)                # 取得收到的訊息內容
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)         #如果訊息是文字
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='test'))  #回傳'test'
    id = event.source.user_id        #抓取使用者id
    profile = line_bot_api.get_profile(id)        #抓取使用者資料
    log(id, profile.display_name, event.message.text)        #紀錄log中

if __name__ == "__main__":
    app.run()
