import bs4
import urllib.request as url

prod_name = input("Enter the product : ")
prod_name = prod_name.replace(' ', '+')
response = url.urlopen("https://www.flipkart.com/search?q={}&as=on&as-show=on".format(prod_name))
page = bs4.BeautifulSoup(response,"html.parser")

titles = page.find_all('div', class_='_3wU53n')
for item in titles:
    print(item.text)

