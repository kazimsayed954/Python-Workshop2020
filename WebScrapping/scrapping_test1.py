import requests
from requests_html import HTMLSession
import csv

session=HTMLSession()
req=session.get('https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs')
Title=req.html.find('.overview-top h4 ')
for title in Title:
    print(title.text)
    print()

discription=req.html.find('.overview-top .outline ')
for dis in discription:
    print(dis.text)
    print()

stars=req.html.find('.overview-top .txt-block ')
for str in stars:
    print(str.text)
    print()


Poster=req.html.find('.hover-over-image img')
for img in Poster:
    print(img.attrs['src'])