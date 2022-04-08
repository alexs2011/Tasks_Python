import lxml.html
import requests

url = "https://coloredmanga.com/manga/dragon-ball-super/chapter-2/"

data = requests.get(url, timeout=10)

print(data.text)

# tree = lxml.html.document_fromstring(data)
