# reading lists from humble bundle bundles
import json
from bs4 import BeautifulSoup


topic = ""      # add manually
publisher = ""  # add manually
html = """  """   # paste site HTML here

def get_books(html)
    soup = BeautifulSoup(html)
    titles = soup.find_all(class_="front-page-art-image-text")
    subtitles = soup.find_all('div', class_='subtitle')
    if subtitles:
        books = list(zip(titles, subtitles))
    else:
        books = titles
    return books

def add_to_list(topic, books, publisher):
    new_reads = dict()
    new_reads[topic] = {'publisher': publisher, 'books': books}

    with open('books.json', 'r+') as f:
        old_reads = json.load(f)
        reads = {**old_reads, **new_reads}
        json.dump(reads, f)


if __name__ == '__main__':
    books = get_books(html)
    add_to_list(topic, books, publisher)
