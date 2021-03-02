#%%

import pandas as pd
import numpy as np
import bs4
import request

import openxl

import os

from selenium import webdriver
import time

os.getcwd()
os.chdir('C:/Users/)

#%%

# 경향신문 기사 크롤러

def kyung(url):
    url = url
       
    kh = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    kh_bs = bs4.BeautifulSoup(kh.text)

    con=kh_bs.find_all('p',class_='content_text')

    con1=[]
    for i in con :
        con1.append(i.text)

    con2=" ".join(con1)
    return con2

#%%
    
# 국민일보 기사 크롤러
    
def kukmin(url):
    url = url
    km = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    km_bs = bs4.BeautifulSoup(km.content.decode('euc-kr','replace'), 'html.parser')
    con=km_bs.find_all('div',class_="tx")

    con
    con1=[]
    con2=[]
    con3=[]
    for i in con :
        con1.append(i.text)

    for j in con1 :
        con2.append(j.replace("\n",""))

    for t in con2 :
        con3.append(t.replace("\t",""))

    return(con3)
    

#%%
    
# 내일신문 기사 크롤러
    
def neaill(url) :    
    url = url
    nea = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    nea_bs = bs4.BeautifulSoup(nea.content.decode('utf-8','replace'), 'html.parser')
    con=nea_bs.find_all('div',class_="article")

    con1=[]
    for i in con :
        con1.append(i.text)

    con2=" ".join(con1)
    con2 = con2.replace("\n","")
    con2=con2.replace("\r","")
    
    return(con2)
    
#%%
    
# 동아일보 기사 크롤러
    
def dong(a):

    url = a

    dong = requests.get(a, headers={"User-Agent": "Mozilla/5.0"})
    dong_bs=bs4.BeautifulSoup(dong.content, 'html.parser')
    con=dong_bs.find_all('div',class_="article_txt")

    con1=[]
    con2=[]
    for i in con :
        con1.append(i.text)

        con2=" ".join(con1)
        con2 = con2.replace("\n","")
        con2=con2.replace("\r","")
        
    return(con2)
    
#%%
    
# 문화일보 기사 크롤러
    
def mun(a):    
    
    url = a
    mun = requests.get(url)
    mun_bs = bs4.BeautifulSoup(mun.content.decode('euc-kr','replace'), 'html.parser')

    con=mun_bs.find_all('div',id='NewsAdContent')

    con1=[]
    for i in con :
        con1.append(i.text)

        con2=" ".join(con1)

    return(con2)

#%%
    
# 서울신문 기사 크롤러
    
def seoul(a) :
    url = a
    seoul = requests.get(url)
    seoul_bs = bs4.BeautifulSoup(seoul.content.decode('euc-kr','replace'), 'html.parser')

    con=seoul_bs.find_all('div',class_='S20_v_article')

    con1=[]
    con2=[]
    for i in con :
        con1.append(i.text)

        con2=" ".join(con1)
        con2 = con2.replace("\n","")
        con2=con2.replace("\r","")    

    return(con2)

#%%
    
# 세계일보 기사 크롤러
    
def sea(a):    
    url = a
    sea = requests.get(url)
    sea_bs = bs4.BeautifulSoup(sea.content.decode('utf-8','replace'), 'html.parser')

    con=sea_bs.find_all('div',itemprop='articleBody')

    con1=[]
    con2=[]
    for i in con :
        con1.append(i.text)

        con2="".join(con1)
        con2 = con2.replace("\n","")
        con2=con2.replace("\r","")    

    return(con2)
    
#%%
    
# 중앙일보 기사 크롤러
    
def jung(a):    
    url = a
    jung = requests.get(url)
    jung_bs = bs4.BeautifulSoup(jung.content.decode('utf-8','replace'), 'html.parser')

    con=jung_bs.find_all('div',id='article_body')

    con1=[]
    con2=[]
    for i in con :
        con1.append(i.text)

        con2="".join(con1)
        con2 = con2.replace("\n","")
        con2=con2.replace("\r","") 
        con2=" ".join(con2.split())

    return(con2)
    
#%%
    
# 한겨레 기사 크롤러
    
def han(a):   
    url = a
    han = requests.get(url)
    han_bs = bs4.BeautifulSoup(han.content.decode('utf-8','replace'), 'html.parser')

    con=han_bs.find_all('div',class_='text')

    con1=[]
    con2=[]
    for i in con :
        con1.append(i.text)

        con2="".join(con1)
        con2 = con2.replace("\n","")
        con2=con2.replace("\r","") 
        con2=" ".join(con2.split())

    return(con2)
    
#%%
    
# 한국일보 기사 크롤러
    
def hankook(a):
    
    url = a
    hankook = requests.get(url)
    hankook_bs = bs4.BeautifulSoup(hankook.content.decode('utf-8','replace'), 'html.parser')

    con=hankook_bs.find_all('p',class_="editor-p")

    con1=[]
    con2=[]
    for i in con :
        con1.append(i.text)

        con2="".join(con1)


    return(con2)


#%%
    
# 조선일보 기사 크롤러
    
def cho(a):
    time.sleep(3)
    driver = webdriver.Chrome('C:/Users/inolab/Desktop/chromedriver.exe')

    driver.get(a)
    time.sleep(3)
    con1=[]
    if a[-1]=='z' :
        
        con = driver.find_elements_by_class_name('par')
        con1=[]
        for i in con :
            con1.append(i.text)
        driver.close()
        
        return(con1[0])
    
    else :
        
        con = driver.find_element_by_class_name('article-body')
        con1 = con.text
        driver.close()
        
        return(con1)

#%%
        
    
    
