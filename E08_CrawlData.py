import concurrent.futures
from bs4 import BeautifulSoup
import requests
from lxml import etree

# urls that tahe three levels of menu


def crawl_data(url):
    adresses = []
    try:
        page = requests.get(url, timeout=10)
        soup = BeautifulSoup(page.text, 'lxml')  # pip install lxml     | 'html.parser' is the build in one
        dom = etree.HTML(str(soup))
        try:
            if len(dom.xpath('//ul/li/ul/li/ul/li')) > 0:
                return {'url': url, 'three_levels': True}
            else:
                return {'url': url, 'three_levels': False}
        except:
            return {'url': url, 'three_levels': False}
    except:
        return {'url': url, 'three_levels': False}


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
    if data['three_levels']:
        print(data['url'])
