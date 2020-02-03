# Código para extrair lista de links em umsite usando requests, urrlibrequest e BeautifulSoup4
# Wandeson Ricardo, 2020
# www.wsricardo.blogspot.com

import requests
from bs4 import BeautifulSoup
import urllib.request
# A palavra reservada 'import' serve para importar outro código,
# para ser usado. Tanto 'from' como 'import ajudam
# a importar módulos contendo definições, funções, variáveis 
# e constantes que podem ser incluidas e usadas pelo código.
# Isso permite criar pacotes contendo códigos
# podem ser compartilhados por outras aplicações
# adicionando novos recursos.
#
# Para obter ajuda sobre uma função, objeto ou classe use
# as funções 'dir' e 'help'.
# Exemplos:
# (Exemplo abaixo)
# Ajuda sobre o objeto string. Uma retorna lista de métodos a associadas
# ao objeto string e a outra, o help, retorna detalhes sobre o objeto e suas
# definições e métodos (funções associadas ao objeto 'string').
# >>> dir(str)
#

urls = {'wiki_pt': 'https://pt.wikipedia.org', 
        'wiki_pt_main': 'https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal',
        'wiki_main': 'https://www.wikipedia.org'
        }

dat = requests.get(urls['wiki_pt_main'])
soup = BeautifulSoup(dat.text, 'html.parser')

# A tag 'a' marca onde esta links em um documento HTML
# Formato geral: <a href="www.seu-link-.com.br">Seu Link<a>
# o atributo 'href' especifica o endereço do site.
links = soup.findAll('a')
#print('links: ',links)
lista_url = map(lambda i: i.get('href'), links[0:len(links)])
print('lista_url',lista_url)

# Lista de links extraidos usando a função 'map' acima.
for i in lista_url:
    print('links>>>', i)


#
#lista_url = map(lambda i: i['href'], links )
#lista = []
# Percorrendo o objeto gerado pela função "map"
# e os anexando a 'lista' com a função 'append'.
# Observe que a função 'replace' troca uma string
# por outra.
#for j in lista_url:
#    print(j)
#    lista.append(j.replace("//", "https://"))
#    print("Site: ",(j))
#from time import *
#sleep(2)
#print(lista)
#print('\n')
#

# Exibbindo o conteúdo da ágina
# (como vistoem um navegador)
#print('Conteudo da página')
#print(soup.get_text())
#
