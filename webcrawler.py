import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://creativeworks.tistory.com/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        # print(plain_text)
        soup = BeautifulSoup(plain_text, 'lxml')
        for link in soup.select('a'):
            print("link : ", link)
            href = "http://creativeworks.tistory.com" + link.get('href')
            title = link.string
            print("href : ", href)
            print("title : ", title)
            print("="*30)

        page += 1

spider(11)
