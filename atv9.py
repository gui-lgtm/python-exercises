def converter_para_maiusculas(lista):
    nova_lista = []
    for palavra in lista:
        nova_lista.append(palavra.upper())
    return nova_lista


lista_strings = ["hello", "world", "python", "programming"]
lista_maiusculas = converter_para_maiusculas(lista_strings)
print(lista_maiusculas)