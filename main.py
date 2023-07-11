import requests
from bs4 import BeautifulSoup
import json

json_file = 'D:\yugioh-db\card_list.json'
html_file = 'D:\yugioh-db\html_dump.html'

# Send a GET request to the webpage
url = 'https://yugiohprices.com/card_price?name=1st%20Movement%20Solo'
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find and extract the desired data
# Here's an example of extracting all the links on the page
links = soup.find_all('a')

# Create a list to store the extracted data
data = []

# Iterate over the links and extract relevant information
for link in links:
    link_data = {
        'text': link.text,
        'url': link.get('href')
    }
    data.append(link_data)

# Convert the data to JSON
json_data = json.dumps(data, indent=4)

# Save the JSON data to a file
with open(json_file, 'w') as file:
    file.write(json_data)

'''
url = 'https://yugiohprices.com/card_price?name=1st%20Movement%20Solo'
response = requests.get(url)

# Get the HTML content
html_content = response.text

# Write the HTML content to a file
with open(html_file, 'w', encoding='utf-8') as file:
    file.write(html_content)
'''    