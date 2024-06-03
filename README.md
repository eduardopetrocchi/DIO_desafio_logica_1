# Desafio Classificador de Nível de Herói

Este repositório contém a solução para o desafio "Classificador de Nível de Herói" proposto pela DIO. O objetivo é criar um script em Python que classifica o nível de um herói com base em sua experiência (XP).

## Objetivo do Desafio

O objetivo é armazenar o nome e a quantidade de experiência (XP) de um herói em variáveis e, utilizando uma estrutura de decisão, determinar e exibir o nível do herói conforme a quantidade de XP.

### Classificação dos Níveis

- XP < 1000: Ferro
- 1001 <= XP <= 2000: Bronze
- 2001 <= XP <= 5000: Prata
- 5001 <= XP <= 7000: Ouro
- 7001 <= XP <= 8000: Platina
- 8001 <= XP <= 9000: Ascendente
- 9001 <= XP <= 10000: Imortal
- XP >= 10001: Radiante

## Estrutura do Projeto

Este projeto utiliza conceitos fundamentais de programação, incluindo:
- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisão

## Instruções de Uso

1. Clone o repositório para sua máquina local.
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```
2. Navegue até o diretório do projeto.
    ```bash
    cd seu-repositorio
    ```
3. Execute o script Python.
    ```bash
    python classificacao_heroi.py
    ```
4. Siga as instruções no terminal para digitar o nome e a experiência (XP) do herói.

## Código

O código abaixo realiza a classificação do herói com base na experiência fornecida:

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



## Autores

- [@eduardopetrocchi](https://github.com/eduardopetrocchi)

