from bs4 import BeautifulSoup
import requests

url = "https://svelte.dev/tutorial/basics"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
#print(soup.prettify())

data = {}

optgroups = soup.find_all('optgroup')

for optgroup in optgroups:
    label = optgroup['label']
    options = optgroup.find_all('option')
    option_texts = [option.text.strip() for option in options]
    data[label] = option_texts

#print(data)

# Loop through the data and print out the topics and subtopics
for key in data:
    print(f"{key}:")
    for item in data[key]:
        print(f"- {item}")
    print()