# Scrapes code from a file in github repo
# Does not work for readme, gradle files
# Confirmed works for py,js,.gitignore and other files
# If you feel bored to click 'raw' on github code but want to copy the url
# and print the output in console/terminal, use this lol.

import requests
from bs4 import BeautifulSoup

URL = "https://github.com/mui-org/material-ui/blob/next/examples/preact/package.json"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_="application-main").find(class_="repository-content").find_all('td')

for i in results:
	if (i.find('span')):
		print(i.text)