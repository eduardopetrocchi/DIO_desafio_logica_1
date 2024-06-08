# Projetos

## Projeto 1

### Descrição
Este projeto calcula o saldo de vitórias e a média de vitórias de um herói em um jogo. Com base na média de vitórias, determina-se o nível do herói.

### Código
```python
vitorias = 10
derrotas = 3

saldo = vitorias - derrotas

media = ((vitorias) / (vitorias + derrotas)) * 100

match media:
    case media if media <= 10:
        nivel = "Ferro"
    case media if media >= 11 and media <= 20:
        nivel = "Bronze"
    case media if media >= 21 and media <= 50:
        nivel = "Prata"
    case media if media >= 51 and media <= 80:
        nivel = "Ouro"
    case media if media >= 81 and media <= 90:
        nivel = "Diamante"
    case media if media >= 91 and media <= 100:
        nivel = "Lendário"
    case media if media >= 101:
        nivel = "Imortal"

media_ = round(media, 2)

print(
    f"O herói tem saldo de {saldo} vitórias e está no nível: {nivel}. \nMédia de {media_}% vitórias"
)
```

## Projeto 2

### Descrição
Este projeto classifica um herói com base em sua experiência (xp) em um jogo. Determina-se o nível do herói com base no valor de xp fornecido.

### Código
```python
def classificiarHeroi():

    if xp < 1000:
        nivel = "Ferro"
    elif xp >= 1001 and xp <= 2000:
        nivel = "Bronze"
    elif xp >= 2001 and xp <= 5000:
        nivel = "Prata"
    elif xp >= 5001 and xp <= 7000:
        nivel = "Ouro"
    elif xp >= 7001 and xp <= 8000:
        nivel = "Platina"
    elif xp >= 8001 and xp <= 9000:
        nivel = "Ascendente"
    elif xp >= 9001 and xp <= 10000:
        nivel = "Imortal"
    elif xp >= 10001:
        nivel = "Radiante"
    else:
        nivel = "Nível desconhecido"

    print(f"O Herói de nome {nome} está no nível: {nivel}")


nome = input("Digite o nome do herói: ")
xp = int(input("Digite a experiência do herói: "))

classificiarHeroi()
```

### Como Executar
Para executar cada projeto, basta copiar e colar o código em um editor de texto ou em uma IDE Python e executar o programa. 


## Projeto 3

# Jogo de Aventura - Heróis

Este projeto implementa uma classe genérica que representa um herói em uma aventura. Cada herói possui propriedades como nome, idade e tipo. Além disso, a classe inclui um método chamado `atacar` que exibe uma mensagem de ataque com base no tipo do herói.

## Estrutura do Projeto

## Funcionalidades

### Classe Heroi

A classe `Heroi` possui as seguintes propriedades:

- `nome`: O nome do herói.
- `idade`: A idade do herói.
- `tipo`: O tipo do herói (ex: guerreiro, mago, monge, ninja).

### Método atacar

O método `atacar` exibe a mensagem: "O {tipo} {nome} atacou usando {ataque}", onde:

- `{tipo}` é o tipo do herói.
- `{nome}` é o nome do herói.
- `{ataque}` depende do tipo do herói:
  - mago -> usou magia
  - guerreiro -> usou espada
  - monge -> usou artes marciais
  - ninja -> usou shuriken
Se o tipo for inválido, o método exibe a mensagem "Insira um tipo válido".
