import urllib.request as url
import bs4

movie = input("Enter movie name : ")
response = url.urlopen("https://www.imdb.com/find?q={}".format(movie))
page = bs4.BeautifulSoup(response, 'lxml')

td = page.find('td', class_='result_text')
a_tag = td.find('a')
href = a_tag.attrs['href']

response = url.urlopen("https://www.imdb.com" + href)
page = bs4.BeautifulSoup(response, 'lxml')
title = page.find("h1")
print(title.text)

subtext = page.find("div", class_='subtext')
subtext = subtext.text.split()
subtext = ' '.join(subtext)
print(subtext)

