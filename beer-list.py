import sys
import requests
import csv
from bs4 import BeautifulSoup
beerwriter = csv.writer(sys.stdout)

try:
    text = open('pouring.html', 'rb').read().decode('utf8')
except:
    asdf
    r = requests.get('http://farmhousefest.com/2019/pouring/')
    text = r.text
    open('pouring.html', 'w').write(text)

soup = BeautifulSoup(text, 'html.parser')
beer_list = soup.find_all('ul', class_='beer-list')
assert(len(beer_list) == 1)
beer_list = beer_list[0]
breweries = beer_list.find_all('li', recursive=False)
for brewery in breweries:
    brewery_name = brewery.find('h3').get_text()
    pouring = soup.find_all('ul', class_='pouring')
    for beer in pouring:
        beer_name = beer.find('h4').get_text()
        try:
            beer_abv = beer.find('p', class_='abv').get_text()
        except:
            beer_abv = '?'
        try:
            beer_desc = beer.find('p', class_='desc').get_text()
        except:
            beer_desc = ''
        beerwriter.writerow((brewery_name, beer_name, beer_abv, beer_desc))



