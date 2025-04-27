from bs4 import BeautifulSoup
import requests

url = "https://docs.cycling74.com/apiref/js/"
response = requests.get(url)

# Check if request was successful
if (response.status_code == 200):
    html_content = response.text
else:
    print(f"Error: {response.status_code}")

soup = BeautifulSoup(html_content, "html.parser")

categories = soup.find_all('h2')

for category in categories:
    table = category.find_next()
    links = table.find_all('a')
    category_name = category.text

    for link in links:
        title = link.get('title')
        link = link.get('href')

        if (title):
            print(category_name, title, link)
