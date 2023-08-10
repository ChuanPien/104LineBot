# import jieba
# jieba.set_dictionary('dict.txt.big')
# jieba.initialize()  #強制提早加載

# import paddle
# paddle.enable_static()
# jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持
# strs=["我来到北京清华大学","乒乓球拍卖完了","中国科学技术大学"]
# for str in strs:
#     seg_list = jieba.cut(str,use_paddle=True) # 使用paddle模式
#     print("Paddle Mode: " + '/'.join(list(seg_list)))

# 全模式
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("\nFull Mode: " + "/ ".join(seg_list))

# fix = ['軟體工程師', '沒有工作經驗']
# for i in fix:
#     jieba.suggest_freq((i), True)  #可調節單個詞語的詞頻，使其能（或不能）被分出來

# seg_list = jieba.cut("我想找軟體工程師無學歷沒有工作經驗")  # 默认是精确模式
# print(", ".join(seg_list))

# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print("\n, ".join(seg_list))

# ------------------------------------------------------

# https://www.tpisoftware.com/tpu/articleDetails/2013
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.linear_model import LogisticRegression
# import pandas as pd

# read = pd.read_excel("Crawler/data.xlsx").values.tolist()
# corpus = [row[0] for row in read]
# intents = [row[1] for row in read]

# feature_extractor = CountVectorizer(
#             analyzer="word", ngram_range=(1, 2), binary=True,
#             token_pattern=r'([a-zA-Z]+|\w)')
# X = feature_extractor.fit_transform(corpus)

# INTENT_CLASSIFY_REGULARIZATION = "l2"

# lr = LogisticRegression(penalty=INTENT_CLASSIFY_REGULARIZATION,class_weight='balanced')
# lr.fit(X, intents)

# user_input = ['松山']
# X2 = feature_extractor.transform(user_input)
# print(lr.predict(X2))

# probs = lr.predict_proba(X2)[0]
# for predict_intent, prob in sorted(zip(lr.classes_, probs), key = lambda x: x[1],reverse = True):
#     print(predict_intent, prob)

# ------------------------------------------------------
# from openpyxl import Workbook, load_workbook

# wb = load_workbook("Crawler/data.xlsx")
# ws = wb["city"]

# A = "東區"

# for row in range(1, ws.max_row):
#     produceName = ws.cell(row, 1).value
#     if A in produceName:
#         print(ws.cell(row, 2).value + "|" + A)

# ------------------------------------------------------
# import json

# with open('Crawler\city.json', 'r', encoding='utf8')as J:
#     j = json.load(J)
#     x=1
#     for i in j["西非"]:
#         print('{"value": "option' + f'{x}' + '", "text":"' + f'{i}'+'"},')
#         x+=1

# ------------------------------------------------------

# import pymysql
# 連線資料庫
# db_settings = {
#     'host' : "192.168.1.60",
#     'user' : "ChuanPien",
#     'passwd' : "",
#     'database' : "LineBot",
#     'port' : 3306
# }

# try:
    # 建立Connection物件
    # conn = pymysql.connect(**db_settings)

    # 建立Cursor物件
    # with conn.cursor() as cursor:
        # 新增SQL資料
        # data = "INSERT INTO user (id, name, job_A, job_B, loc_A, loc_B, loc_C, pay, exp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # cursor.execute(data, ("U445009dc87d992834e15252c9e637b6b", "李慈欣", "軟體/工程類人員", "iOS工程師", "台灣地區", "台中市", "台中市西屯區", "1500~35000", "0"))
        
        # 抓取SQL資料
        # command = "SELECT * FROM User WHERE id = %s"
        # cursor.execute(command, ("U445009dc87d992834e15252c9e637b6b",))
        # result = cursor.fetchall()  #取得所有資料
        # print(result)

        # 修改SQL資料
        # command = "UPDATE User SET name = %s WHERE id = %s"
        # cursor.execute(command, ("ChuanPien", "U445009dc87d992834e15252c9e637b6b"))
        
        # 刪除SQL資料
        # command = "DELETE FROM User WHERE id = %s"

        # conn.commit()   #儲存變更

# except Exception as ex:
#     print(ex)

# ------------------------------------------------------

# import requests

# # LINE Notify 權杖
# token = '4mNmdpSPZPNsPtryTpQDr2HbnHBEUvj15deUuFQvNqC'

# # 要發送的訊息
# message = '這是用 Python 發送的訊息'

# # HTTP 標頭參數與資料
# headers = { "Authorization": "Bearer " + token }
# data = { 'message': message }

# # 以 requests 發送 POST 請求
# requests.post("https://notify-api.line.me/api/notify",
#     headers = headers, data = data)

# ------------------------------------------------------

# from datetime import datetime
# print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

# ------------------------------------------------------

