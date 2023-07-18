"""
Дз
1. Получить данные из вебсайта: https://www.vox.com/technology/archives 
Данные:
- название статьи
- ссылку к статье
- кем написан 
- дата написания

сделать также поддержку пагинации.
"""

import requests
from bs4 import BeautifulSoup


def parse_vox():    
    results = []
    for page in range(1, 4):
        url = f'https://www.vox.com/technology/archives/?p={page}'
        res = requests.get(url)
        soup = BeautifulSoup(
            res.text, 'html.parser'
        )
    
    articles = soup.find_all(class_='titleline')

    for article in articles:
        title = article.find('h3').text.strip()
        link = article.find('a')['href']
        author = article.find('div', class_='c-byline').find('a').text.strip()
        date = article.find('div', class_='c-byline__item').text.strip()
        
        results.append({
            'title': title,
            'link': link,
            'author': author,
            'date': date
        })
        
    return results

for arcticle in ():
    print(f"Название статьи: {article['title']}")
    print(f"Ссылка на статью: {article['link']}")
    print(f"Автор: {article['author']}")
    print(f"Дата написания: {article['date']}")
    print('---')