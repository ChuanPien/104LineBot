#import selenium 相關函式庫
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time, json
with open('config.json', 'r', encoding='utf8')as J:     #讀取json設定檔
    j = json.load(J)

#設定Chrome參數
s = Service(j['driver'])
options = Options()
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(service=s, options=options)
driver.maximize_window()        #全螢幕
driver.get("https://www.104.com.tw/jobs/main/")      #連到104網頁
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)        #網頁至頂

#等待網頁元素出現
WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "ijob"))
    )

#模擬點擊[職務類別選單]
ijob = driver.find_element(By.ID, "ijob")
action = ActionChains(driver).click(ijob).perform()

# {"職務":{"經營":["儲備幹部"],"人資類":["人力資源人員"]}}

#抓取所有職務類別並存入JSON檔
arrows = driver.find_elements(By.CLASS_NAME, "arrow--right")                        #抓取大類別
for arrow in arrows:
    i = 0
    action = ActionChains(driver).click(arrow).perform()                            #依序打開
    ardowns = driver.find_elements(By.CLASS_NAME, "arrow--down")                    #抓取中類別
    for ardown in ardowns[1:]:
        action = ActionChains(driver).click(ardown).perform()                       #依序打開
        l2s = driver.find_elements(By.CLASS_NAME, "category-item--level-two")       #抓取中類別
        l3s = driver.find_elements(By.CLASS_NAME, "category-item--level-three")     #抓取小類別
        print('"'+l2s[i].text+'"')
        for l3 in l3s:
            if l3.text != '':
                print('"'+l3.text+'"')
        i += 1
        arrowup = driver.find_element(By.CLASS_NAME, "arrow--up")                   #抓取打開的小類別
        actions = ActionChains(driver).click(arrowup).perform()                     #關閉小類別
        time.sleep(0.3)                                                             #等待0.3秒

    # with open("data.json", "w") as d:
    #     json.dump(":{{l2.text}:[]}",format() ,d)


driver.quit()                                                                       #關閉網頁
# j.close()                                                                         #關閉JSON檔
