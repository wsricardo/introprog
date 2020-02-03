# Código para extrair lista de links em umsite usando requests, urrlibrequest e BeautifulSoup4
import requests
from bs4 import BeautifulSoup
import urllib.request

urls = {'wiki_pt': 'https://pt.wikipedia.org', 
        'wiki_pt_main': 'https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal',
        'wiki_main': 'https://www.wikipedia.org'
        }

dat = requests.get(urls['wiki_main'])
soup = BeautifulSoup(dat.text, 'html.parser')

links = soup.findAll('a')

lista_url = map(lambda i: i['href'], links[0: len(links)])
lista = []
for j in lista_url:
    lista.append(j.replace("//", "https://"))
    print("Site: ",(j))

print(lista[0])

#print('\n')
#print('Conteudo da página')
#print(soup.get_text())
