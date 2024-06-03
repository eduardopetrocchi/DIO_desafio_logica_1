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
