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

#讀取設定檔
with open('./config.json', 'r', encoding='utf8')as J:
    j = json.load(J)


def city(continent, country, town):
    #模擬點擊[職務類別選單]
    icity = driver.find_element(By.ID, "icity")
    ActionChains(driver).click(icity).perform()
    try:
        WebDriverWait(driver, 15.0).until(
        EC.presence_of_element_located((By.CLASS_NAME, "category-item--level-one"))
        )
    except:
        redata = '發生City階段錯誤'
        return(redata)
    else:
    #抓取所有職務類別
        l1s = driver.find_elements(By.CLASS_NAME, "category-item--level-one")
        for l1 in l1s:
            if l1.text == continent:
                ActionChains(driver).click(l1).perform()                                         #依序打開
                l2s = driver.find_elements(By.CLASS_NAME, "category-item--level-two")
                for l2 in l2s:
                    if l2.text == country:
                        ActionChains(driver).click(l2).perform()                                    #依序打開
                        l3s = driver.find_elements(By.CLASS_NAME, "category-item--level-three")
                        #依序將l3s中的文字提出
                        for l3 in l3s:
                            if l3.text == town:
                                ActionChains(driver).click(l3).perform()
                                close = driver.find_element(By.CLASS_NAME, "category-picker-o-close")
                                ActionChains(driver).click(close).perform()
                                return


def job(job1, job2):
    #模擬點擊[職務類別選單]
    ijob = driver.find_element(By.ID, "ijob")
    ActionChains(driver).click(ijob).perform()
    #抓取所有職務類別
    arrows = driver.find_elements(By.CLASS_NAME, "arrow--right")
    for arrow in arrows:
        ActionChains(driver).click(arrow).perform()                                         #依序打開
        l2s = driver.find_elements(By.CLASS_NAME, "category-item--level-two")
        for l2 in l2s:
            if l2.text == job1:
                ActionChains(driver).click(l2).perform()                                    #依序打開
                l3s = driver.find_elements(By.CLASS_NAME, "category-item--level-three")
                #依序將l3s中的文字提出
                for l3 in l3s:
                    if l3.text == job2:
                        time.sleep(0.2)
                        ActionChains(driver).click(l3).perform()
                        close = driver.find_element(By.CLASS_NAME, "category-picker-o-close")
                        ActionChains(driver).click(close).perform()
                        return


def run():
    # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ENTER)
    time.sleep(3.0)
    list = driver.find_elements(By.CLASS_NAME, "js-job-link")
    for i in list:
        url = i.get_attribute('href')
        return(i.text, url)

# 設定Chrome參數
def setup():
    s = Service(j['driver'])
    options = Options()
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    global driver
    driver = webdriver.Chrome(service=s, options=options)
    driver.get("https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007001013&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001008007&order=17&asc=0&page=1&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1")
    # driver.get("https://www.104.com.tw/jobs/main/")
    
# 主程式
def main(data):
    redata = setup()
    # if data[0]:
    #     redata = city(data[0],data[1],data[2])
    # time.sleep(.5)
    # if data[3]:
    #     redata = job(data[3],data[4])
    # time.sleep(.5)
    redata = run()

    driver.quit()
    return redata

data = ('台灣地區', '台中市', '台中市西屯區', '軟體／工程類人員', 'iOS工程師', '35000', 0)
print(main(data))