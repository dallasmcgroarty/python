import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

base_url = 'http://quotes.toscrape.com'
url = '/page/1'

def get_quotes(base_url, url):
    all_quotes = []
    while url:
        response = requests.get(f"{base_url}{url}")
        print(f"Now scraping {base_url}{url}")
        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all(class_='quote')

        for card in cards:
            all_quotes.append({
                "text": card.find(class_='text').get_text(),
                "author": card.find(class_='author').get_text(),
                "bio-link": card.find('a')["href"]
            })
        
        next_btn = soup.find(class_='next')
        url = next_btn.find('a')['href'] if next_btn else None
        sleep(2)
    return all_quotes

def write_quotes(quotes):
    with open('web_scrape_game/quotes.csv', 'w', encoding='utf-8') as file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = get_quotes(base_url, url)
write_quotes(quotes)
