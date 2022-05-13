### Função 1
def normaliza(dic):
    dic_vazio={}
    for cont,pais in dic.items():
        for pais,dados in pais.items():
            dic_vazio[pais]=dados
            dic_vazio[pais]['continente']=cont
    return dic_vazio

### Função 2
import random
def sorteia_pais(dados):
    lista_paises = []
    for pais in dados:
        lista_paises.append(pais)
    resultado = random.choice(lista_paises)
    return resultado

### Função 3

### Função 4

### Função 5

### Função 6

