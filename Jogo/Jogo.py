print("JOGO DOS PAÍSES\nComandos:\ndica - entra no mercado de dicas")


import random
def sorteia_pais(dados):
    lista_paises = []
    for pais in dados:
        lista_paises.append(pais)
    pais_sorteado= random.choice(lista_paises)
    return pais_sorteado

pais_escolhido = sorteia_pais


