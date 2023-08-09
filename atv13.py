from collections import Counter
import string

def contar_ocorrencias(texto):
 
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    palavras = texto.lower().split()
    contador = Counter(palavras)
    return contador

texto = input("Digite o texto: ")
ocorrencias = contar_ocorrencias(texto)

print("Ocorrências de palavras no texto:")
for palavra, quantidade in ocorrencias.items():
    print(f"{palavra}: {quantidade}")
