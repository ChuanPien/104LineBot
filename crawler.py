#import selenium 模組
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
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)    #網頁至頂

#等待網頁元素出現
WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "ijob"))
    )

#模擬點擊[職務類別選單]
ijob = driver.find_element(By.ID, "ijob")
action = ActionChains(driver).click(ijob).perform()

#抓取所有職務類別
childrens = driver.find_element(By.CLASS_NAME, "children")
for children in childrens:
    print(children.text)

driver.quit()