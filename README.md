# Aplicativo Restaurantes


## Resumo



Esse projeto consiste em uma simulação das funcionalidades iniciais de uma aplicativo de restaurantes. Nele, é possível escolher o restaurante, o cardápio e a média da avaliação dos clientes. 

## Estrutura


Com o intuito de organizar as funcionalidades e informações do projeto, foram desenvolvidas a seguinte estrutura de arquivos:

- [modelos](#modelos)
    - [cardapio](#cardapio)
      -   [bebida](#bebida)
        - [item_cardapio](#item_cardapio)
        - [prato](#prato)
  - [avaliacao](#avaliacao)
  - [restaurante](#restaurante)
    - [Observações](#Observações)
- [app](#app)



## modelos



Dentro da pasta **modelos** foram alocadas todas as funcionalidades e estruturas que o aplicativo contém. 

## cardapio



A pasta **cardapio** agrupa todos os arquivos que referentes a consulta e exibição do cardápio dos restaurantes. 

## bebida



O arquivo bebida.py tem como função criar a classe que irá instanciar o atributo `tamanho` e herdar os atributos `nome` e `preço` da classe pai `ItemCardapio`. Essa bebida representa a escolha do cliente ao utilizar o aplicativo. 

**OBS**: Conforme o código abaixo, foi criada classe `Bebida` utilizando como parâmetro a classe `ItemCardapio`, fazendo-se necessária sua importação.

```python
from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        # Objeto super() permite que você acesse informações da classe ItemCardapio
        super().__init__(nome, preco)
        self.tamanho = tamanho
```

Nesse cenário, utiliza-se o objeto `super()` para acessar o método construtor da classe pai `ItemCardapio` , inicializando os atributos `nome` e `preco`.

## item_cardapio



Além de ser a classe pai para as classes `Bebida` e `Prato`, instanciando os atributos `nome` e `preco`, a classe ItemCardapio tem um peculiariedade. Essa classe tem a responsabilidade de “forçar” as classe filhas a possuírem o método `aplicar_desconto()`, através do uso do decorador `@abstractmethod`, conforme código abaixo:

```python
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    # Classe abstrata = Força as classes 'filhas' a obrigatoriamente terem esse método
    @abstractmethod
    def aplicar_desconto(self):
        pass
```

## prato



O arquivo prato.py tem como função criar a classe que irá instanciar o atributo `descricao` e herdar os atributos `nome` e `preço` da classe pai `ItemCardapio`. Seguindo as mesmas características da classe `Bebida`. Esse prato representa a escolha do cliente ao utilizar o aplicativo. 

## avaliacao



Arquivo responsável por criar a classe `Avaliacao` que instancia os atributos `cliente` e `nota`. A ideia é representar um sistema de avaliação na qual o cliente coloca seu nome e o número de estrelas daquele restaurante, referente a qualidade da sua experiência. 

## restaurante



Principal arquivo do projeto, o restaurante.py é responsável por criar a principal classe do sistema: `Restaurante` . Nela, são realizadas ações muito importantes como: 

1. Criar e listar os restaurantes.
2. Alterar e indicar se os restaurantes estão ativos.
3. Adicionar e exibir as avaliações dos clientes.
4. Incluir e exibir itens no cardápio.

### Observações


Conforme código abaixo, no método `listar_restaurantes()` utiliza-se o decorador `@classmethod` , indicando que o método `listar_restaurantes()` é um método de classe. Isso significa que ele pode ser chamado diretamente na classe `Restaurante` sem a necessidade de instanciar um objeto da classe. Conforme código abaixo:

```python
@classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')
```

No método `ativo()`, utiliza-se o decorador `@property`, definindo que esse método pode ser acessado como um atributo. Isso indica que o método é destinado apenas para visualização, não para modificação.

```python
@property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
```

```python
def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): # Verifica se o item inserido é uma instância da classe ItemCardapio
            self._cardapio.append(item)
```

## app


O arquivo `app.py` serve como um script principal para instanciar e manipular objetos das classes `Restaurante`, `Bebida` e `Prato`. Ele demonstra a criação de um restaurante, a adição de itens ao cardápio, a aplicação de descontos, a recepção de avaliações, e a exibição do cardápio e lista de restaurantes.
