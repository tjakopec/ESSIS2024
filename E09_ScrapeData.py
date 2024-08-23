import concurrent.futures
from bs4 import BeautifulSoup
import requests
from lxml import etree

# find smart phone


def scrape_data(url):
    adresses = []
    try:
        page = requests.get(url, timeout=10)
        soup = BeautifulSoup(page.text, 'lxml')  # pip install lxml     | 'html.parser' is the build in one
        print(page.text)
        # Ispričavam se zbog neugodnosti
        #  ...ali tvoja aktivnost i ponašanje na ovoj web stranici naveli su me da mislim da si prešao na tamnu stranu.

        # I apologize for the inconvenience
        # ...but your activity and behavior on this website has led me to think that you have gone over to the dark side.

        dom = etree.HTML(str(soup))
        try:
            for element in dom.xpath('/html/body/div[12]/div[2]/div[1]/main/form/div/div[1]/div[6]/div[3]/ul'):
                print(element)
            else:
                pass
        except:
            pass
    except:
        pass


scrape_data('https://www.njuskalo.hr/iphone-15-pro?sort=cheap')



