# 載入 pymysql 及 json 函式庫
import pymysql, json, datetime

# 讀取json資料
with open('./config.json', 'r', encoding='utf8')as J:
    j = json.load(J)

# 連接絲料庫
db_settings = j["db_settings"]
db = pymysql.connect(**db_settings)
con = db.cursor()

# 新增SQL資料
def insert_db(id, name, data):
    commend = f"""INSERT INTO user (id, name, job_A, job_B, loc_A, loc_B, loc_C, pay, exp) 
        VALUES ('{id}', '{name}', '{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{data[6]}')"""
    con.execute(commend)

# 修改SQL資料
def updata_db(id, data):
    i = 0
    tmp = ['job_A', 'job_B', 'loc_A', 'loc_B', 'loc_C', 'pay', 'exp', 'crawler']
    for x in data:
        if x != '#':
            command = f"""UPDATE user SET {tmp[i]} = '{data[i]}' WHERE id = '{id}'"""
            con.execute(command)
        i += 1

# 抓取SQL資料
def select_db(id):
    command = f"""SELECT * FROM log WHERE id = '{id}'"""
    con.execute(command)
    result = con.fetchall()  #取得所有資料
    print(result)

# 刪除SQL資料
def delete_db(id):
    command = f"""DELETE FROM User WHERE id = '{id}'"""
    con.execute(command)

# 紀錄log
def log_db(id, name, msg, remsg):
    time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    commend = f"""INSERT INTO log (time, id, name, msg, remsg) 
        VALUES ('{time}', '{id}', '{name}', '{msg}', '{remsg}')"""
    con.execute(commend)
    db.commit()
    db.close()

def main(id, name, msg):
    try:
        data = msg.split(',')   #將msg字串用,分割開
        data.remove("##")        #移除第一個'##'字號
        commend = f"""SELECT id FROM user WHERE EXISTS(SELECT * FROM user WHERE id = '{id}')"""     #檢查資料是否存在
        if con.execute(commend):    #如果存在就進行修改
            updata_db(id,data)
        else:                       #如果不存在就新增
            insert_db(id, name, data)            
    except:
        msg = "發生錯誤!"
        raise
    else:
        #資料庫存檔並關閉
        db.commit()
        db.close()
        msg = "資料儲存成功!"
    
    return msg
