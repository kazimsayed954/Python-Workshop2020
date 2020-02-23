from bs4 import BeautifulSoup
import requests
import csv

data =open("books.csv","w")
writer=csv.writer(data)
header=['Book image','Book title','Price']
writer.writerow(header)
num=1
for page in range(0,51):
    source=requests.get(f'http://books.toscrape.com/catalogue/page-{page}.html').text
    #print(source)
    soup=BeautifulSoup(source,'lxml')
    #print(soup.prettify())

    '''in beautiful soup find return only single elements 
    whereas find_all method gives a list as compare to request'''

    book=soup.find_all('li',class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    #title=book.article.h3.a.attrs['title']
    #print(book.prettify())
    #print(book)

    books_title=soup.find_all('li',class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        
    price=soup.find_all(class_="price_color")

    image=soup.find_all(class_="thumbnail")
    #print(f'http://books.toscrape.com/{image}')

    '''
    Attribute dindt have text as well as find_all method
    '''
    
    for i in range(0,len(price)):
        print(f"http://books.toscrape.com/{image[i].attrs['src']}")
        print(num,":",books_title[i].article.h3.a.attrs['title'])
        print(price[i].text)
        li=[f"http://books.toscrape.com/{image[i].attrs['src']}",books_title[i].article.h3.a.attrs['title'],price[i].text]
        print()
        writer.writerow(li)
        num+=1

