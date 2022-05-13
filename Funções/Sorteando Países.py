import random
def sorteia_pais(dados):
    lista_paises = []
    for pais in dados:
        lista_paises.append(pais)
    resultado = random.choice(lista_paises)
    return resultado
