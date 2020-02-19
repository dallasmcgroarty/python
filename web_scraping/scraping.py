# scrape data into CSV
# grab all links from rithm school blog
# store url, anchor tag text and date

import requests
from bs4 import BeautifulSoup
from csv import writer

def web_crawl(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all('article')

    with open('web_scraping/blog_data.csv', 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow(["title","link","date"])

        for article in articles:
            a_tag = article.find('a')
            title = a_tag.get_text()
            a_url = a_tag['href']
            date = article.find('time')['datetime']
            csv_writer.writerow([title, a_url, date])

    try:
        next_page = soup.find(class_ = 'current').find_next_sibling().find('a')['href']
    except:
        exit()

    next_page = next_page[5:]

    print(next_page)

    if url[-1].isdigit():
        next_url = url[:-1] + next_page[-1]
    else:
        next_url = url + next_page

    web_crawl(next_url)

    return
    
web_crawl('https://www.rithmschool.com/blog')