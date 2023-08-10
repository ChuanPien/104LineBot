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
    PostbackTemplateAction
)
from flask import Flask, request, abort
from DB import db
import json

# 讀取設定檔
with open('config.json', 'r', encoding='utf8')as J:
    j = json.load(J)

app = Flask(__name__)
line_bot_api = LineBotApi(j['token'])
handler = WebhookHandler(j['secret'])
bg='https://raw.githubusercontent.com/ChuanPien/LineBot_Updating/main/lib/preview.jpg'
remsg = '' #宣告空字串

# 基底碼
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
@handler.add(MessageEvent, message=TextMessage)                                             #如果訊息是文字
def message(event):
    msg = event.message.text                                                                #將收到的文字放入msg中
    id = event.source.user_id                                                               #抓取使用者id
    profile = line_bot_api.get_profile(id)                                                  #抓取使用者資料
    if msg.startswith("##,"):                                                               #如果開頭是##,
        msg = db.main(id, profile.display_name, msg)                                        #呼叫函式，並取得msg回傳
        remsg = msg                                                                         #將回傳的文字放入remsg中
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = remsg))         #回傳給使用者
    elif msg == "#主選單":
        try:
            remsg=ButtonsTemplate(
                thumbnail_image_url=bg,
                title='主選單',
                text='請選擇功能',
                actions=[
                    PostbackTemplateAction(
                        label='資料填寫表',
                        data='#dataWeb'
                    ),
                    PostbackTemplateAction(
                        label='叫出主選單',
                        data='#mainPage'
                    )
                ]
            )
        except:
            remsg = "發生錯誤"
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = remsg))
        else:
            line_bot_api.reply_message(event.reply_token,TemplateSendMessage(alt_text='Buttons template', template = remsg))
            remsg = "成功送出"
        
    log(id, profile.display_name, event.message.text, remsg)#呼叫log函式

@handler.add(PostbackEvent)
def event(event):
    data = event.postback.data                  #將收到的資料放入data中
    id = event.source.user_id                   #抓取使用者id
    profile = line_bot_api.get_profile(id)      #抓取使用者資料
    if data == "#mainPage":
        try:
            remsg=ButtonsTemplate(
                thumbnail_image_url=bg,
                title='主選單',
                text='請選擇功能',
                actions=[
                    PostbackTemplateAction(
                        label='資料填寫表',
                        data='#dataWeb'
                    ),
                    PostbackTemplateAction(
                        label='叫出主選單',
                        data='#mainPage'
                    )
                ]
            )
        except:
            remsg = "發生錯誤"
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = remsg))
        else:
            line_bot_api.reply_message(event.reply_token,TemplateSendMessage(alt_text='Buttons template', template = remsg))
            remsg = "成功送出"
    elif data == "#dataWeb":
        try:
            remsg=ButtonsTemplate(
                thumbnail_image_url=bg,
                title='資料填寫表',
                text='資料填寫表',
                actions=[
                    URIAction(
                        label='資料填寫表',
                        uri='https://liff.line.me/2000268560-PDBzXMGm'
                    )
                ]
            )
        except:
            remsg = "發生錯誤"
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = remsg))
        else:
            line_bot_api.reply_message(event.reply_token,TemplateSendMessage(alt_text='Buttons template', template = remsg))
            remsg = "成功送出"
    log(id, profile.display_name, data, remsg)#呼叫log函式

if __name__ == "__main__":
    app.run()
