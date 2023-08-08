# 載入 LINE Message API 及 flask 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction,
    PostbackEvent,
    PostbackTemplateAction
)
from flask import Flask, request, abort
from logs.log import log
from UserConfig.config import config
import json

#讀取設定檔
with open('UserConfig/config.json', 'r', encoding='utf8')as J:
    j = json.load(J)

app = Flask(__name__)
line_bot_api = LineBotApi(j['token'])
handler = WebhookHandler(j['secret'])

#基底碼
@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
    body = request.get_data(as_text=True)                # 取得收到的訊息內容
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

#接收Line客戶端訊息
@handler.add(MessageEvent, message=TextMessage)                                            #如果訊息是文字
def event(event):
    msg = event.message.text                                                                #將收到的文字放入msg中
    remsg = ""                                                                              #宣告空字串
    id = event.source.user_id                                                               #抓取使用者id
    profile = line_bot_api.get_profile(id)                                                  #抓取使用者資料
    if msg.startswith("#,"):                                                                #如果開頭是#/
        msg = config(id, profile.display_name, msg)                                         #呼叫函式，並取得msg回傳
        remsg = msg                                                                         #將回傳的文字放入remsg中
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = remsg))         #回傳給使用者
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = msg))           #回傳給使用者
        remsg = msg                                                                         #將回傳的文字放入remsg中
    log(id, profile.display_name, event.message.text, remsg)                                #紀錄log中


if __name__ == "__main__":
    app.run()
