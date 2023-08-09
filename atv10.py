def encontrar_maior_menor_numero(sequencia):
    if not sequencia:
        return None, None  

    maior_numero = menor_numero = sequencia[0]

    for numero in sequencia:
        if numero > maior_numero:
            maior_numero = numero
        elif numero < menor_numero:
            menor_numero = numero

    return maior_numero, menor_numero

entrada = input("Digite a sequência de números separados por espaços: ")
numeros = [int(x) for x in entrada.split()]

maior, menor = encontrar_maior_menor_numero(numeros)

if maior is not None and menor is not None:
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
else:
    print("Sequência vazia, não é possível encontrar o maior e o menor número.")
