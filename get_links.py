import requests as rq
from bs4 import BeautifulSoup

# Enter url (User)
url = input("Enter Link: ")

# Checks url
if ("https" or "http") in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)

soup = BeautifulSoup(data.text, "html.parser")
links = []

# finds all <a> tags
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Writes the output to a file (all_links.txt) 
with open("all_links.txt", 'a') as saved:
    print(links[:10], file=saved)