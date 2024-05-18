from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
def wh_msg(p,a,m):        
        wtapp_profile="user-data-dir=C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\wah"
        options = Options()
        options.add_argument('--headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('--disable-gpu')
        options.add_argument(wtapp_profile)

        service = Service('C:\\Users\\HP\\Downloads\\chromedriver.exe')
        service.start()
        driver = webdriver.Chrome(service=service, options=options)

        driver.get('https://web.whatsapp.com/')
        for i in range(0, len(p)):
                search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
                search_box = WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, search_box_xpath)))
                search_box.send_keys(p[i])
                search_box.send_keys(u'\ue007')

                message_box_xpath = '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
                message_box = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, message_box_xpath)))
                c=a[i]+m
                message_box.send_keys(c)
                message_box.send_keys(u'\ue007')
                time.sleep(5)

        driver.quit()
        service.stop()


def wh_p_msg(ph,c):
        wtapp_profile="user-data-dir=C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\wah"
        options = Options()
        options.add_argument('--headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('--disable-gpu')
        options.add_argument(wtapp_profile)

        service = Service('C:\\Users\\HP\\Downloads\\chromedriver.exe')
        service.start()
        driver = webdriver.Chrome(service=service, options=options)

        driver.get('https://web.whatsapp.com/')

        for p in ph:
                search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
                search_box = WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, search_box_xpath)))
                search_box.send_keys(p)
                search_box.send_keys(u'\ue007')

                message_box_xpath = '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
                message_box = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, message_box_xpath)))
                message_box.send_keys(c)
                message_box.send_keys(u'\ue007')
                time.sleep(5)
                driver.quit()
                service.stop()

def code_4(p,c):
        wtapp_profile="user-data-dir=C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\wah"
        options = Options()
        options.add_argument('--headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('--disable-gpu')
        options.add_argument(wtapp_profile)

        service = Service('C:\\Users\\HP\\Downloads\\chromedriver.exe')
        service.start()
        driver = webdriver.Chrome(service=service, options=options)

        driver.get('https://web.whatsapp.com/')

        search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
        search_box = WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, search_box_xpath)))
        search_box.send_keys(p)
        search_box.send_keys(u'\ue007')

        message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        message_box = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, message_box_xpath)))
        message_box.send_keys(c)
        message_box.send_keys(u'\ue007')
        time.sleep(5)

        driver.quit()
        service.stop()
