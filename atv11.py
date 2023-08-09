import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Tente um número maior.")
            elif palpite > numero_secreto:
                print("Tente um número menor.")
            else:
                acertou = True
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")

        except ValueError:
            print("Por favor, digite um número válido.")

jogo_adivinhacao()
