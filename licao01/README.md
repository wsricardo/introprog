
Algoritmo
===========

Como visto anteriormente "algoritmo" de forma básica é uma sequência de instruções que servem a resolução de um dado problema ou tarefa. De modo geral um algoritmo o conceito de algoritmo está por trás da construção de programas de computadores os quais podem ser escritos em dada linguagem na qual será descrita os passos para a resolução de um problema.
Pense por exemplo como a receita de um bolo como também um algoritmo.

Trabalhando e Representando Dados
==================================

Os programas de computador trabalham em cima de informações, dados, representados em um formato interno da máquina com zeros e uns. Para armazenar esses dados é preciso pensar objetos que retenham essas informações. A nível de hardware esses dados são armazenados em áreas especificas do computador, contudo em termos de programas e linguagens de programação pensamos nesses objetos como sendo variáveis ou estrutura de dados compostas que armazenam esses dados para manipula-los e processa-los. Esses dados pocessados podem gerar outros dados que daí serão armazenados em outra área da máquina podendo esses dados serem exibidos ao usuário pelo monitor ou enviados para uma impressora por exemplo.

Variáveis
===========

Em algumas liguagens de modo geral antes de se utilizar uma variável é preciso a definir bem e seu tipo tendo em mente as operações a serem executadas sobre essa variável.

Neste pequeno curso de programação de computador consideraremos como base a linguagem Python mas traremos alguns exemplos seguidos de breves explicações sobre a versão do código em C.

Na linguagem Python, a qual é uma linguagem interpretada, a definição do tipo da variável é dinâmica ou seja o seu tipo é definido na atribuição e pode ser alterado ao longo do programa.

Exemplo:

Python

```
a = 2.0 # Tipo "real"
k = 0 # inteiro
nome = "Pedro Henrique" # tipo "string", cadeia de caracteres
```

Poderiamos realizar algumas operações com estas variáveis.

```
dobro = 2*a
k = k + 1
nome = nome.upper() # chamamos a função "upper" que processa o conteudo de nome

```

Digite,

```
print(dobro)
print(k)
print(nome)
```
Temos a seguinte saída para o fragmento acima,

```
	4.0
	1
	PEDRO HENRIQUE
```

A palavra "print" é uma função (veremos mais detalhes em seção sobre funções) que serve a exibir mensagens na tela, neste exemplo os conteúdos das variáveis.

Observe que de modo geral as linguagens permitem que novos tipos sejam criados e operações sobre esses tipos definidas.

A váriavel nome é do tipo string, pode ser vista como um vetor de caracteres que pode ter elementos acessados da seguinte formas:

```
nome[n]
```

onde n indica a posição no vetor do elemento, com n iniciando em 0.
Ou seja, o elemento em *nome[0]* é o primeiro elemento do vetor. Neste caso o elemento para n=0 é o caractere "P".

Mais a frente vamos em examinar algumas funções que operam sobre variaveis do tipo string.

Outros tipos de dados são listas, tuplas e dicionários.

Exemplos:

**Listas**

```
	>>> lista = [2, 1, 3,] # lista de inteiros
	>>> print(lista)
	>>> l = [0, "Pedro", "c", True] # Não obrigado os elementos da lista serem do mesmo tipo.
	>>> l2 = [1, [2 ,3 ,4], [2, 3]] # Pode haver listas e sublistas.

```
**Tuplas**

```
	>>> t = (3, 4, 5) # Semelhante a listas (*)
	>>> t = ("oi", 34)
	>>> print(t[0]) # exibindo o primeiro elemento da tupla.
```

(*) Obs.: Tuplas são tipos imutaveis ou seja apos definida uma variavel do tipo tupla seu valor não poderá ser alterado.

**Dicionários**

```
	>>> dc = {"chave1":"value1", "chave2": "value2"}
	>>> print(dc["chave2"])
	value2
```

Como no exemplo acima a estrutura de um dicionário é criada definindo uma *chave* e um *valor* associado a essa chave.
As chaves podem ser valores inteiros, string.

Obs.: mais detalhes sobre tipos, estruturas de dados nas seções seguintes. Na seção [extras](https://wsricardo.github.io/introprog/licao01/extras)

Operações
=================

Vamos observar um pouco agora sobre operações básicas. Como ocorre na matemática, como vimos na escola, há regras de preccedência que definem qual operação vem a ser executada primeiro.

Exemplo:

	2*4+1

é diferente de

	2*(4+1)

Isso porque a multiplicação é efetuada primeiro que a soma e a subtração. A divisão também tem precedência maior que a soma e subtração. Essa ordem de execução das operações, como visto acima, pode ser alterada usando-se parenteses.

Seu Interpretador Como Calculadora
----------------------------------

Usando o linux é possível iniciar o interpretador pelo terminal chamando o programa,

```
	$ python
```

ou

```
	$ python3
```

No Windows é possível chamar pelo menu iniciar.

Algumas operações e cálculos.

```
# importando algumas funções do módulo de funções matemática
from math import *

sin(pi/2.0) # seno de um ângulo em radianos 

sqrt(4) # raiz quadrada

2**4 # exponênciação

```

Para ver a lista de funções e constantes matemáticas disponiveis no módulo *math* 

```
	help(math)
```

mais detalhes podem ser encontradas no site www.python.org na seção de documentação (em inglês).

[Documentação Python](https://docs.python.org/)


-----------------------------------------------------


**Conteúdo** [Extras](https://wsricardo.github.io/introprog/licao01/extras) 
