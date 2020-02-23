
import requests
from requests_html import HTMLSession
import csv
session=HTMLSession()

req=session.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
code=req.html.find('h1',first=True)
art=req.html.find('.titleColumn')
para=req.html.find('p')
#poster=req.html.find('.posterColumn img')
print(code.text)
lis=[]
'''for article in art:
    print(article.text)
    '''
'''for p in para[0:6]:
    print(p.text)'''
    
#for img in poster:
 #   print(img.url)
Rating=req.html.find('.ratingColumn strong')

for i in range(0,len(art)):
    print(art[i].text,end=" ")
    print(Rating[i].text)

poster=req.html.find('.posterColumn img')
#for i in poster:
     #print(i.attrs['src'])
     #print()

for i in range(0,len(poster)):
    print(poster[i].attrs['src'])
    print(art[i].text,end=" ")
    print(Rating[i].text)

#creating a file 
data=open('MovieData.csv','w')
writer=csv.writer(data)

#creating a header row
header=['Title','Rating','Poster URL']
writer.writerow(header)

for i in range(0,len(art)):
    list=[art[i].text,Rating[i].text,poster[i].attrs['src']]
    writer.writerow(list)