### Função 1
def normaliza(dados):
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
def adiciona_em_ordem(nome_pais, distancia, lista_paises):

    adicionar = [nome_pais,distancia]
    i = 0
    if len(lista_paises) > 0 :
        tamanho = len(lista_paises)
        ultimo_ele = lista_paises[tamanho-1]   
        distancia_ultimo_elemnto = ultimo_ele[1]
    if len(lista_paises) == 0:
        resposta = lista_paises.append(adicionar)
        
    for sublista in lista_paises:
        if sublista[0] == nome_pais:
            return lista_paises
            
        if sublista[0] != nome_pais:
            if sublista[1] >= distancia:
                lista_paises.insert(i,adicionar)
                return lista_paises
            if distancia > distancia_ultimo_elemnto:
                lista_paises.append(adicionar)
                return lista_paises
                        
        i += 1

### Função 5
def esta_na_lista(pais, lista_paises):
    i = 0
    for sublista in lista_paises:
        if nome_pais in sublista:
            i += 1    
    if i > 0:
        return True
    else:
        return False 

### Função 6 !!!
import random
def sorteia_letra(palavra,lista_restrita):
    letras_sorteio = []
    caracteres_especiais = ['.', ',', '-', ';', ' ']
    for letra in palavra:
        letra=letra.lower()
        if letra not in lista_restrita and letra not in caracteres_especiais:
            letras_sorteio.append(letra)
            if len(letras_sorteio) == 0:
                resultado = ''
            else:
                resultado = random.choice(letras_sorteio)
        

    return resultado

