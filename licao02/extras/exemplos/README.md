# Exemplo 1

## Implementado Um Chatbot

Neste exemplo implementaremos um chatbot simples rodando no console (terminal de comandos). O conhecimento do bot ficará armazenado em um arquivo json e csv. Você poderá escolher um dos dois ou usar os dois. O formato json e csv é mostrado na [seção "Extras"](https://wsricardo.github.io/introprog/licao02/extras/)

O formato csv seguirá a seguinte definição:

1. Primera coluna contém as possíveis entradas do usuário.
2. Segunda coluna contém a saída que corresponderia a entrada fornecidad.
3. Cada linha na tabela construida no arquivo _cvs_ referência as possíveis combinações de entrada e saída.

Exemplo:

Entrada | Saída
-----------------
Oi		|	Olá
Como vai?	| Eu estou bem obrigado. E você?

Em csv a tabela acima poderia ficar como se segue

"Entrada"	,	"Saída"

"Oi"	,	"Olá"

Como vai?	,	"Eu estou bem obrigado. E você?"



A virgula serve para delimitar os campos e as aspas envolvem o valor de cada campo. A quebra de linha ("pulando uma linha") indica-se uma nova linha na tabela. Observe as duas contruções acima.

Vamos ao código!


Primeiro desejamos que nosso código continue executando até que o usuário deseje encerrar a conversa com nosso robô.

```
entrada = ''
continuar = True
idkey = ''

dados = { 
	"Oi": "Olá",
	"Como vai?":"Eu vou bem obrigada. E você como está?",
	"Estou bem.":"Que bom",
	"Bem": "Que bom. :)",
}

while continuar:
	entrada = input(">> ")
	if entrada.lower() in str.lower(dados.keys()):
		print(">> {}".format(dados[entrada]))
	
```

Observe que temos o *loop while* para repetir um bloco de código especifico e a estrutura *if* para testar a condição e verificar qual a resposta o robô deve enviar ao usuário.

O código acima é uma implementação bem simples. Poderiamos considerar outras situações onde o usuário deseja saber como o robô está expressando tal ideia de forma diferente variando palavras. Mas neste caso de estudo só avaliaremos as estruturas e a interação feita com usuário.

## Curiosidades

Existe recursos que auxiliam na criação de robôs com um nível de inteligência maior sendo capazes até de aprender através de cada nova interação com o usuário. Esse campo que prover tais ferramentas para tal é o da inteligência artificial neste nos deparemos com questões ligadas por exemplo à *processamento de linguagem natural* e *aprendizado de máquina* conhecida como *machine learning*.
