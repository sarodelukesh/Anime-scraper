import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # To handle relative URLs

# Ask for the URL of the page to scrape
url = input("Enter the URL of the search result page: ")

# Send the GET request to fetch the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Parse the content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the link starting with 'some.ex/down'
found_link = None
for link in soup.find_all('a', href=True):  # Look at all anchor tags with href
    href = link['href']
    if href.startswith('https://s3embtaku.pro/download'):
        found_link = href
        break

# If the link is found, print the full URL (handling relative URLs)
if found_link:
    full_url = urljoin(url, found_link)  # Handle relative URLs
    print("Found the link:", full_url)
else:
    print("Link starting with 'some.ex/down' not found.")
