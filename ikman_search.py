from bs4 import BeautifulSoup
import requests

page = 1
ads = []
min_price = 0
max_price = 10000
print(f'page 1 loading..........')
html_text = requests.get(f'https://ikman.lk/en/ads/sri-lanka?sort=relevance&buy_now=0&urgent=0&query=19%20monitor&page=1').text
soup = BeautifulSoup(html_text, 'lxml')
pages_element = soup.find('span', {'class': 'ads-count-text--1UYy_'}).text
pages = round(int(pages_element.split(' ')[3].replace(',', '')) / 25)
print(f'total pages: {pages}')

def process(soup, i):
    try:
        ad_list = soup.find('ul', {'class': 'list--3NxGO'}).find_all('li', {'class': 'normal--2QYVk gtm-normal-ad'})
            
        for ad in ad_list:
            price = ad.find('div', {'class': 'price--3SnqI color--t0tGX'}).find('span').text
            price = int(price.split(' ')[1].replace(',', ''))
            if price <= max_price and price > 0:
                name = ad.find('h2', {'class': 'heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow'}).text
                location = ad.find('div', {'class': 'description--2-ez3'}).text.split(' ')[0].replace(',', '')
                time = ad.find('div', {'class': 'updated-time--1DbCk'}).text
                
                ads.append({'name': name, 'location': location, 'time': time, 'price': price, 'page': i})
    except AttributeError:
        pass
    
def printV(ads):
    print(f'there are {len(ads)} filtered ads \n')
    for ad in ads:
        print('Name: ', {ad['name']})
        print('Location: ', {ad['location']})
        print('Time: ', {ad['time']})
        print('Price: ', {ad['price']})
        print('Page: ', {ad['page']})
        print('\n')


process(soup, 1)

for i in range(2, pages):
    print(f'page {i} loading..........')
    html_text = requests.get(f'https://ikman.lk/en/ads/sri-lanka?sort=relevance&buy_now=0&urgent=0&query=laptop&page={i}').text
    soup = BeautifulSoup(html_text, 'lxml')
    process(soup, i)

        
printV(ads)