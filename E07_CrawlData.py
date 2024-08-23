import concurrent.futures
from bs4 import BeautifulSoup
import requests

# Find all adresses


def crawl_data(url):
    adresses = []
    try:
        page = requests.get(url, timeout=10)
        soup = BeautifulSoup(page.text, 'lxml')  # pip install lxml     | 'html.parser' is the build in one
        for adress in soup.findAll('address'):
            try:
                adresses.append(adress.get_text())
            except:
                pass
        return {'url': url, 'adresses': adresses}
    except:
        return {'url': url, 'adresses': []}


urls = []

file = open('urls.txt', 'r')
for d in file.readlines():
    urls.append(d.strip())

data_list = []

with concurrent.futures.ThreadPoolExecutor(len(urls)) as executor:
    futures = [executor.submit(crawl_data, urls[index]) for index in range(len(urls))]
    for future in concurrent.futures.as_completed(futures):
        data_list.append(future.result(timeout=10))

for data in data_list:
    for adress in data['adresses']:
        print(adress)
