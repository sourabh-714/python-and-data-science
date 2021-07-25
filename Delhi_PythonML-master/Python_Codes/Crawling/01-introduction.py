import bs4
import urllib.request as url

# makes a http request
response = url.urlopen("https://www.flipkart.com/search?q=red+mi+note+6&as=on&as-show=on")
# returns a http response

page = bs4.BeautifulSoup(response,"html.parser")

# page.find('div',attrs={'class':'_3wU53n'})
# title = page.find('div', class_='_3wU53n')
# print(title.text)

titles = page.find_all('div', class_='_3wU53n')
for item in titles:
    print(item.text)

