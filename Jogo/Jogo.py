print("JOGO DOS PAÍSES\nComandos:\ndica - entra no mercado de dicas\n\nTente advinhar o país\nVocê tem 20 tentativas!")

#imports
import random
import math
from junção_das_funções import *
from Dados import *

#variaveis:
i = 0
lista_paises = []

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
    
    if palpite in lista_paises:
        info_palpite = dados_normalizado[palpite]
        info_geo_palpite = info_palpite['geo']
        lat_palpite = info_geo_palpite['latitude']
        log_palpite = info_geo_palpite['longitude']    
        distancia_palpite = haversine(raio_terra, lat_escolhido, log_escolhido, lat_palpite, log_palpite)
        distancia_int = int(distancia_palpite)
        print('Distancia: {}'.format(distancia_int))

    elif palpite == 'dica':

    
        

            
    i += 1




