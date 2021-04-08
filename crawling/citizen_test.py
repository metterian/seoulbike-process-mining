import csv
import requests
from bs4 import BeautifulSoup
with open('/Users/seungjun/PycharmProjects/python_project/seoulbike/href_list.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    href = []
    for row in reader:
        href.append(row['href'])

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




def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()




reviewsInfos = []
for opinion in href:
    try :
        reviews = get_text(opinion)
    except:
        pass
    try:
        reviewsInfos.append(reviews)
    except NameError:
        pass

df = pd.DataFrame(data=reviewsInfos)
df.to_csv('Seoulbike_complaint.csv')
