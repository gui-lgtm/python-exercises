def imprimir_numeros_naturais(numero):
    for i in range(numero + 1):
        print(i)

try:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero >= 0:
        imprimir_numeros_naturais(numero)
    else:
        print("O número deve ser inteiro positivo.")
except ValueError:
    print("Entrada inválida. Digite um número inteiro positivo.")
