import requests
from bs4 import BeautifulSoup
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

def get_url(pageNo):
    homepage = "https://www.bikeseoul.com/customer/opinionBoard/opinionBoardList.do?currentPageNo={}".format(pageNo)

    pageString = crawl(homepage)
    post_url = "https://www.bikeseoul.com"
    links = []
    obj1 = parser_for_homepage(pageString)
    for link in obj1.find_all('a'):
         links.append(post_url+link.get('href'))
    return links

href_list = []
for pageNo in range(1,2027):
    href_list= href_list+ get_url(pageNo)

def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()

data = {"href": href_list}
df = pd.DataFrame(data=data)
#save(df, "./complain_list.xlsx")
df.to_csv('href_list.csv')