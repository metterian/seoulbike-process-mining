import requests
from bs4 import BeautifulSoup
import pandas as pd
def crawl(url):
    data  = requests.get(url)
    print (data , url)
    return  data.content

def getLocationInfo(tr0):
    td  = tr0.find("a")
    tdtext = td.text.replace("\t" ,"")
    tdtext1 = tdtext.replace("\n","")
    tdtext2 = tdtext1.replace("\r","")

    return {"content": tdtext2, "ID":"",}

def parser(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    table = bsObj.find("table")
    tr = table.findAll("tr")
    #tds = tr.find("td", {"class":"left"})
    locationInfos = []
    for i in range(1,6):

        LocationInfo = getLocationInfo(tr[i])
        locationInfos.append(LocationInfo)

    return locationInfos
productsInfos = []
def crawlPage (pageNo):
    url = "https://www.bikeseoul.com/customer/opinionBoard/opinionStationBoardList.do?currentPageNo={}".format(pageNo)
    pageString = crawl(url)
    locations = parser(pageString)
    return locations
result = []
for pageNo in range(1,2027):
    result = result + crawlPage(pageNo)
print(len(result))

def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()

df = pd.DataFrame(data= result)
save(df, "./seoulbike_location.xlsx")
print(df)