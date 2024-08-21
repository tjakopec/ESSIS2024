import concurrent.futures
from urllib.parse import urlparse

import requests


def process_domain(domain):
    timeout = 10  # seconds
    exists = True
    try:
        reqs = requests.get('https://' + domain, timeout=timeout)
    except:
        try:
            reqs = requests.get('http://' + domain, timeout=timeout)
        except:
            try:
                reqs = requests.get('https://www.' + domain, timeout=timeout)
            except:
                try:
                    reqs = requests.get('http://www.' + domain, timeout=timeout)
                except:
                    exists = False
    if exists:
        try:
            return {'domain': domain, 'url': reqs.url}
        except:
            return {'domain': domain, 'url': ''}
    else:
        return {'domain': domain, 'url': ''}


file = open('domains.txt', 'r')
domains = []
for d in file.readlines():
    domains.append(d.strip())

furls = []

with concurrent.futures.ThreadPoolExecutor(len(domains)) as executor:
    futures = [executor.submit(process_domain, domains[index]) for index in range(len(domains))]
    count = 0  # bacause index starts at 0
    for future in concurrent.futures.as_completed(futures):
        data = future.result(timeout=10)  # seconds
        if data['url'] != '':
            hrdomain = urlparse(data['url']).netloc
            if hrdomain.endswith('.hr'):
                if hrdomain.endswith(data['domain']):  # www.
                    furls.append(data['url'])
                    # print('OK', count, '->', data['domain'], ' is ', hrdomain)
                else:
                    print('Fail non same domain', count, '->', data['domain'], ' != ', hrdomain)
            else:
                print('Fail non hr domain', count, '->', data['domain'], ' != ', hrdomain)
        else:
            print('Fail connect', count, '->', data['domain'])
        count += 1

# write results to file
f = open('urls.txt', 'a')
for url in furls:
    f.write(url + "\n")
f.close()
