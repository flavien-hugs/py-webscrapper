import csv
import requests
from time import sleep
from warnings import warn
from random import randint
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Flavien HUGS, flavienhugs.one',
    'From': 'flavienhugs@pm.me'
}

URL = "https://www.freecodecamp.org/news/"

def get_freecodecamp_data():
    response = requests.get(URL, headers=headers)
    sleep(randint(5, 10))
    if response.status_code != 200:
        warn(f'Request: {requests}; Status code: {response.status_code}')

    page_html = BeautifulSoup(response.content, "html.parser")
    page_html_id = page_html.find(id="site-main")
    return page_html_id


def get_freecodecamp_element():
    data = get_freecodecamp_data()
    return data.find_all("article", attrs={"class": "post-card"})


def freecodecamp():

    file = csv.writer(open('data/freecodecamp.csv', 'w'))
    file.writerow(['title', 'author', 'published'])

    for element in get_freecodecamp_element():

        title = element.find("h2", class_="post-card-title")
        title = title.text.strip()

        author = element.find("a", class_="meta-item")
        author = author.text.strip()

        published = element.find("time", class_="meta-item")
        published = published.text.strip()

        file.writerow([title, author, published])

        print(title, "\t\n", author, "\t\n", published, "\t\n")


if __name__ == '__main__':
    freecodecamp()
