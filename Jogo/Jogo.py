continua_jogo = True
while continua_jogo == True:
    print("JOGO DOS PAÍSES\nComandos:\ndica - entra no mercado de dicas\n\nTente advinhar o país\nVocê tem 20 tentativas!")

#imports
    import random
    import math

    from sklearn.decomposition import dict_learning
    from junção_das_funções import *
    from Dados import *
    from colorama import Fore, Back, Style
#variaveis:
    i = 0
    lista_paises = []
    lista_dicas = [0,1,2,3,4,5]
    dicas_usadas = []

#funções do jogo:
    dados_normalizado = normaliza(dados)
    pais_escolhido = sorteia_pais(dados_normalizado)
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
        num_palpites = 20 - i 
    
    
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
                            print(Fore.GREEN+'\n{} ------> {} Km\n'.format(palpite,distancia_int)+Style.RESET_ALL)
                        if distancia_int > 1000 and distancia_int <= 3000 :
                            print(Fore.BLUE+'\n{} ------> {} Km\n'.format(palpite,distancia_int)+Style.RESET_ALL)
                        if distancia_int > 3000 :
                            print(Fore.RED+'\n{} ------> {} Km\n'.format(palpite,distancia_int)+Style.RESET_ALL)
                        i += 1
            elif palpite == pais_escolhido:
                print(Fore.GREEN+'\nPARABÉNS VOCÊ ACETOU!\n'+Style.RESET_ALL)
                continua_jogo = False
                i = 22
        
# DICAS
            
            dicas_usadas = []

        elif palpite == 'dica' or palpite =='Dica':
            print('MERCADO DE DICAS')

            lista_dicas = []

            lista_dicas.append(0)

            if num_palpites > 4:
                if 1 not in dicas_usadas:
                    print('1 - cor da bandeira(valor: 4 palpites)')
                    lista_dicas.append(1)
            
            if num_palpites > 3:
                if 2 not in dicas_usadas:
                    print('2 - letra da capital(valor: 3 palpites)')
                    lista_dicas.append(2)
            
            if num_palpites > 6:
                if 3 not in dicas_usadas:
                    print('3 - área(valor: 6 palpites)')
                    lista_dicas.append(3)

            if num_palpites > 5:
                if 4 not in dicas_usadas:
                    print('4 - população(valor: 5 palpites)')
                    lista_dicas.append(4)
            
            if num_palpites > 7:
                if 5 not in dicas_usadas:
                    print('5 - continente(valor: 7 palpites)')
                    lista_dicas.append(5)


            print('0 - sem dica(valor: 0 palpites)')

            n_dica = int(input('Escolha sua opção {}:'.format(lista_dicas)))

            

            if n_dica == 1 and 1 in lista_dicas:
                cores_bandeira = info_escolhido["bandeira"]
                lista_cores = []
                for cor,porcentagem in cores_bandeira.items():
                    cores_bandeira[cor] = porcentagem
                    if porcentagem >= 30:
                        lista_cores.append(cor)
                
                print("Cores da bandeira {}". format(lista_cores))
                i += 4
                dicas_usadas.append(1)
               

            elif n_dica == 2 and 2 in lista_dicas:
                capital = info_escolhido["capital"]
                print("Uma letra da capital: {}". format(sorteia_letra(palpite,[capital[0]])))
                i += 3
                dicas_usadas.append(2)


            elif n_dica == 3 and 3 in lista_dicas:
                print("Área: {} Km".format(info_escolhido["area"]))
                i += 6
                dicas_usadas.append(3)
                
            elif n_dica == 4 and 4 in lista_dicas:
                print("População: {} habitantes".format(info_escolhido["populacao"]))
                i += 5
                dicas_usadas.append(4)

            elif n_dica == 5 and 5 in lista_dicas:
                print("Continente: {}".format(info_escolhido["continente"]))
                i += 7
                dicas_usadas.append(5)
 
            
        elif palpite not in lista_paises :
            print('país desconhecido')  

    if i == 21:
        print(Fore.RED+"\nVOCÊ PERDEU!\nO país era {}\n".format(pais_escolhido)+Style.RESET_ALL)
        i = 22

    if i == 22:
        voltar = input("Deseja votar a jogar? [s/n]")
        if voltar == 's':
            continua_jogo = True
            i = 0
        if continua_jogo == 'n':
            continua_jogo = False                
