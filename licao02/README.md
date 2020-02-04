# Estruturas de Controle

Muitas vezes você deseja que o programa repita algumas ações ou selecione uma outra ação caso algo seja necessário.
Para tanto linguagens de programação em geral possuem *estruturas* que permitem você controlar a execução de seu programa. Tais estruturas são as codicionais e as de repetição.
As estruturas condicionais desviam a execução de um trecho caso uma condição seja satisfeita. Já as estruturas de repetição repetem trechos de ações especificadas.

Em python essas estruturas são como veremos abaixo.

## Condicionais

Como dito determinam a execução de trecho de código caso uma condição esteja satisfeita. Ou seja permite o programador desviar de um bloco de código a outro seguinte de acordo com a *condição* definida.

Para python temos If, Elif, Else.

Analisemos o seguinte trecho de código:


```
	>>> idade = 23
	>>> if idade >= 18:
	...	print("Você é maior de idade!")
	>>>
```

No exemplo a *condição* definida é **idade** ser maior ou igual a 18 anos. Como idade recebeu 23, logo a linha contendo o **print** será executda. Experimente alterar o trecho acima e atribuir um valor menor que 18 a idade e veja o resultado.

Caso precise avaliar outras condições ou dterminar outras ações ou condições a serem analizadas caso a primeira falhe pode se usar o **elif** e o **else**.

```
	>>> idade = 12
	>>> if idade >= 18:
	...	print("Você é maior de idade!")
	... else:
	...	print("Você é menor de idade!")
	Você é menor de idade!
	>>>
```

Neste segundo exemplo usando-se o **else** se estabelece um caminho alternativo e uma ação para o caso que a idade é menor que 18.

Mas imagine uma situação onde quer selecionar, separando em jovens, adultos e idosos.

```
	idade = 45
	if idade =< 29:
		print("Você é jovem!")
	elif idade > 29 and idade < 60:
		print("Você é um adulto.")
	else:
		print("Você possui mais de 60 anos. É um idoso.")
```

Abra um editor de texto e digite esse exemplo acima. E execute com interpretador python.
Para este exemplo logo acima a saída será  "*Você é um adulto.*".

Observe neste último exemplo o uso do **and** que é um conectivo lógico. Ele serviu para conectar as duas condições formando uma condição formada por duas partes onde as duas precisam ser verdadeiras simultaneamente para termos o *print* de "Você é um adulto.* ser exibido na tela.

Vejamos alguns operadores lógicos.

* And -> E  
* Or -> Ou 
* Not -> Não

Obs.: O valor **1** representa sentença *verdadeira* e **0** para *falso*.

Pensamos em **A** e **B** como proposições, ou afirmações. 
(Do código acima **A** e **B** seriam as condições.)

Tabela

| **A** | **B** | **A** and **B** | **A** or **B** |
|-------|-------|-----------------|----------------|
|   1   |   1   |       1         |       1        |
|   1   |   0   |       0         |       1        |
|   0   |   1   |       0         |       1        |
|   0   |   0   |       0         |       0        |


| **A** | not **A** | 
|-------|-----------|
|   1   |     0     |
|   0   |     1     |



### Operações Lógicas

Alguns exemplos. Operadores **and**, **or** e **not**.


```python
	>>> True and False
	False
	>>> True and True
	True
	>>> False and False
	False
	>>>
	>>> True or False
	True
	>>> False or False
	False
	>>> True or True
	True
	>>>
	>>> not True
	False
	>>> not False
	True

```

Suponha agora que temos idade1 = 23  e idade2 = 12, observemos a tabela. 
(Sabendo que a maioridade é atingida aos 18 anos.)

Definindo **A** e **B**

A := idade1 > 18,
B := idade2 < 18

|             |           |    
|-------------|-----------| 
| idade1 > 18 |    1      |
| idade2 < 18 |    0      |
|-------------|-----------|
|   A and B   |    0      |
|-------------|-----------|
|   A or B    |    1      | 


## Estruturas de Repetição

Para repetição de trecho de códigos temos a estrutura do **for** e **while** ambos criam loops
onde um trecho interno apos o for ou while são executados.

Exemplo básico com *for*

```python
	>>> for i in range(5):
	...	print(i)
	...
	0
	1
	2
	3
	4
	>>>
```

O **for** (*para* em português) cria um loop onde a intrução dentro do **for** é executada cinco vezes. Neste caso acima a função **range**
gera a uma lista com inteiro de 0 até 4, ou seja, [0,1,2,3,4] onde a variavel **i** irá assumir a cada
repetição um valor presente na lista.

Vejamos uma tabela para verificar a execução do trecho acima a cada passo da repetição.

| passo |      a     |
|-------|------------|
|   1   |      0     |
|   2   |      1     |
|   3   |      2     |
|   4   |      3     |
|   5   |      4     |

No primeiro passo, **a** é iguai 0, no passo 2 **a** é 1, e assim por diante.

Vejamos um exemplo para o uso da estrutura **while** (*enquanto* em português).

Imaginemos que desejamos somar os números de 1 até 6 por exemplo.

Algo como, soma = 1 + 2 + 3 + 4 + 5 + 6,

```python
	>>> soma = 0
	>>> i = 1
	>>> while i <= 6
	...	soma = soma + i
	...	i = i + 1
	...
	>>>
	>>> print(soma)
	21
	>>>
```

Usaremos uma tabela para fazer o *teste de mesa* do código.

| passo |   instrução   |  i     | soma  |
|-------|---------------|--------|-------|
|   1   |soma = soma + i|   1    |   1   |
|   2	|  "            |   2    |   3   |
|   3   |  "            |   3    |   6   |
|   4   |   "           |   4    |   10  |
|   5   |   "           |   5    |   15  |
|   6   |   "           |   6    |   21  |

No passo **6** a variavel **soma** estará armazenando o valor 21 que é o resultado da soma dos inteiros de 1 até 6 desrito no código acima.

A tabela acima para soma ilustra o processo da execução do loop **while**, que é uma estrutura de repetição assim como o **for**.

Usando as *tabelas* como as acima é possível analisar os resultados das operações lógicas nas condições usadas em loops e estruturas condicionaais como também avaliar os valores armazenados nas variáveis a cada passo da eexecução do código.
