print("JOGO DOS PAÍSES\nComandos:\ndica - entra no mercado de dicas\n\nTente advinhar o país\nVocê tem 20 tentativas!")

#imports
import random
import math
from junção_das_funções import *
from Dados import *

#variaveis:
i = 0 

#funções do jogo:
dados_normalizado = normaliza(dados)
pais_escolhido = sorteia_pais(dados_normalizado)

while i < 20 :
    palpite = str(input('Qual seu palpite:    '))
    distancia_palpite = haversine(raio_terra, )
    i += 1




