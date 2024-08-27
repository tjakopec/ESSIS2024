from bs4 import BeautifulSoup
import requests
from w3c_validator import validate  # pip install -U Online-W3C-Validator


# good: https://github.com/sethblack/python-seo-analyzer


def scrape_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')  # pip install lxml     | 'html.parser' is the build in one

    print(soup.prettify())
    print(soup.get_text())

    print('Investigate title')
    print('soup.title', soup.title)
    print('soup.title.name', soup.title.name)
    print('soup.title.string', soup.title.string)
    print('soup.title.parent.name', soup.title.parent.name)

    # is page valid to W3C
    messages = validate(url)['messages']
    if len(messages) == 0:
        print('Page IS W3C valid')
    else:
        for m in messages:
            print("Type: %(type)s, Line: %(lastLine)d, Description: %(message)s" % m)

    for link in soup.findAll('a'):
        href = link.get('href').strip()
        if href.startswith('http'):
            print(href)


'''
    tags = soup.find_all()
    for tag in tags:
        if tag.string is not None:
            print(tag.name, '->', tag.string)
'''

# crawl_data('https://duco-projekt.hr/')

scrape_data('https://oziz.ffos.hr/nastava20232024/dlaslo_23/vjezba1zadatak2.html')

# student task: investigate three URL. Select the URL according to your choice
