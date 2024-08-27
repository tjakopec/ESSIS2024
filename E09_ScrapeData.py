import concurrent.futures
from bs4 import BeautifulSoup
import requests
from lxml import etree

# find smart phone


def scrape_data(url, xpath):
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
            for element in dom.xpath(xpath):
                print(element)
            else:
                pass
        except:
            pass
    except:
        pass


# scrape_data('https://www.njuskalo.hr/iphone-15-pro?sort=cheap','/html/body/div[12]/div[2]/div[1]/main/form/div/div[1]/div[6]/div[3]/ul')


scrape_data('https://www.index.hr/oglasi/mobiteli/iphone/15/pretraga?searchQuery=%257B%2522category%2522%253A%2522iphone%2522%252C%2522categoryLv1Ids%2522%253A%255B%2522ad7a8aeb-6394-4dbe-a102-8b3850873866%2522%255D%252C%2522module%2522%253A%2522mobiteli%2522%257D',
            '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]')
# You need to enable JavaScript to run this app. - we need emulation of browser


# student task: try to find item you want to buy on website that you usually buy items


