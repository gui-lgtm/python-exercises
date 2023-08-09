def e_palindromo(palavra):
    palavra = palavra.lower()  
    palavra_invertida = palavra[::-1] 

    return palavra == palavra_invertida


print(e_palindromo("arara"))   
print(e_palindromo("python")) 
print(e_palindromo("reconhecer"))
