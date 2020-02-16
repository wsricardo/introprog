# Seu Momento Hacker

Aqui trazemos alguns exemplos simples usando os recursos vistos nesta primeira lição.
Neste exemplos usaremos algumas funções disponiveis no python3. E recursos adicionais que podem
ser instalados usando pip ou gerenciador de instalação de sua distribuição linux.

## Recursos Necessários

Algumas bibliotecas que serão utilizadas nesta seção.

	* Requests
	* Python3 LXML
	* BeautifulSoup4

## Instalação

### Windows

Baixe e instale o python 3 do site www.python.org antes de tudo se tiver instalado.
Usando o powershell que está presente no Windows 10 (o qual pode ser baixado do site da microsoft gratuitamente)
instale  *requests*, *lxml* e *BeautifulSoup*.

```
	$ pip install lxml
	$ pip install requests
	$ pip install BeautifulSoup4
```

### Linux

Usando seu gerenciador de instalação de aplicativos de seu sistema linux instale *requests*, *lxml* e *BeautifulSoup*.

No Debian/Ubuntu a instalação pode ser feita da seguinte forma:

Debian
```
	$ su
	# apt update && apt upgrade
	# apt install python3-requests python3-lxml python3-bs4

```

Ubuntu
```
	$ sudo su
	# apt update && apt upgrade
	# apt install python3-lxml python3-requests python3-bs4
```

Também se pode optar fazer a instalação via pip.
Usando *sudo su* no Ubuntu ou *su* no Debian você obtêm o privilégio de administrador do
sistema podendo instalar ou remover aplicativos.


```
	pip install requests
	pip install lxml
	pip install beautifulsoup
```
### Referências para leitura

* PIP & Python Requests (Instalação) - https://pypi.org/project/requests/
* Python Requests - https://requests.readthedocs.io/pt_BR (documentação)
* BeautifulSoup - https://pypi.org/project/beautifulsoup4/
* Python LXML - https://lxml.de/
* Python BeautifulSoup4 - https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/ (documentação)
* Projeto Python LXML (PIP, Instalação) - https://pypi.org/project/lxml/

[Hack](https://wsricardo.github.io/introprog/licao01/extras/exemplos/hack)
