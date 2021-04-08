import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import  re
from selenium.webdriver.common.keys import Keys
import  random

import pandas as pd

def crawl(url):
    data  = requests.get(url)
    print (data , url)
    return  data.content


def parser_for_homepage(pageString):
    bsObj = BeautifulSoup(pageString,"html.parser")
    table = bsObj.find("table")
    return table

def parser_for_reviews(pageString):
    bsObj = BeautifulSoup(pageString,"html.parser")
    return bsObj

def get_text(url):
    pageString = crawl(url)
    obj= BeautifulSoup(pageString, "html.parser")
    context = obj.find("dd").text
    context = context.replace('\n','')
    context = context.replace('\t', '')
    context = context.replace('\r', '')
    context = context.replace('\xa0', ' ')
    head = obj.find("dt")
    title = head.find("p").get_text()
    date = head.find_all("span")[0].get_text()
    id = head.find_all("span")[1].get_text()
    return {"id": id, "date": date, "title": title, "content": context.strip() }


def get_url(pageNo):
    homepage = "https://www.bikeseoul.com/customer/opinionBoard/opinionBoardList.do?currentPageNo={}".format(pageNo)

    pageString = crawl(homepage)
    post_url = "https://www.bikeseoul.com"
    links = []
    obj1 = parser_for_homepage(pageString)
    for link in obj1.find_all('a'):
         links.append(post_url+link.get('href'))
    return links
#homepage = "https://www.bikeseoul.com/customer/opinionBoard/opinionBoardList.do?currentPageNo={}".format(pageNo)
href_list = []
for pageNo in range(1,1731):
    href_list= href_list+ get_url(pageNo)
print(len(href_list))




reviewsInfos = []
for opinion in href_list:
    reviews = get_text(opinion)
    reviewsInfos.append(reviews)

def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()

df = pd.DataFrame(data=reviewsInfos)
save(df, "./Seoulbike_complain.xlsx")
print(df.count())