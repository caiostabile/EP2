def normaliza(dic):
    dic_vazio={}
    for cont,pais in dic.items():
        for pais,dados in pais.items():
            dic_vazio[pais]=dados
            dic_vazio[pais]['continente']=cont
    return dic_vazio
        
