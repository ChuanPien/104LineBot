import json
'''
Json檔案基底
{
    "ID":"U445009dc87d992834e15252c9e63",
    "Name": "社畜",                         #使用者姓名
    "job": ["工作", "工作2"],               #工作
    "pay": [0, 100],                        #薪資
    "loc": ["西屯", "台中"],                #地點
    "exp": 0                                #經歷
}
'''

#創建/寫入JSON
def write_json(id, name, new_data):
    file = f'UserConfig/User.json'
    with open(file,'r+', encoding='utf8') as f:
        file_data = json.load(f)                                                #讀取JSON現有資料
        file_data["ID"] = id
        file_data["Name"] = name
        file_data["job"] = new_data
        file_data["pay"] = new_data
        file_data["loc"] = new_data
        file_data["exp"] = new_data
        f.seek(0)                                                               #設定輸入位置
        f.write(json.dumps(file_data, ensure_ascii = False, indent = 4))        #寫入                                                   
        f.close()                                                               #關閉

def config(id, name, msg):
    try:
        data = msg.split(',')
        data.remove("#")
        print(data)
        # write_json(id, name, data)
    except:
        msg = "發生錯誤!"
        raise
    else:
        msg = "資料儲存成功!"
    
    return msg
