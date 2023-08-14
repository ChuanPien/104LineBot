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
                                close = driver.find_element(By.CLASS_NAME, "category-picker-btn-primary")
                                ActionChains(driver).click(close).perform()
                                return


def job(job1, job2):
    #模擬點擊[職務類別選單]
    ijob = driver.find_element(By.ID, "ijob")
    ActionChains(driver).click(ijob).perform()
    time.sleep(0.2)
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
                    time.sleep(0.2)
                    if l3.text == job2:
                        time.sleep(0.2)
                        ActionChains(driver).click(l3).perform()
                        time.sleep(0.1)
                        close = driver.find_element(By.CLASS_NAME, "category-picker-btn-primary")
                        ActionChains(driver).click(close).perform()
                        return


def run(scmin, scmax, exp):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ENTER)
    time.sleep(1.0)
    tabs = driver.find_elements(By.CLASS_NAME, 'b-tabs__item')

    if scmin != 0 or scmax != 0:
        # 填入薪資條件
        ActionChains(driver).click(tabs[2]).perform()
        time.sleep(.2)
        if scmin != 0:
            driver.find_element(By.CLASS_NAME, 'salary-min').send_keys(scmin)
        if scmax != 0:
            driver.find_element(By.CLASS_NAME, 'salary-max').send_keys(scmax)
        time.sleep(.5)
        driver.find_element(By.CLASS_NAME, 'salary-min').send_keys(Keys.ENTER)

    if exp != 0:
        seletexp = 0
        # 選擇年資條件
        if exp >= 1 and exp <=2:
            seletexp = 1
        elif exp >= 3 and exp <=4:
            seletexp = 2
        elif exp >= 5 and exp <=9:
            seletexp = 3
        elif exp >= 10:
            seletexp = 4
            
        if seletexp != 0:
            ActionChains(driver).click(tabs[3]).perform()
            exp = driver.find_element(By.XPATH, f'/html/body/main/div[2]/div[3]/div[2]/div/div[4]/label[{seletexp}]/span')
            ActionChains(driver).click(exp).perform()

    time.sleep(.3)
    jobs = driver.find_elements(By.CLASS_NAME, "js-job-link")
    if jobs:
        redata = []
        for i in jobs[:3]:
            url = i.get_attribute('href')
            redata.append(i.text)
            redata.append(url)
    else: 
        redata = '抱歉!沒有與您條件相符的職缺'
    return(redata)

# 設定Chrome參數
def setup():
    s = Service(j['driver'])
    options = Options()
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    global driver
    driver = webdriver.Chrome(service=s, options=options)
    # driver.get("https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007001013&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001008007&order=17&asc=0&page=1&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1")
    driver.get("https://www.104.com.tw/jobs/main/")
    
# 主程式
def main(data):
    redata = setup()
    if data[0]:
        redata = city(data[0],data[1],data[2])
    time.sleep(.5)
    if data[3]:
        redata = job(data[3],data[4])
    time.sleep(.5)
    redata = run(data[5], data[6], data[7])

    driver.quit()
    return redata

# data = ('台灣地區', '台中市', '台中市西屯區', '軟體／工程類人員', 'iOS工程師', 30000, 35000, 0)
# print(main(data))