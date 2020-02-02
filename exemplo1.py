# Código para extrair lista de links em umsite usando requests, urrlibrequest e BeautifulSoup4
import requests
from bs4 import BeautifulSoup
import urllib.request

dat = requests.get('https://www.wikipedia.org')
soup = BeautifulSoup(dat.text, 'html.parser')

links = soup.findAll('a')

lista_url = map(lambda i: i['href'], links[0: len(links)])
lista = []
for j in lista_url:
    lista.append(j.replace("//", "https://"))
    print("Site: ",(j))

print(lista[0])

