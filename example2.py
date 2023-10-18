# Importing the requests library to fetch web content
import requests
# Importing the BeautifulSoup module from bs4 for web scraping
import bs4

# The URL of the webpage we want to fetch
url = "https://www.digitalasprasmes.lv/example.html"

# Using requests.get() to fetch the content of the URL
saturs = requests.get(url)

# Checking the status code of the request
if saturs.status_code == 200:
    # HTTP status code 200 means OK/successful
    # Parsing the content of the webpage with BeautifulSoup
    lapa = bs4.BeautifulSoup(saturs.content, 'html.parser')
    
    # Finding all h3 tags on the webpage
    atrada = lapa.find_all("h3")
    
    # Printing the text (string) content of the first h3 tag found
    print(atrada[0].string)
elif saturs.status_code == 404:
    # HTTP status code 404 means Not Found - the server could not find the requested URL
    print("Error 404: The webpage was not found.")
elif saturs.status_code == 403:
    # HTTP status code 403 means Forbidden - the server understands the request but refuses to fulfill it
    print("Error 403: Access to the webpage is forbidden.")
elif saturs.status_code == 500:
    # HTTP status code 500 means Internal Server Error - the server encountered an unexpected condition
    print("Error 500: The server encountered an internal error.")
else:
    # If the status code is something other than the ones we've explicitly checked for
    print(f"Received an unexpected HTTP status code: {saturs.status_code}")
