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
import math
def haversine(raio_terra,l1,f1,l2,f2):
    parte1=(math.sin(math.radians((l2-l1)/2)))**2
    parte2=math.cos(math.radians(l1))* math.cos(math.radians(l2))*(math.sin(math.radians((f2-f1)/2)))**2
    resposta = 2*r*math.asin((parte1+parte2)**0.5)
    return resposta

### Função 4

### Função 5

### Função 6

