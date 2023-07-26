import datetime, time

def log(id, name, text, remsg = ''):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    with open(f"logs/{id}.txt", "a", encoding='utf8') as f:
        print(f'<{st}>\n使用者名稱 : {name}\n訊息 : {text}\n機器人回傳:{remsg}\n'+'-'*25, file=f)
