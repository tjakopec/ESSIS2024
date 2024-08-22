import concurrent.futures
from bs4 import BeautifulSoup
import requests

# Order all URLs by total links on crawled page

def crawl_data(url):
    try:
        page = requests.get(url, timeout=10)
        soup = BeautifulSoup(page.text, 'lxml')  # pip install lxml     | 'html.parser' is the build in one
        total_links = 0
        for link in soup.findAll('a'):
            try:
                href = link.get('href').strip()
                if href.startswith('http'):
                    total_links += 1
            except:
                pass
        return {'url': url, 'total_links': total_links}
    except:
        return {'url': url, 'total_links': 0}


urls = []

file = open('urls.txt', 'r')
for d in file.readlines():
    urls.append(d.strip())

data_list = []

with concurrent.futures.ThreadPoolExecutor(len(urls)) as executor:
    futures = [executor.submit(crawl_data, urls[index]) for index in range(len(urls))]
    for future in concurrent.futures.as_completed(futures):
        data_list.append(future.result(timeout=10))

sorted_list = sorted(data_list, key=lambda i: i['total_links'], reverse=True)

for data in sorted_list:
    print(data['total_links'], '\t', data['url'])
