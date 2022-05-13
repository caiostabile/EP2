def esta_na_lista(nome_pais, lista_paises):
    i = 0
    for sublista in lista_paises:
        if nome_pais in sublista:
            i += 1    
    if i > 0:
        return True
    else:
        return False 