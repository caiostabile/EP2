print("JOGO DOS PAÍSES\nComandos:\ndica - entra no mercado de dicas\n\nTente advinhar o país\nVocê tem 20 tentativas!")

#imports
import random
import math

from sklearn.decomposition import dict_learning
from junção_das_funções import *
from Dados import *

#variaveis:
i = 0
lista_paises = []
numero_de_jogadas = 20 - i 

#funções do jogo:
dados_normalizado = normaliza(dados)
pais_escolhido = sorteia_pais(dados_normalizado)
info_escolhido = dados_normalizado[pais_escolhido]
info_geo_escolhido = info_escolhido['geo']
lat_escolhido = info_geo_escolhido['latitude']
log_escolhido = info_geo_escolhido['longitude']

for ppp in dados_normalizado:
    lista_paises.append(ppp)
    print(lista_paises)

while i < 20 :
    palpite = str(input('Qual seu palpite? :  '))
    palpite = palpite.lower()
    
    if palpite in lista_paises:
        info_palpite = dados_normalizado[palpite]
        info_geo_palpite = info_palpite['geo']
        lat_palpite = info_geo_palpite['latitude']
        log_palpite = info_geo_palpite['longitude']    
        distancia_palpite = haversine(raio_terra, lat_escolhido, log_escolhido, lat_palpite, log_palpite)
        distancia_int = int(distancia_palpite)
        print('Distancia: {}'.format(distancia_int))

    elif palpite == 'dica' or palpite =='Dica':
        print('dica')
        print('1 - cor da bandeira(valor: 4 palpites)\n2 - letra da capital(valor: 3 palpites)\n3 - área(valor: 6 palpites)\n4 - população(valor: 5 palpites)\n5 - continente(valor: 7 palpites)\n0 - sem dica(valor: 0 palpites)')
        n_dica = int(input('Escolha sua opção [0 | 1 | 2 | 3 | 4 | 5]:'))

        if n_dica == 0 :
            print(numero_de_jogadas)

        if n_dica == 1:
            cores_bandeira = info_escolhido["bandeira"]
            lista_cores = []
            for cor,porcentagem in cores_bandeira.items():
                cores_bandeira[cor] = porcentagem
                if porcentagem >= 30:
                    lista_cores.append(cor)
            print(lista_cores)
            i += 4

        elif n_dica == 2:
            capital = info_escolhido["capital"]
            print(sorteia_letra(palpite,[capital[0]]))
            i += 3

        elif n_dica == 3:
            print(info_escolhido["area"])
            i += 6

        elif n_dica == 4:
            print(info_escolhido["populacao"])
            i += 5

        elif n_dica == 5:
            print(info_escolhido["continente"])
            i += 7
            
    else :
        print('país desconhecido')  
            
    i += 1
