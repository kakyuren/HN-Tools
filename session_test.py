#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import requests
import json


ny_url= "https://ny-gateway.chngdz.com/platform/cert_truck/list?size=20&page=1&certStatus=authenticating"
login_url="https://ny.chngdz.com/login/login.html"
header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
#ve_url
options= webdriver.ChromeOptions()
#options.add_argument('detach=true')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path ='chromedriver.exe',chrome_options=options)
s = requests.session()

data = {
    "size": 20,
    "page": 1,
    "certStatus": "authenticating"
}

def login(url):
    header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

    #driver = webdriver.Chrome(executable_path ='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',chrome_options=options)
    driver.get(url)
    driver.find_element_by_name("account").send_keys("13655179351")
    driver.find_element_by_name("password").send_keys("ren1982")
    driver.find_element_by_tag_name("button").click()
    cookie = driver.get_cookies()
    return cookie

def add_cookies(cookie):
    cr = requests.cookies.RequestsCookieJar()
    for i in cookie:    #添加cookie到CookieJar
        cr.set(i["name"], i["value"])
    print(cr)
    s.cookies.update(cr) 
    print(s.cookies)


cookie=login(login_url)
add_cookies(cookie)
time.sleep(5)
ny=requests.get(ny_url)

#dicinfo = json.loads(ny.text)
#print(dicinfo)
print(ny.text)
driver.close()
