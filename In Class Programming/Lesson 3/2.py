import requests
from bs4 import BeautifulSoup

search = "food"
url = "https://en.wikipedia.org/wiki/Deep_learning"
source_code = requests.get(url)
text = source_code.text
soup = BeautifulSoup(text, "html.parser")
print(soup.title.text)
results = soup.findAll('a')
for link in results:
    href = link.get('href')
    print(href)
