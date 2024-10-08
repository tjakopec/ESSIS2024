# pip install chromedriver-py
# pip install chromedriver-py==127.0.6533.199
# pip install selenium

# Find the notification about the exam

from selenium import webdriver
from chromedriver_py import binary_path  # this will get you the path variable
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

svc = webdriver.ChromeService(executable_path=binary_path)


options = Options()
# do not show chrome - faster
options.add_argument('--headless=new')
options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(service=svc, options=options)

# deprecated but works in older selenium versions
# driver = webdriver.Chrome(executable_path=binary_path)
driver.get('https://www.ffos.unios.hr/odsjek-za-informacijske-znanosti/')

# elements = driver.find_elements(By.XPATH, '//*[@id="sokrat-news"]/div[2]/div[1]/div/div[1]/div/div')
elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'owl-item')]")
for element in elements:
    # print(element.get_attribute('outerHTML'))
    text = element.get_attribute('textContent')
    # print(element.get_attribute('textContent'))
    if 'jakopec' in text.lower():
        print(text)
        print('*********')

# student task: find the notification about the exam on website of your faculty

# student task Osijek: find the notification about the exam on website of https://sit.unizd.hr/

