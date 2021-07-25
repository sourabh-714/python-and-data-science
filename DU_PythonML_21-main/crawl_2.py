import urllib.request as url
import bs4

response = url.urlopen("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")
page = bs4.BeautifulSoup(response, 'lxml')

'''
title = page.find('h3', class_='lister-item-header')
print(title.text)
'''
titles = page.find_all('h3', class_='lister-item-header')
for item in titles:
    print(item.text)
    print("*" * 30)
