import json, os

#Json檔案基底
temp = {
    "name": "社畜",                         #使用者姓名
    "job": ["工作", "工作2"],               #工作
    "pay": [0, 100],                        #薪資
    "location": ["西屯", "台中"],           #地點
    "exp": 0                                #經歷
}

#創建/寫入JSON
def write_json(file, new_data):
    file = f'UserConfig/{file}.json'
    if not os.path.isfile(file):
        with open(file, "w", encoding='utf8') as f:
            f.write(json.dumps(temp, ensure_ascii = False, indent = 4))
            f.close()

    with open(file,'r+', encoding='utf8') as f:
        file_data = json.load(f)                                                #讀取JSON現有資料
        file_data["name"] = new_data
        # file_data["job"] = new_data
        # file_data["pay"] = new_data
        # file_data["location"] = new_data
        # file_data["exp"] = new_data
        f.seek(0)                                                               #設定輸入位置
        f.write(json.dumps(file_data, ensure_ascii = False, indent = 4))        #寫入                                                   
        f.close()                                                               #關閉

def config(id, name, text):
    try:
        data = text
        write_json(id, data)
    except:
        raise
        # msg = "發生未知問題!"
    else:
        msg = "資料儲存成功!"
    
    return msg
