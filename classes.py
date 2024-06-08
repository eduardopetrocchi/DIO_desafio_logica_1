class Heroi:
    def __init__(self, nome: str, idade: int, tipo: str) -> None:
        self.nome = nome
        self.idade = idade
        self.tipo = tipo


def atacar(tipo, ataque=""):

    if tipo == "mago":
        ataque = "magia"
    elif tipo == "guerreiro":
        ataque = "espada"
    elif tipo == "monge":
        ataque = "artes marciais"
    elif tipo == "ninja":
        ataque = "shuriken"
    else:
        print("Insira um tipo válido")
        return

    print(f"o {tipo} atacou usando {ataque}")


atacar("mago")
atacar("guerreiro")
atacar("monge")
atacar("ninja")
atacar("nin")
