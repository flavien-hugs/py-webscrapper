# scrip web scrapping website

import requests
from bs4 import BeautifulSoup


def get_data():
    page = requests.get("https://www.freecodecamp.org/news/")
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="site-main")
    return results


def get_elements():
    elements = get_data().find_all("article", class_="post")
    return elements


def get_context_data():
    for element in get_elements():

        title_element = element.find("h2", class_="post-card-title")
        title_element = title_element.text.strip()

        author_element = element.find("a", class_="meta-item")
        author_element = author_element.text.strip()

        time_element = element.find("time", class_="meta-item")
        time_element = time_element.text.strip()

        print(title_element)
        print(author_element)
        print(time_element)
        print()
