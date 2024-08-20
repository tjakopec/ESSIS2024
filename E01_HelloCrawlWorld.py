# Import the requests library: pip install requests | pip3 install requests (or using PyCharm IDE visual tool)
import requests

# Define the URL of the website to scrape
URL = 'https://www.uni-hildesheim.de/fb3/institute/iwist/veranstaltungen/dess-2022-1/'

# Send a GET request to the specified URL and store the response in 'resp'
resp = requests.get(URL)

# Print the HTTP status code of the response to check if the request was successful
print('Status Code:', resp.status_code)

# Print the HTML content of the response
print('\nResponse Content:')
print(resp.text)
