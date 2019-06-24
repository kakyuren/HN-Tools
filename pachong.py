#coding=utf-8
import warnings
import time
import requests
import json
from requests.cookies import RequestsCookieJar
import os

warnings.filterwarnings("ignore")
jsid=input("输入JSESSIONID:")
url= "https://ny.chngdz.com/login/login.html"
yundan_url="https://ny-gateway.chngdz.com/waybill/waybill/outsourcing_list?size=20&page=1&waybillNo="
header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
cd={'JSESSIONID':jsid};
requests.adapters.DEFAULT_RETRIES =5 
s = requests.Session()
s.keep_alive = False

def get_list(i=0):
    f = open("./list.txt","r") 
    lines = f.read().splitlines()
    for line in lines:
        if len(line) != 0:
            print("--------------------------------------")
            a=s.get(yundan_url+line,cookies=cd)
            b=json.loads(a.text)
            waybillNo=b.get("content")[0].get("waybillNo")
            loadingAttachment=b.get("content")[0].get("loadingAttachment")
            unloadingAttachment=b.get("content")[0].get("unloadingAttachment")
            loadimgs(loadingAttachment,waybillNo)
            unloadimgs(unloadingAttachment,waybillNo)
            i=i+1
            print("已抓取%d个运单信息" % i)
        


def loadimgs(lamt,wbn):
    if(lamt):
        new_lamt=lamt.split(':')
        postfix=1
        for num in new_lamt:
            load_rp=s.get("https://ny-gateway.chngdz.com/waybill/fw/image/"+num+"/get",cookies=cd,headers=header)
            b=json.loads(load_rp.text)
            loadimgsurl=b.get("content").get("thumbnailList")[0].get("url")
            dowload_loadingimgs(loadimgsurl,wbn,postfix)
            postfix=postfix+1
    else:
        print(wbn+"     "+"发货凭证"+"     "+"缺失") 
        False

def unloadimgs(ulamt,wbn):
    if(ulamt):
        new_ulamt=ulamt.split(':')
        postfix=1
        for num in new_ulamt:
            load_rp=s.get("https://ny-gateway.chngdz.com/waybill/fw/image/"+num+"/get",cookies=cd,headers=header)
            b=json.loads(load_rp.text)
            unloadimgsurl=b.get("content").get("thumbnailList")[0].get("url")
            dowload_unloadingimgs(unloadimgsurl,wbn,postfix)
            postfix=postfix+1
    else:
        print(wbn+"     "+"收货凭证"+"     "+"缺失") 
        False


def dowload_loadingimgs(url,wbn,postfix):
    path1='./凭证数据/'+wbn+'/发货凭证'
    postfix=str(postfix)
    isExists=os.path.exists(path1)

    if not isExists:
        os.makedirs(path1) 

    r = s.get(url,verify=False, stream=True)
    #chunk_size = 1024  # 单次请求最大值
    #content_size = int(r.headers['content-length'])  # 内容体总大小
    data_count = 0
    with open(path1+'/'+postfix+'.png','wb') as f:
        f.write(r.content)

    print(wbn+"     "+"发货凭证"+"     "+"成功")                    

def dowload_unloadingimgs(url,wbn,postfix):
    path2='./凭证数据/'+wbn+'/收货凭证'
    postfix=str(postfix)
    isExists=os.path.exists(path2)

    if not isExists:
        os.makedirs(path2) 

    r = s.get(url,verify=False, stream=True)
    with open(path2+'/'+postfix+'.png','wb') as f:
       f.write(r.content)  
    print(wbn+"     "+"收货凭证"+"     "+"成功")  

if __name__ == "__main__":
    get_list()
    input("按任意键退出！")


