def numeros_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = numeros_pares(lista_original)
print(lista_pares)  