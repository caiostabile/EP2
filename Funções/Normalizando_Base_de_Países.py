def normaliza(dic):
    novo_dic = {}
    for Continente in dic:
        continente = dic[Continente]
        nome_continente = Continente
        for pais in continente:
            país = continente[pais]
            area = país["area"]
            população = país["populacao"]
            geo = país["geo"]
            latitude = geo["latitude"]
            longitude = geo["longitude"]
            bandeira = país["bandeira"]
            vermelha = bandeira["vermelha"]
            laranja = bandeira["laranja"]
            amarela = bandeira["amarela"]
            verde = bandeira["verde"]
            azul = bandeira["azul"]
            azul_claro = bandeira["azul claro"]
            preta = bandeira["preta"]
            branca = bandeira["branca"]
            outras = bandeira["outras"]

            país_nd = {
            "area": area,
            "população": população,
            "geo":{
            "latitude": latitude,
            "longitude":longitude
            },
            "bandeira":{
            "vermelha": vermelha,
            "laranja": laranja,
            "amarela": amarela,
            "verde": verde,
            "azul": azul,
            "azul_claro": azul_claro,
            "preta": preta,
            "branca": branca,
            "outras": outras 
            },
            "continente": nome_continente
            }

            novo_dic[pais] = país_nd
        
    return novo_dic
        
