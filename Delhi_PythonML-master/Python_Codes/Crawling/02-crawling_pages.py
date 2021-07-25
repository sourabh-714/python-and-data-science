import bs4
import urllib.request as url

for i in range(1,5):
    path = "https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}".format(i)
    res = url.urlopen(path)
    print(".................Page_{}................".format(i))
    page = bs4.BeautifulSoup(res,'html.parser')
    titleList = page.find_all('div',class_='_3wU53n')
    priceList = page.find_all('div', class_='_1vC4OE _2rQ-NK')

    for j in range(len(titleList)):
        print(titleList[j].text)
        print(priceList[j].text)
        print('*'*20)


