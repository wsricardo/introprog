# WEB & HTML

Em nossos exemplo quando acessamos páginas da WEB através de nossos códigos obtemos determinados conteúdos especificos que descrevem o visual e funcionalidade de sites. A linguagem usada para construir esses sites chama-se *HTML* que é uma abreviação para expressão inglesa *HyperText Markup Language* que significa *Linguagem de Marcação de Hipertexto*. O *HTML* é uma linguagem de *marcação* a qual é interpretada pelos navegadores. 

Todo documento *HTML* usa marcadores (do inglês, *tags*) que palavras entre *parêntes angulares* - sinais *<* e *>* - tais marcadores são usados na formatação do conteúdo e na inserção de funcionalidades e recursos externos que definem o comportamento e o visual da página WEB. Esses recursos podem ser imagens, vídeos, scripts e arquivos CSS. Os dois últimos acrescentam funcionalidades e definem o visual respectivamente. A linguagem usada para os scripts (códigos) é a linguagem *javascript* que acrescenta recursos que podem definir ações e eventos tratados pela página conferindo mais dinamismo na exibição e tratamento do conteúdo. Já com arquivos CSS ( do inglês *Cascading Style Sheets*, folha de estlos) adiciona estilos ao site descrevendo aspectos visuais.

## HTML

Atualmente o padrão usado é o **HTML5** o qual acrescentou novos recursos aos sites e simplicações a criações do mesmo.

Vamos à um pequeno exemplo de uma página:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Meu Site</title>
  </head>
<body>
  <h1><b>Wellcome</b></h1>
  <br>
  Lista de Links
  <br>
  
  <ul>
    <li><a href="https://www.google.com">Google</a></li>
    <li><a href="https://www.github.com">Github</a></li>
    <li><a href="https://wsricardo.blogspot.com">WS Ricardo</a></li>
  </ul>	
 
</body>
</html>
```

Copie o código acima e salve com a extensão *.html (exemplo.html) e abra com seu navegador web.

Vejamos agora o significado de cada *tag*. A tag principal *html* marca a área do documento e onde todas as demais e o conteúdo serão inseridas. A tag *head* (ou cabeçalho) como nome sugeri delimita a área de recursos e informações sobre a página. Já na tag *body* temos o corpo do documento onde irá o conteúdo presente no site e tags que definirão como este conteúdo será posicionado. 

A tag *h1* especifica uma área de conteúdo destacado e importante, como por exemplo um titulo de uma seção ou artigo. O nível dessa importância em sua variação trás-nos as tags *h2*, *h3*, *h4*, *h5* e *h6*.

Já com a tag *ul* especificamos a criação de uma lista não-ordenada de elemento onde cada tag *li* define um item dessa lista.

Com a tag *a* criamos um elemento para *link* que permite redirecionar-nos para outra página da internet ou seção do site. O parâmetro href especifica para onde o link deve apontar.

Devemos notar que de modo geral e exceção de tags como *<br>* necessitamos abrir e fechar a tag. Como visto acima a tag *a* inicia com ```*<a href="https://www.google.com"> e termina com *</a>*```.

## Visual do site com CSS

Imagine que agora você deseja modifica o visual do seu site. Você pode fazê-lo adicionando CSS dentro do próprio arquivo html ou em um arquivo externo. Neste exemplo mostraremos o trecho que pode adicionar e como coloca-lo internamente ou externamente.
Vejamos:

```css
// Definições gerais de estilo para fonte e tamanho dos textos
* {
  font-family: arial, helvetica, sans-serif;
  font-size: 14pt;
}

// Definindo estilo pra visual da *lista* criada com *ul*.
ul {
  display: inline;
  list-style-type: none;
  margin: 0;
  padding: 0;

}

ul li {
	padding: 6px;
}

h1 {
	font-family: "Arial", sans-serif;
	font-style: bold;
	font-size: 60px;
}

```

salve este código dentro do arquivo *exemplo.html* dentro da tag *head* usando a tag *style* como mostrado abaixo no exemplo.

```html
<!DOCTYPE HTML>
<html>
  <head>
    <title>Meu Site</title>
    <style>
        // Meu código CSS aqui
    </style>
  <head>
<body>
  <h1>Wellcome</h1>
</body>
</html>
```

No caso de o CSS estar em um arquivo externo, tendo salvo o código CSS acima como *style.css*, por exemplo, podemos inclui-lo no *HTML* da seguinte forma,

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Meu Site</title>
    <link rel="stylesheet" href="style.css">
  <head>
<body>
  <h1>Wellcome</h1>
</body>
</html>

```

O *estilo* (*style*) para o site também pode ser inserida de forma *inline* da seguinte forma,

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Meu Site</title>
  <head>
<body>
  <h1 style="font-family: Arial Helvetica sans-serif; font-size: 40px;">Wellcome</h1>
</body>
</html>
```

Usando o parâmetro *style* dentro de uma tag neste caso a *h1* denimos a forma como conteúdo desta tag é exibido.

De modo geral o CSS tem a seguinte forma,

```css
<seletor> { 
  <declaração1>; 
  <declaração2>;
  //...
  <declaraçãon>
}
```

Onde o *seletor* (*selector* em inglês) o faz referência ao elemnto HTML no qual você deseja definir o estilo, ou seja, aspectos visuais. 

E *declaração* inclui as propriedades nas quais serão definidas as caracteriscas visuais através dos valores definidos. Por exemplo para definir a fonte e seu tamanho na tag *h1* fazemos *font-family: arial helvetica sans-serif* e *font-size: 40px* onde definiu-se a familia da fonte e seu tamanho respectivamente.

Vejamos:

```css
h1 {
  font-family: arial helvetica sans-serif; // Defini qual fonte para o texto será usada.
  font-size: 40px; // Tamanho da fonte.
}
``` 

Mais detalhes sobre o uso do html e css serão mostrados na seções seguintes.

[Conteúdo](https://wsricardo.github.io/introprog)
[Lição 2](https://wsricardo.github.io/introprog/licao02) 
