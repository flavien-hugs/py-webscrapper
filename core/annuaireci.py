import requests
from bs4 import BeautifulSoup


def get_annuaireci_data():
    annuaireci = requests.get("https://www.annuaireci.com/cote-divoire/fr-FR/search?a=Bouake")
    content = BeautifulSoup(annuaireci.content, "html.parser")
    return content.find("main", class_="SearchResults-results")


def get_annuaireci_element():
    return get_annuaireci_data().find_all("article", class_="SearchResult")


def annuaireci():
    for element in get_annuaireci_element():

        title = element.find("h3", class_="SearchResult-title")
        title = f"company: {title.text.strip()}"

        location = element.find("small", class_="SearchResult-location")
        location = f"location: {location.text.strip()}"

        category = element.find("a", class_="BusinessProfile-category")
        category = f"category: {category.text.strip()}"

        phone = element.find("a", class_="SearchResult-footerBtn")
        phone = f"phone: {phone.text.strip()}"

        web = element.find("span", class_="SearchResult-btnText")
        web = f"website: {web.text.strip()}"

        print(title, "\n", location, "\n", category, "\n", phone, "\n", web, "\n")


if __name__ == '__main__':
    annuaireci()
