import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def calcular_soma(dado1, dado2):
    return dado1 + dado2

dado1, dado2 = lancar_dados()
soma = calcular_soma(dado1, dado2)

print(f"Resultado do dado 1: {dado1}")
print(f"Resultado do dado 2: {dado2}")
print(f"Soma dos resultados: {soma}")
