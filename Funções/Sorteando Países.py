import random
def sorteia_pais(dic):
    lista_paises = []
    for pais in dic:
        lista_paises.append(pais)
    resultado = random.choice(lista_paises)
    return resultado
