# Tasks

## Tarefas Faltantes

### Correções

* Corrigir o programa crawlernews.py
	- Adequar variavel para armazenar a noticia e seu link.
	- implementar variavel e função para salvar noticias em json e csv.
	- 


#### Montando a estrutura pra armazenar informações das noticias


tags -> class

article (destaque) -> class=(MQsxIb  xTewfe  R7GTQ  keNKEd  j7vNaf  Cc0Z5d EjqUne)

article (comum) -> class=(  MQsxIb xTewfe tXImLc R7GTQ keNKEd keNKEd  dIehj EjqUne ) 

a (links das noticias)  -> class=(VDXfz  DY5T1d)

h3 (título da noticia em destaque) -> ( ipQwMb  ekueJc  gEATFF  RD0gLb )

div (rodapé da noticiade e fonte) -> class=( QmrVtf  RD0gLb ) (1) * 
	[1] (Contém o nome de onde é a notícia) -> a -> class=( wEwyrc  AVN2gc  uQIVzc  Sksgp ) 

( ( div -> SbNwzf ) -> article ) -> class=( MQsxIb  xTewfe  tXImLc  R7GTQ  keNKEd  keNKEd   dIehj , EjqUne ) 

h4 -> class=( ipQwMb  ekueJc  gEATFF  RD0gLb )


Estrutura Campos

{ Titulo, link, nome da fonte da noticia }

definindo ela como dicionário

```
	dnews = { 'titulo': texto,
		'link': link_name,
		'nome_origem': origem }

```

Refinindo a estrutura

```
dnews = [ {'titulo': texto, 'link': link_name, 'nome_origem': origem },
	  {.},
	...,
	{.},

	]
```


### Atualidação

	Atualizar tutorial introprog seção 2 e 3
