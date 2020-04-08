# Crawler de noticias.
# Pegando noticias e informações.
import requests
import re
from bs4 import BeautifulSoup

"""
Observando o código html da página
https://news.google.com temos.
Noticias estão nas tags 'article',
em cada tag article há o titulo (h3,h4);
o link na tag 'a' com atributo class de
alor 'VDXfz'. As tag h3 ou h4 dentro de
article tem atributo class com valor ipQwMb;
já a tag 'div' com atributo class com valor
QmrVtf contem informação do nome do site
de onde é a noticia e há quanto tempo
foi publicada.
"""

# -Variaveis globais-
_url = ''
_attr = ''
_content = ''
_fl = ''
# ----

# Estrutura Dados Noticias (Inicio)
# Estrutura para armazenar
# título, link, e origem da notícia.
# (title, link_name, nsource_name)
#dnews = [
#        { 'title':          '',
#            'link_name':    '',
#            'nsource_name': ''
#            }
#
news = { 'title': '',
        'link_name': '',
        'nsource_name': ''
        }
# Fazer dnews.append(news) para adicionar
# cada notícia.
dnews = [] 
# (Fim)


# Inicializando variaveis globais.
def set_(url, attr='', file_name=''):
    """
        url -> sites
        attr -> atributos, e parametros de pesquisa
        fl -> arquivo para salvar dados das notícias
    """
    global _url
    global _attr
    global _fl

    _url = url
    _attr = attr
    _fl = file_name

# Extraindo dados das noticias
def nextract(web_content):


    return dnews


# Iniciando busca no código html da
# página do site Google News e processando.
def crawler():
    print('url: {}'.format(_url))
    if _url == '':
        print('\nEspecificar url (site)')
        return 0
    # Dados
    dat = requests.get(_url)
    soup = BeautifulSoup(dat.text, 'html.parser')
    
    # CraWNews -> cwn
    # da página do google news.
    cwn = soup.find_all('article', class_='MQsxIb')
    # Conteúdos
    _content = cwn[0]
    # Debug
    #print('\n>> {}'.format(_content.get_text()))


    return cwn

def main():
    _content = crawler()
    #print('\n>>{}'.format(_content.get_text()))
    for i in _content:
        print('\n> {}'.format(i.get_text()))

if __name__=="__main__":
    set_('https://news.google.com/topstories?tab=wn&hl=pt-BR&gl=BR&ceid=BR:pt-419')
    main()
