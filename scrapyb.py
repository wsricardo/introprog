import requests
from bs4 import BeautifulSoup

dat = requests.get('https://www.bibliaonline.com.br/')
soup = BeautifulSoup(dat.text, 'html.parser')

vs = soup.findAll('article')

vs2 = vs[0].find_all(class_='jss162')

print(vs2)



print(vs2[0].get_text())
