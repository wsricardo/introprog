# Hacking Com Linux

Aqui estaremos usando sistema linux e aplicações presentes em sistemas linux.

## Recursos usados

* Python
	- Modulos: requests, urllib, lxml, BeautifulSoup
* grep (ferramenta de linha de comando linux)

## Usando grep

```
	$ echo "Texto texto. Bem vindo a Pernambuco." > /tmp/data
	$ cat /tmp/data | grep texto
	$ cat /tmp/data | less
```

## Leituras Sobre Linux

* [Na Wikipédia](https://pt.wikipedia.org/wiki/Linux)
* [Guia Foca Linux (material antigo)](https://guiafoca.org/)
* [Canal Diolinux](https://www.diolinux.com.br/)
* [Google](https://www.google.com/)
* [Slideshare](https://pt.slideshare.net/fernando.palma/apostila-linux-bsico)

## Combinando Python e grep

Script python

```python
	>>> from bs4 import BeautifulSoup
	>>> import requests
	>>> dat = requests.get('https://pt.wikipedia.org/w/index.php?search=Arte&title=Especial%3APesquisar&wprov=acrw1_0')
	>>> f = open('/tmp/data', 'w')
	>>> f.write(dat.text)
	>>> f.close()
```

no terminal com comando *grep*, *cat* e *less*.


Obter conteúdo do arquivo criado pelo script python acima.
```
	$ cat /tmp/data
```

selecionando partes especificas do texto com grep que contem uma palavra ou que *casam* com a [expressão regular]() passada para o grep,

```
	$ cat /tmp/data | grep "Arte"
```

visualizando mais detalhadamente usando less (rolagem pelo conteudo)

```
	$ cat /tmp/data | grep "Arte" | less
```

pedaço da saída para comando acima

```
<title>Arte – Wikipédia, a enciclopédia livre</title>
<script>document.documentElement.className="client-js";RLCONF={"wgBreakFrames":!1,"wgSeparatorTransformTable":[",\t."," \t,"],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"],"wgMonthNamesShort":["","jan.","fev.","mar.","abr.","mai.","jun.","jul.","ago.","set.","out.","nov.","dez."],"wgRequestId":"XjgxzwpAICoAABUWjlAAAACU","wgCSPNonce":!1,"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":!1,"wgNamespaceNumber":0,"wgPageName":"Arte","wgTitle":"Arte","wgCurRevisionId":56962048,"wgRevisionId":56962048,"wgArticleId":310,"wgIsArticle":!0,"wgIsRedirect":!1,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["!Artigos com ligações precisando de desambiguação","!Artigos que carecem de notas de rodapé desde abril de 2017","!Artigos de arte que carecem de notas de rodapé","!Artigos com ligações inativas",
"!Artigos destacados na Wikipédia em espanhol","!Artigos destacados na Wikipédia em catalão","!Artigos destacados na Wikipédia em macedônio","!Artigos destacados na Wikipédia em africâner","!Artigos bons na Wikipédia em galego","Arte"],"wgPageContentLanguage":"pt","wgPageContentModel":"wikitext","wgRelevantPageName":"Arte","wgRelevantArticleId":310,"wgIsProbablyEditable":!1,"wgRelevantPageIsProbablyEditable":!1,"wgRestrictionEdit":["autoconfirmed"],"wgRestrictionMove":["autoconfirmed"],"wgMediaViewerOnClick":!0,"wgMediaViewerEnabledByDefault":!0,"wgPopupsReferencePreviews":!1,"wgPopupsConflictsWithNavPopupGadget":!1,"wgVisualEditor":{"pageLanguageCode":"pt","pageLanguageDir":"ltr","pageVariantFallbacks":"pt"},"wgMFDisplayWikibaseDescriptions":{"search":!0,"nearby":!0,"watchlist":!0,"tagline":!0},"wgWMESchemaEditAttemptStepOversample":!1,"wgULSCurrentAutonym":"português","wgNoticeProject":"wikipedia","wgWikibaseItemId":"Q735",
<link rel="alternate" href="android-app://org.wikipedia/http/pt.m.wikipedia.org/wiki/Arte"/>
<link rel="canonical" href="https://pt.wikipedia.org/wiki/Arte"/>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-Arte rootpage-Arte skin-vector action-view">
        <h1 id="firstHeading" class="firstHeading" lang="pt">Arte</h1>
                <div id="mw-content-text" lang="pt" dir="ltr" class="mw-content-ltr"><div class="mw-parser-output"><div class="hatnote"><img alt="Disambig grey.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Disambig_grey.svg/20px-Disambig_grey.svg.png" decoding="async" width="20" height="15" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Disambig_grey.svg/30px-Disambig_grey.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Disambig_grey.svg/40px-Disambig_grey.svg.png 2x" data-file-width="260" data-file-height="200" />&#160;<b>Nota:</b> Para outros significados, veja <a href="/wiki/Arte_(desambigua%C3%A7%C3%A3o)" class="mw-disambig" title="Arte (desambiguação)">Arte (desambiguação)</a>.</div>
<p><b>Arte</b> (do termo <a href="/wiki/Latim" title="Latim">latino</a> <i>ars</i>, significando <i><a href="/wiki/T%C3%A9cnica" title="Técnica">técnica</a></i> e/ou <i>habilidade</i>) pode ser entendida como a atividade humana ligada às manifestações de ordem <a href="/wiki/Est%C3%A9tica" title="Estética">estética</a> ou <a href="/wiki/Comunica%C3%A7%C3%A3o" title="Comunicação">comunicativa</a>, realizada por meio de uma grande <a href="/wiki/Manifesto_das_Sete_Artes" title="Manifesto das Sete Artes">variedade de linguagens</a>,<

:
```

Os dois-pontos indica que o texto continua.
