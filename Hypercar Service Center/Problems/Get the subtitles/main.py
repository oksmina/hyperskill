import requests

from bs4 import BeautifulSoup

number = int(input())
r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')
count = 0
for s in soup.find_all('h2'):
    if count == number:
        print(s.text)
        break
    count = count + 1