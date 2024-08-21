import requests


def process_domain(domain):
    exists = True
    try:
        reqs = requests.get('https://' + domain)
    except:
        try:
            reqs = requests.get('http://' + domain)
        except:
            try:
                reqs = requests.get('https://www.' + domain)
            except:
                try:
                    reqs = requests.get('http://www.' + domain)
                except:
                    exists = False
    if exists:
        try:
            url = reqs.url
        except:
            url = 'null'
    else:
        url = 'null'

    print('Done', domain, '->', url)


file = open('domains.txt', 'r')
domains = file.readlines()
for d in domains:
    process_domain(d.strip())
