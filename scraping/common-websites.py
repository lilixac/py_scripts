import requests
from bs4 import BeautifulSoup

URL = 'https://www.alexa.com/topsites'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all(class_="tr site-listing")
for j,i in enumerate(results):
    name = i.find(class_="td DescriptionCell").find('p').find('a')
    print('{}. {}'.format(j+1, name.text))