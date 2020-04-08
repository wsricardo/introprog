import requests
from bs4 import BeautifulSoup

dat = requests.get('https://www.bibliaonline.com.br/')
soup = BeautifulSoup(dat.text, 'html.parser')

vs = soup.findAll('article')

# (0) Referência classe no codigo html onde está o trecho desejado.
vs1 = vs[0].find_all(class_='jss162 jss157')
vs2 = vs[0].find_all(class_='jss162 jss157')
#print(vs2[0].findAll('a')[0].get_text())

# Na tag 'article' captura a class 'jss162 jss157'
# que onde ficam os versículos do dia no
# código html da página BibliaOnline. 
# A localização do versículo fica dentro tag 'a'
# na class especificada acima em (0)
texto = (vs1[0].findAll('p')[0].get_text() + '\n' +
        vs1[0].findAll('a')[0].get_text() + '\n\n' +
        vs2[1].findAll('p')[0].get_text() + '\n' + 
        vs2[1].findAll('a')[0].get_text() + '\n')

print('\n\t\t\tVersículos Diários')
print('\n{}'.format(texto))
