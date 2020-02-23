from bs4 import BeautifulSoup
import requests
import csv

#for page in range(0,9):
    #source=requests.get(f"http://quotes.toscrape.com/page/{page}/").text
source=requests.get("http://quotes.toscrape.com").text
soup=BeautifulSoup(source,'lxml')
qoutes=soup.find_all(class_="text")
links=soup.find(class_="text")
author=soup.find_all(class_="author")
tags=soup.find_all(class_="tags")
for quo in qoutes:
    print(quo.text)
    

for auth in author:
    print(auth.text)
for tag in tags:
    print(tag.text)

print(links.a.attrs['href'])
