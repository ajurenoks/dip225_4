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
    
    # Searching the parsed content for all list items (<li> elements) with the class "interlanguage-link",
    # which usually represents the links to the same Wikipedia page in other languages
    atradu = lapas_saturs.find_all("li", class_="interlanguage-link")
    
    res = []
    # Iterating through each found interlanguage link
    for a in atradu:
        # Finding the child anchor tag (<a>) of each list item which contains the link and language info
        row = a.findChild("a")
        # Appending the found anchor tag to the 'res' list
        res.append(row)
    
    dati = []
    # Iterating through each anchor tag stored in 'res'
    for ieraksts in res:
        row = []
        # Extracting the 'title' attribute from the anchor tag, which is usually the language name in English 
        # (e.g., "German: Riga Technical University")
        valoda = ieraksts.attrs['title']
        
        # Extracting the 'lang' attribute from the anchor tag, which represents the language code (e.g., "de" for German)
        lang = ieraksts.attrs['lang']
        
        # Appending the language name and language code to the 'row' list
        row.append(valoda)
        row.append(lang)
        
        # Appending the 'row' list to the 'dati' list, resulting in a nested list structure
        dati.append(row)

# Printing the 'dati' list, which contains pairs of language names and their respective codes
print(dati)
