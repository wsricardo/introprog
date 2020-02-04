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

Obs.: O valor **1** representa sentença *verdadeira* e **0** para falso.

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




