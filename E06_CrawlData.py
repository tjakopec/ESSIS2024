import concurrent.futures
from bs4 import BeautifulSoup
import requests

# Find all emails


def crawl_data(url):
    emails = []
    try:
        page = requests.get(url, timeout=10)
        soup = BeautifulSoup(page.text, 'lxml')  # pip install lxml     | 'html.parser' is the build in one
        for link in soup.findAll('a'):
            try:
                href = link.get('href').strip()
                if href.startswith('mailto'):
                    emails.append(href.replace('mailto:', ''))
            except:
                pass
        return {'url': url, 'emails': emails}
    except:
        return {'url': url, 'emails': []}


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
    for email in data['emails']:
        print(email)
