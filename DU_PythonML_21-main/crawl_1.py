import urllib.request as url
import bs4

response = url.urlopen("https://www.imdb.com/title/tt0848228/?ref_=fn_al_tt_1")
page = bs4.BeautifulSoup(response, 'lxml')

title = page.find("h1")
print(title.text)

subtext = page.find("div", class_='subtext')
subtext = subtext.text.split()
subtext = ' '.join(subtext)
print(subtext)
