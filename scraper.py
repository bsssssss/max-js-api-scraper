from bs4 import BeautifulSoup
import requests

url = "https://docs.cycling74.com/apiref/js/"
response = requests.get(url)

# Check if request was successful
if (response.status_code == 200):
    html_content = response.text
    # print(html_content)
else:
    print(f"Error: {response.status_code}")

soup = BeautifulSoup(html_content, "html.parser")

categories = soup.find_all('h2')

for category in categories:
    print(category)
