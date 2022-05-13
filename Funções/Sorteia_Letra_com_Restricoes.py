import random
def sorteia_letra(palavra,lista_restrita):
    letras_sorteio = []
    caracteres_especiais = ['.', ',', '-', ';', ' ']
    for letra in palavra:
        letra =letra.lower()
        if letra not in lista_restrita and letra not in caracteres_especiais:
            letras_sorteio.append(letra)
    if len(letras_sorteio) == 0:
                resultado = ''
    else:
                resultado = random.choice(letras_sorteio)
    return resultado
