def encontrar_maior_menor_palavra(lista):
    if not lista:
        return None, None 

    maior_palavra = menor_palavra = lista[0]

    for palavra in lista:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
        elif len(palavra) < len(menor_palavra):
            menor_palavra = palavra

    return maior_palavra, menor_palavra


entrada = input("Digite as palavras separadas por espaços: ")
palavras = entrada.split()

maior, menor = encontrar_maior_menor_palavra(palavras)

if maior and menor:
    print(f"Maior palavra: {maior}")
    print(f"Menor palavra: {menor}")
else:
    print("Lista vazia, não é possível encontrar a maior e a menor palavra.")
