# Importing the requests library to fetch web content
import requests

# The URL of the webpage we want to fetch
url = "https://www.digitalasprasmes.lv/example.html"

# Using requests.get() to fetch the content of the URL
saturs = requests.get(url)

# Opening a file named 'result.txt' in write mode
f = open("result.txt", "w")

# Writing the content (text) of the fetched webpage to the file
f.write(saturs.text)

# Closing the file to ensure data is saved and to free up system resources
f.close()
