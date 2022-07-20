from bs4 import BeautifulSoup
import requests
from csv import writer



url = 'https://www.pararius.com/apartments/rotterdam'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_='listing-search-item')

with open('housing02.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    hader = ['Title', 'location', 'price', 'area']
    thewriter.writerow(hader)

    for list in lists:
        title = list.find('a', class_="listing-search-item__link listing-search-item__link--title").text.replace('\n', '')
        location = list.find('div', class_="listing-search-item__location").text.replace('\n', '')
        price = list.find('div', class_="listing-search-item__price").text.replace('\n', '')
        area = list.find('li', class_="illustrated-features__item illustrated-features__item--surface-area").text.replace('\n', '')
        info = [title, location, price, area]
        thewriter.writerow(info)