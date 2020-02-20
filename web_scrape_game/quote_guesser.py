import requests
import random
from bs4 import BeautifulSoup
from csv import DictReader

base_url = 'http://quotes.toscrape.com'

def read_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

def get_hints(bio_link, author, guesses):
    res = requests.get(f"{base_url}{bio_link}")
    soup = BeautifulSoup(res.text, "html.parser")

    if guesses == 3:
        birthdate = soup.find(class_='author-born-date').get_text()
        birthplace = soup.find(class_='author-born-location').get_text()
        print(f"Here's a hint: The author was born on {birthdate} {birthplace}")
    elif guesses == 2:
        print(f"Here's a hint: The author's first name starts with {author[0]}")
    elif guesses == 1:
        last = author.split(' ')[1][0]
        print(f"Here's a hint: The author's first name starte with {last}")
    else:
        print(f"Sorry you ran out of guesses. The answer was {author}")

def guess_quote(quotes):
    remaining_guesses = 4
    quote = random.choice(quotes)
    print("Here's a qoute:")
    print(quote["text"])
    print(quote["author"])
    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")
        if guess.lower() == quote["author"].lower():
            print('YOU GOT IT RIGHT')
            break

        remaining_guesses -= 1

        get_hints(quote['bio-link'],quote["author"],remaining_guesses)
        
    again = ''
    while again.lower() not in ('y','yes','n','no'):
        again = input('Would you like to play again? (y/n)')
    if again.lower() in ('yes','y'):
        guess_quote(quotes)
    else:
        print('Thanks for playing!')

quotes = read_quotes('web_scrape_game/quotes.csv')
guess_quote(quotes)