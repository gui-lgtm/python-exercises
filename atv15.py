def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    escolha = input("Digite 'C' para converter de Celsius para Fahrenheit ou 'F' para converter de Fahrenheit para Celsius: ").upper()

    if escolha == 'C':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius} Celsius equivalem a {fahrenheit:.2f} Fahrenheit.")
    elif escolha == 'F':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit equivalem a {celsius:.2f} Celsius.")
    else:
        print("Escolha inválida. Por favor, digite 'C' ou 'F'.")

if __name__ == "__main__":
    main()
