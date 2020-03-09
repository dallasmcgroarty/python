import sqlite3
import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)
    save_books(all_books)

def save_books(all_books):
    conn = sqlite3.connect("SQL/books.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, price REAL, rating INTEGER)")

    if c.executemany("INSERT INTO books VALUES (?,?,?)", all_books):
        print("Books successfully added to database!")
    else:
        print("Error inserting into database")

    conn.commit()
    conn.close()

def get_title(book):
    return book.find("h3").find("a")["title"]

def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price[2:])

def get_rating(book):   
    ratings = {"Zero":0, "One":1,"Two":2,"Three":3,"Four":4,"Five":5}
    paragraph = book.select(".star-rating")[0]
    word = paragraph.get_attribute_list("class")[-1]
    return ratings[word]


scrape_books("http://books.toscrape.com/catalogue/category/books/history_32/index.html")