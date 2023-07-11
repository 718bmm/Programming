import requests
from bs4 import BeautifulSoup
import re
import pprint

url = "https://news.ycombinator.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser") # parses the code and returns BeautifulSoap
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)

print(soup.span)
print(soup.span["class"])
print(soup.span.attrs)
print(soup.a.attrs)

print(soup.find_all('a'))
print("values\n\n\n\n")

title = soup.find_all(class_="titleline")
print(title)
link_to_arcticle = title.a["href"]

print(title.a.text)
print(title.a["href"])
print(title.a.find(href="score_34491704"))

score = soup.find_all