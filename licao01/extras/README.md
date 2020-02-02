
# EXTRAS

1. Função Lambda Python
2. Trabalhando com String

## Função Lambda

Em Python há um recurso interesante para criar funções através da palavra reservada pela linguagem "lambda".

```
dobro = lambda n: 2*n
```

O que faz a função acima é retornar o dobro de um número. A função *dobro* poderia ser usada da seguinte forma:

```
dobro(2)
```

Saída:

```
	4
```

Definição geral:

```
	nome_funcao = lambda <parametros> : <expressão>
```

Mais detalhes: [https://docs.python.org/3/reference/expressions.html#lambda](https://docs.python.org/3/reference/expressions.html#lambda)

## Trabalhando com strings

Algumas operações e funções estão definidas para se trabalhar com strings. Por exemplo com o operador + é possível concatenar duas strings ou mais.

Exemplos

```
	>>> n1 = "Pedro"
	>>> n2 = "Henrique"
	>>> n1 + n2
	'PedroHenrique'
	>>> m = n1 + ' ' + n2
	>>> print(m)
	Pedro Henrique
	>>> m.split() 
	['Pedro', 'Henrique']

	>>> m[2:6] # Selecionando um pedaço da string
	'dro'
	>>> m[2:]
	'dro Henrique'
```

Material extra sobre a linguagem Python [https://panda.ime.usp.br/panda/python](https://panda.ime.usp.br/panda/python)
e em [www.python.org](https://www.python.org).

