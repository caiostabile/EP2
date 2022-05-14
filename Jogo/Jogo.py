continua_jogo = True
while continua_jogo == True:
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


#funções do jogo:
    dados_normalizado = normaliza(dados)
    pais_escolhido = sorteia_pais(dados_normalizado)

    info_escolhido = dados_normalizado[pais_escolhido]

    info_escolhido = dados_normalizado[pais_escolhido]

    info_geo_escolhido = info_escolhido['geo']
    lat_escolhido = info_geo_escolhido['latitude']
    log_escolhido = info_geo_escolhido['longitude']

    for ppp in dados_normalizado:
        lista_paises.append(ppp)
    


    while i < 20 and continua_jogo == True:
        print("\n\nQuantidade de palpites: {}".format(20-i))
        palpite = str(input('Qual seu palpite? :  '))
        palpite = palpite.lower()
    
    
        if palpite in lista_paises:
            info_palpite = dados_normalizado[palpite]
            info_geo_palpite = info_palpite['geo']
            lat_palpite = info_geo_palpite['latitude']
            log_palpite = info_geo_palpite['longitude']    
            distancia_palpite = haversine(raio_terra, lat_escolhido, log_escolhido, lat_palpite, log_palpite)
            distancia_int = int(distancia_palpite)

            if palpite != pais_escolhido:
                if i < 20:
                    if 20 - i == 1:
                        i += 2
                    else:
                        if distancia_int < 1000 :
                            print('Distancia em relação ao {}  {} Km'.format(palpite,distancia_int))
                        if distancia_int > 1000 and distancia_int <= 3000 :
                            print('Distancia em relação ao {}  {} Km'.format(palpite,distancia_int))
                        if distancia_int > 3000 :
                            print('Distancia em relação ao {}  {} Km'.format(palpite,distancia_int))
                        i += 1
            elif palpite == pais_escolhido:
                print("PARABÉNS VOCÊ ACETOU!")
                continua_jogo = False
                i = 22
        

        elif palpite == 'dica' or palpite =='Dica':
            print('MERCADO DE DICAS')
            print('1 - cor da bandeira(valor: 4 palpites)\n2 - letra da capital(valor: 3 palpites)\n3 - área(valor: 6 palpites)\n4 - população(valor: 5 palpites)\n5 - continente(valor: 7 palpites)\n0 - sem dica(valor: 0 palpites)')
            n_dica = int(input('Escolha sua opção [0 | 1 | 2 | 3 | 4 | 5]:'))

            if n_dica == 1:
                cores_bandeira = info_escolhido["bandeira"]
                lista_cores = []
                for cor,porcentagem in cores_bandeira.items():
                    cores_bandeira[cor] = porcentagem
                    if porcentagem >= 30:
                        lista_cores.append(cor)
                if 20 - i > 4:
                    print("Cores da bandeira {}". format(lista_cores))
                    i += 4
                elif 20 - i == 4:
                    i += 5
                else:
                    print("Você nao tem palpites suficientes!")

            elif n_dica == 2:
                capital = info_escolhido["capital"]
                if 20 - i > 3:
                    print("Uma letra da capital: {}". format(sorteia_letra(palpite,[capital[0]])))
                    i += 3
                elif 20 - i == 3:
                    i += 4
                else: 
                    print("Você nao tem palpites suficientes!")
            elif n_dica == 3:
                if 20 - i > 6:
                    print("Área: {} Km".format(info_escolhido["area"]))
                    i += 6
                elif 20 - i == 6:
                    i += 7
                else: 
                    print("Você nao tem palpites suficientes!")

            elif n_dica == 4:
                if 20 - i > 5:
                    print("População: {} habitantes".format(info_escolhido["populacao"]))
                    i += 5
                elif 20 - i == 5:
                    i += 6
                else: 
                    print("Você nao tem palpites suficientes!")

            elif n_dica == 5:
                if 20 - i > 7:
                    print("Continente: {}".format(info_escolhido["continente"]))
                    i += 7
                elif 20 - i == 7:
                    i += 8
                else: 
                    print("Você nao tem palpites suficientes!")
            
        else :
            print('país desconhecido')  

    if i == 21:
        print("VOCÊ PERDEU!\nO país era {}".format(pais_escolhido))
        i = 22

    if i == 22:
        voltar = input("Deseja votar a jogar? [s/n]")
        if voltar == 's':
            continua_jogo = True
            i = 0
        if continua_jogo == 'n':

            continua_jogo = False




