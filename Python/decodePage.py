import requests
from bs4 import UnicodeDammit, BeautifulSoup

dammit = UnicodeDammit
url = 'http://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
for title in soup.find_all('article class="story"'):
    print title