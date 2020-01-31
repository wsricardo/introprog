
# EXTRAS

1. Função Lambda Python
2. Uma Breve Apresentação a Linguagem C


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


## Linguagem C


**C** é uma linguagem compilada de proposito geral bastante usada na criação de programas e drivers para diversos sistemas operacionais e hardwares. É uma linguagem que permite certo controle e acesso aos recursos de um hardware. Ela foi criada em 1972 por Dennis Ritchie na empresa AT&T Bell Labs e foi usada no desenvolvimento do sistema operacional UNIX.

Esqueleto básico de um código C:

```c 
1 #include<stdio.h>
2
3 int main(int argc, char **argv){
4	// instruções.
5
6	return 0;
7}
```

Na linha 1 é incluido biblioteca de funções que serão necessárias no programa. A linha três declara a função principal **main** que é por onde o programa inicia. Já a instrução **return** como diz o nome retorna um valor neste caso significa que o programa saiu com sucesso. A funão **main** é antecedida pelo nome **int** que indica o tipo do valor que a função deve retornar neste caso um inteiro (*int* de integer).
