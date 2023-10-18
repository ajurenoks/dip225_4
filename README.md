# Web Scraping Project

This repository contains a series of Python scripts that showcase various aspects of web scraping using the `requests` and `BeautifulSoup` libraries.

## Contents

1. `example1.py` - A script that fetches the content of a specific webpage and stores it in a file.
2. `example2.py` - Scrapes headlines from the Wikipedia page for Riga Technical University.
3. `example3.py` - Extracts links to the Riga Technical University Wikipedia page in other languages.
4. `example4.py` - A script that handles various HTTP status codes and provides respective messages.

## Libraries Used

### `requests`

- **Description**: The `requests` library is a popular Python library for making HTTP requests. It abstracts the complexities of making requests behind a simple API, with the ability to send HTTP/1.1 requests.
- **Usage in this Project**: In our scripts, the `requests` library is primarily used to fetch the content of webpages.

### `BeautifulSoup` (`bs4`)

- **Description**: `BeautifulSoup` is a Python library for web scraping purposes to pull the data out of HTML and XML files. It provides idiomatic ways of navigating, searching, and modifying the parse tree.
- **Usage in this Project**: We use `BeautifulSoup` to parse the content fetched from webpages and extract specific information like headlines and interlanguage links.

## Setup & Usage

### Prerequisites

- Python 3.x
- `requests` and `bs4` (BeautifulSoup) libraries

### Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/web-scraping-project.git
```

2. Navigate to the directory:

```
cd web-scraping-project
```

3. Install the required libraries:

```
pip install requests bs4
```

### Running the Scripts

To run a script, simply execute it with Python. For example:

```
python wiki_headlines.py
```

## Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
