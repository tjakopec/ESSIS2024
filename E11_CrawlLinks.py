
# https://github.com/calc1f4r/Recusive-web-crawler/blob/master/main.py

import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from urllib.parse import urljoin


class WebCrawler:
    def __init__(self, url, max_depth):
        self.url = url
        self.max_depth = max_depth
        self.subdomains = set()
        self.links = set()
        self.jsfiles = set()

    def start_crawling(self):
        self.crawl(self.url, depth=1)

    def crawl(self, url, depth):
        if depth > self.max_depth:
            return

        try:
            response = requests.get(url, timeout=3, allow_redirects=True)
            soup = BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as err:
            print(f"[-] An error occurred: {err}")
            return

        subdomain_query = fr"https?://([a-zA-Z0-9.-]+)"

        for link in soup.find_all('a'):
            link_text = link.get('href')
            if link_text:
                if re.match(subdomain_query, link_text) and link_text not in self.subdomains:
                    self.subdomains.add(link_text)
                else:
                    full_link = urljoin(url, link_text)
                    if full_link != url and full_link not in self.links:
                        self.links.add(full_link)
                        self.crawl(full_link, depth + 1)

        for file in soup.find_all('script'):
            script_src = file.get('src')
            if script_src:
                self.jsfiles.add(script_src)

    def print_banner(self):
        print("-" * 80)
        print(f"Recursive Web Crawler starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("-" * 80)
        print(f"[*] URL".ljust(20, " "), ":", self.url)
        print(f"[*] Max Depth".ljust(20, " "), ":", self.max_depth)
        print("-" * 80)

    def print_results(self):
        if self.subdomains:
            for subdomain in self.subdomains:
                print(f"[+] Subdomains : {subdomain}")
        print()

        if self.links:
            for link in self.links:
                print(f"[+] Links : {link}")

        print()

        if self.jsfiles:
            for file in self.jsfiles:
                print(f"[+] JS Files : {file}")


web_crawler = WebCrawler('https://www.ffos.unios.hr', 1)
web_crawler.print_banner()
web_crawler.start_crawling()
web_crawler.print_results()

# student tasks:
# run this crawler to URL of your choice
# exclude all not https URL
# exclude all the not initial domain links


