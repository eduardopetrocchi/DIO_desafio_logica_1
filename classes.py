class Heroi:
    def __init__(self, nome: str, idade: int, tipo: str) -> None:
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = ""
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            print("Insira um tipo válido")
            return

        print(f"O {self.tipo}{self.nome} atacou usando {ataque}")


heroi1 = Heroi("Merlin", 150, "mago")
heroi2 = Heroi("Arthur", 35, "guerreiro")
heroi3 = Heroi("Shaolin", 40, "monge")
heroi4 = Heroi("Hanzo", 25, "ninja")
heroi5 = Heroi("Desconhecido", 30, "nin")

heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
heroi5.atacar()