# JavaScript

## Documentação Oficial

---

https://developer.mozilla.org/pt-BR/docs/Learn/JavaScript/First_steps/What_is_JavaScript

 [Guia de JavaScript: o que é e como aprender a linguagem mais popular do mundo?](https://www.alura.com.br/artigos/javascript)

## Template Strings

---

```jsx
alert(`Isso ai! Você descobriu o número secreto ${numeroSecreto}`);
```

## Operadores Lógicos

---

### AND (&&)

```jsx
let idade = 25;
let possuiCarteira = true;

// se idade é maior que 18 e possui carteira…
if (idade > 18 && possuiCarteira) {
  console.log("Pode dirigir!");
} else {
  console.log("Não pode dirigir.");
}
```

### OR (||)

```jsx
let temMaça = false;
let temBanana = true;

// se tem maça ou tem banana…
if (temMaça || temBanana) {
  console.log("Você tem frutas!");
} else {
  console.log("Não tem frutas.");
}
```

### Operador Ternário

```jsx
// Tentativa é igual a 1? Senão, colocar tentativas;
let palavraTentativa = tentativas == 1 ? 'tentativa' : 'tentativas';
```

## Math Random()

---

<aside>
<img src="https://www.notion.so/icons/code_gray.svg" alt="https://www.notion.so/icons/code_gray.svg" width="40px" /> **`Math.random()`** gera um número aleatório entre 0 e 1 com diversas casas decimais

**`parseInt`** basicamente força o resultado a ser um “int”, descartando as casas decimais

</aside>

Exemplo :

```jsx
parseInt(Math.random() * 10 + 1);
```

## HTML + JavaScript

---

<aside>
<img src="https://www.notion.so/icons/code_gray.svg" alt="https://www.notion.so/icons/code_gray.svg" width="40px" /> **`document`**  fornece acesso a todos os elementos e estruturas do documento HTML

**`querySelector`**  seleciona a TAG que você esteja tentando acessar o conteúndo no documento HTML

**`.innerHTML`**  modifica o código HTML de um elemento na página. NÃO É UM INPUT.

</aside>

Exemplo :

```jsx
// Cria uma função que consegue acessar o tag e o texto do html
function exibirTextoNaTela(tag, texto) {

    // document = acessa o script html | querySelector acessa o tag especificado
    let campo = document.querySelector(tag);
    // innerHTML atribui um valor dentro da variável que está no HTML
    campo.innerHTML = texto;
}
```

<aside>
<img src="https://www.notion.so/icons/code_gray.svg" alt="https://www.notion.so/icons/code_gray.svg" width="40px" /> **`document.getElementById("valor-total")`**  recupera a tag referente a esse id, no caso, valor-total

**`.value`**  recupera valores digitados em campos de um formulário na página. É UM INPUT.

**`.innerHTML`**  modifica o código HTML de um elemento na página.

</aside>

Exemplo :

```jsx
// document.getElementById("produto") RETORNA A TAG HTML - Tem que usar o .value para acessar o valor
    let produto = document.getElementById("produto").value;
```

## Slicing and Dicing

---

<aside>
<img src="https://www.notion.so/icons/code_gray.svg" alt="https://www.notion.so/icons/code_gray.svg" width="40px" /> `split()` separa trechos de uma String por um determinado delimitador;

</aside>

Exemplo:

```jsx
// .split quebra a string em arrays determinados pelo caracter divisório - entre chaves a posição do array
    let nomeProduto = produto.split("-")[0];
    let valorProduto = produto.split("R$")[1];

// Nesse caso, "Fone de ouvido - R$200" ficou:
// nomeProduto = Fone de ouvido
// valorProduto = 200
```

## Responsive Voice

---

<aside>
<img src="https://www.notion.so/icons/code_gray.svg" alt="https://www.notion.so/icons/code_gray.svg" width="40px" /> Permite que o texto mostrado na tela seja falado: `responsiveVoice(conteúdo a ser dito, língua, velocidade da fala)`

</aside>

Exemplo:

```jsx
    responsiveVoice.speak(texto, 'Brazilian Portuguese Female', {rate: 1.2});
```