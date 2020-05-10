# Crawler News 1
import requests
from  bs4 import BeautifulSoup
import re

url_pt_br = 'https://news.google.com/topstories?tab=wn&hl=pt-BR&gl=BR&ceid=BR:pt-419'

url = 'https://news.google.com'

attr = { 'tags': 'article',
        'class': 'MQsxIb'
        }
# Fazendo requisição dos dados da página e salvando página no arquivo data.
# Request web page of Google News and save in file.
#dat = requests.get(url)
#with open('data','w') as fl:
#    fl.write(dat.text)
#    fl.close()   
# Baixar página usando python em /tmp/data
fl = open('/tmp/data', 'r')
content = fl.read()
fl.close()

#print(content)
soup = BeautifulSoup(content, 'html.parser')

cwn = soup.find_all('article')
news = { 'title': '', 'url':'','source_news':'' }
dnews = []

# A primeira noticia (article) usa 'h3'
# as noticias seguintes usam 'h4'
for i in cwn:
    dnews.append({'title': i.find_all(
                        re.compile('^h[1-6]'))[0].string,
                'url': i.a['href'],

                'source_news': i.find_all('a', class_='wEwyrc')[0].string})
    pass

size_dnews = len(dnews)
for i in range(size_dnews):
    print('\n {0} \n {1} \n {2} \n'.format(
        dnews[i]['title'],
        url+dnews[i]['url'][1:],
        dnews[i]['source_news'] )
        )

def gen_template(content_news, template_full=False):

    if template_full:
        page_news = '<ul >'
        for i in range(size_dnews):
            page_news += """
            <li> <h4 style="margin: 0; padding: 0;"> {0} </h4>
            <a style="margin: 0; padding: 0; text-align: center;" href="{1}">{2}</a> </li><br><br><br>
            """.format(
                    dnews[i]['title'],
                    url+dnews[i]['url'][1:],
                    dnews[i]['source_news']
                    )
        # Fim 'for'
        page_news += '</ul>'

        with open('output1.html', 'w') as fl:
            fl.write("""
                    <!DOCTYPE html>
                    <html>
                    <head><title>Notícias</title>
                    </head>
                    <body>
                    <h3>Portal Notícias</h3>
                     {0}
                    </body>
                    </html>

                    """.format( page_news ) )
            return 1

    return """
            <br>
            <h3> {0} </h3>
            <br>
            <a> {1} </a> </a>
            <br>
            {2}
            """.format(content_news['title'],
                    content_news['source_news'],
                    content_news['url'])

def gen_json(content_news, out='output'):
    import json
    data = json.dumps(
            content_news,
            ensure_ascii=False,
            sort_keys=False,
            indent=4
            )

    with open(out+'.json', 'w') as fl:
        fl.write(data)
        

#print(gen_template(dnews[0]))
#gen_json(dnews)
gen_template(dnews, True)

#print(dnews[0]['source_news'])
#print('$> ',dnews[0])
#print('\n>' + 
#        repr(cwn[1].find_all(re.compile('^h'))[0].string) 
#        )
#print(cwn[0].h3.string)
#print(cwn[0].a['href'])
#print('Origem Noticia$> '+cwn[0].find_all('a', class_='wEwyrc')[0].string)
