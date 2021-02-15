import requests

from bs4 import BeautifulSoup

number = int(input())
r = requests.get(input())

soup = BeautifulSoup(r.content, 'html.parser')
a = soup.find_all('a')
count = 1
for i in a:
    if count == number:
        print(i.get('href'))
        break
    count = count + 1