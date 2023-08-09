def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)

    if tamanho % 2 == 1:
    
        mediana = lista_ordenada[tamanho // 2]
    else:
       
        meio1 = lista_ordenada[tamanho // 2 - 1]
        meio2 = lista_ordenada[tamanho // 2]
        mediana = (meio1 + meio2) / 2

    return mediana

lista_numeros = [10, 5, 2, 8, 7]
mediana = calcular_mediana(lista_numeros)
print(f"A mediana da lista é: {mediana}")
