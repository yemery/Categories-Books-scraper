from lxml import html
from bs4 import BeautifulSoup
import requests
import numpy as np
import time
import requests
import csv
from termcolor import colored
import json
import re
from collections import OrderedDict

def getCategories():
    catsList=[]
    URL="https://www.thriftbooks.com/sitemap/"
    r=requests.get(URL)
    soup=BeautifulSoup(r.content,'html5lib')
    # print(soup.prettify())
    catNames=soup.find_all('div',{'class':"SiteMap-Header"})
    for i in catNames[0:-3]:
        # print(i.text.strip())
        catsList.append(i.text.strip())
    return catsList



def catCSVfile(catArr):
    catListObj=[]
    for i in range(len(catArr)):
        catDict={}
        catDict['id']=i
        catDict['name']=catArr[i]
        catListObj.append(catDict)
    with open("books_cats.csv", 'w',encoding="utf-8") as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames =['id','name']) 
        writer.writeheader() 
        # writing data rows 
        writer.writerows(catListObj) 
        print(colored("added secc...\n",'blue'))
print(catCSVfile(getCategories()))
# print(getCategories())



