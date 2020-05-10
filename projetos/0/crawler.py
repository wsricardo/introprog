import requests
from bs4 import BeautifulSoup
import re

url = ""

def crawler(hdata, htag=None, attr=None, css_id=None, css_class=None):
    data = None
    soup = BeautifulSoup(hdata, 'html.parser')
    cwn = soup.find_all(htag, css_class)
    

    return (data, cwn)

def initCrawler():
    print('\nCrawler\n')

    if interative == 'yes':
        while True:
            inp_user = input('\n$>>')


            if int_user=='$q':
                exit()
            
            if connect_url:
                pass


if __name__=="__main__":
    print('\nInit crawler')
    print('\nFor exit type "$q".\n\n')
    initCrawler()
