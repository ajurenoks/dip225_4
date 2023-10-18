# Importing the requests library to fetch web content
import requests
# Importing the BeautifulSoup module from bs4 for web scraping
import bs4

# Setting the URL of the Wikipedia page for Riga Technical University as the target for scraping
url = "https://en.wikipedia.org/wiki/Riga_Technical_University"

# Using requests.get() to send a GET request to the specified URL and fetch its content
saturs = requests.get(url)

# Checking if the request was successful (HTTP status code 200 means OK/successful)
if saturs.status_code == 200:
    # Parsing the fetched content of the webpage with BeautifulSoup using the 'html.parser' method
    lapas_saturs = bs4.BeautifulSoup(saturs.content, 'html.parser')
    
    # Searching the parsed content for all elements with the class "mw-headline", 
    # which usually represents the headlines/sub-headlines in Wikipedia articles
    atradu = lapas_saturs.find_all(class_="mw-headline")
    
    # Iterating through each found headline/sub-headline
    for a in atradu:
        # Printing the text (string) content of each headline/sub-headline
        print(a.string)
