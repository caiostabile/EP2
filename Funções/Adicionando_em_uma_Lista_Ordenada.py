def adiciona_em_ordem(pais, distancia, lista_paises):

    adicionar = [pais,distancia]
    i = 0
    if len(lista_paises) > 0 :
        tamanho = len(lista_paises)
        ultimo_ele = lista_paises[tamanho-1]   
        distancia_ultimo_elemnto = ultimo_ele[1]
    if len(lista_paises) == 0:
        resposta = lista_paises.append(adicionar)
        
    for sublista in lista_paises:
        if sublista[0] == pais:
            return lista_paises
            
        if sublista[0] != pais:
            if sublista[1] >= distancia:
                lista_paises.insert(i,adicionar)
                return lista_paises
            if distancia > distancia_ultimo_elemnto:
                lista_paises.append(adicionar)
                return lista_paises
                        
        i += 1
print(adiciona_em_ordem('chile',18000,[['libia',3678],['franca',3998],['egito',5008],['siria',5919],['india',9919],['japao',13836]]))