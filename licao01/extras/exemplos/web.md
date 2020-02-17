# WEB & HTML

Em nossos exemplo quando acessamos páginas da WEB através de nossos códigos obtemos determinados conteúdos especificos que descrevem o visual e funcionalidade de sites. A linguagem usada para construir esses sites chama-se *HTML* que é uma abreviação para expressão inglesa *HyperText Markup Language* que significa *Linguagem de Marcação de Hipertexto*. O *HTML* é uma linguagem de *marcação* a qual é interpretada pelos navegadores. 

Todo documento *HTML* usa marcadores (do inglês, *tags*) que palavras entre *parêntes angulares* - sinais *<* e *>* - tais marcadores são usados na formatação do conteúdo e na inserção de funcionalidades e recursos externos que definem o comportamento e o visual da página WEB. Esses recursos podem ser imagens, vídeos, scripts e arquivos CSS. Os dois últimos acrescentam funcionalidades e definem o visual respectivamente. A linguagem usada para os scripts (códigos) é a linguagem *javascript* que acrescenta recursos que podem definir ações e eventos tratados pela página conferindo mais dinamismo na exibição e tratamento do conteúdo. Já com arquivos CSS ( do inglês *Cascading Style Sheets*, folha de estlos) adiciona estilos ao site descrevendo aspectos visuais.

## HTML

Atualmente o padrão usado é o **HTML5** o qual acrescentou novos recursos aos sites e simplicações a criações do mesmo.

Vamos à um pequeno exemplo de uma página:

```html
<DOCTYPE html>
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

```
<!DOCTYPE HTML>
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
