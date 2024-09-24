import requests
from bs4 import BeautifulSoup

def coletar_manchetes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    manchetes = [h2.text for h2 in soup.find_all('h2')]
    return manchetes

manchetes = coletar_manchetes('https://g1.globo.com/')
for manchete in manchetes:
    print(manchete)