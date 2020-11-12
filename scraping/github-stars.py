# Todo: Use selenium to click to go to a new page if there are more starred projects than what ia available in the first page
# Currently, it scrapes the repo name, and the link to the repo and saves in the file starred.md in the same directory.

import requests
from bs4 import BeautifulSoup

URL = "https://github.com/chiphuyen?tab=stars"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all(class_="col-12 d-block width-full py-4 border-bottom")

f = open("starred.md", "a")
f.write('## List of starred repositories \n')

for i in results:
	blocks = i.find(class_="d-inline-block mb-1")
	repo = blocks.find_all('a')
	for x in repo:
		f.write('- [**{}**](https://github.com{})\n'.format(x.text.replace(' ','').replace('\n',''),x['href']))		