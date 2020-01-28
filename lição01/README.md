
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

 
