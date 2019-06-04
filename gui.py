#coding=utf-8

from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.select import Select
import time
import requests
import json


url= "http://sso.logink.org/index.do?resourceID=120380A218FC003EE053C0A87F0C003E"
vehicle_info_result={}
people_info_result={}
options= webdriver.ChromeOptions()
options.add_argument('detach=true')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path ='chromedriver.exe',chrome_options=options)


def login(url):
    header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

    #driver = webdriver.Chrome(executable_path ='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',chrome_options=options)
    driver.get(url)
    driver.find_element_by_id("username").send_keys("25991")
    driver.find_element_by_id("password").send_keys("js5320739")
    driver.find_element_by_id("button").click()

def ent_check(en):
    response=requests.post("http://credit.logink.org/gateway/entQry!query.htm",data={"enterpriseName": en,"provinceCode":"360000"})
    dicinfo = json.loads(response.text)
    if(dicinfo['result']):
      for k,v in dicinfo['data'].items():
         if(k=='ent'):
            pn=v.get('permitNumber')
            vehicle_info_result['运输经营许可证号']=pn

def vehicle_check(text):
    response=requests.post("http://credit.logink.org/gateway/vehQry!query.htm",data={"vehicleNumber": text,"licensePlateTypeCode":"黄色"})
    dicinfo = json.loads(response.text)
    #print(type(dicinfo['result']))

    try:
      if(dicinfo['result']):
         for k,v in dicinfo['data'].items():
            #  print(v)
            if(k=='rtcs'):
               vn=v[0].get("vehicleNumber")
               rc=v[0].get("roadTransportCertificateNo")
               vl=v[0].get("vehicleLength")
              # vw=v[0].get("vehicleTonnage")
               vw=dicinfo['data']['vehicleTonnage']
               en=v[0].get("enterpriseName")
               vehicle_info_result['车牌号']=vn
               vehicle_info_result['车长']=vl
               #vehicle_info_result['车辆载重']=vw
               vehicle_info_result['载重']=vw
               vehicle_info_result['道路运输证号']=rc
               vehicle_info_result['所有人(业户名称)']=en
               ent_check(en)
               return vehicle_info_result
      else: 
         return dicinfo['errMsg']
    except:
         return "未知错误，请重试或退出！"


def people_check(name,idno):
    response=requests.post("http://credit.logink.org/gateway/perQry!query.htm",data={"nameOfPerson":name,"identityDocumentNumber":idno,"provinceCode":"360000"})
    dicinfo = json.loads(response.text)
    #print(type(dicinfo['result']))
    try:
      if(dicinfo['result']):
         for k,v in dicinfo['data'].items():
            #  print(v)
            if(k=='qcs'):
               qn=v[0].get("qualificationCertificateNo")
               people_info_result['从业资格证号']=qn
               return people_info_result
      else: 
         return dicinfo['errMsg']
    except:
         return "未知错误，请重试或退出！"

def close_driver(dr):
      dr.quit()

