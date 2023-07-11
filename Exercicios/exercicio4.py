"""
Exercício 1:
Utilizando um loop "while", imprima os números de 1 a 10.
"""
numero = 1
while numero <= 10:
    print(numero)
    numero += 1
"""
Exercício 2:
Utilizando um loop "for", imprima os números de 1 a 10.
"""
for numero in range(1, 11):
    print(numero)
"""
Exercício 3:
Utilizando um loop "while", calcule a soma dos números de 1 a 100.
"""
numero = 1
soma = 0
while numero <= 100:
    soma += numero
    numero += 1
print("A soma é:", soma)

"""
Exercício 4:
Utilizando um loop "for", calcule a soma dos números de 1 a 100.
"""
soma = 0
for numero in range(1, 101):
    soma += numero
print("A soma é:", soma)

"""
Exercício 5:
Utilizando um loop "while", imprima os números pares de 1 a 20.
"""
numero = 1
while numero <= 20:
    if numero % 2 == 0:
        print(numero)
    numero += 1

"""
Exercício 6:
Utilizando um loop "for", imprima os números pares de 1 a 20.
"""
for numero in range(2, 21, 2):
    print(numero)

"""
Exercício 7:
Utilizando um loop "while", inverta uma string digitada pelo usuário.
"""
string = input("Digite uma string: ")
indice = len(string) - 1
string_invertida = ""
while indice >= 0:
    string_invertida += string[indice]
    indice -= 1
print("A string invertida é:", string_invertida)

"""
Exercício 8:
Utilizando um loop "for", verifique se uma palavra digitada pelo usuário é um palíndromo (lê-se da mesma forma de trás para frente).
"""
palavra = input("Digite uma palavra: ")
palavra_invertida = ""
for letra in palavra:
    palavra_invertida = letra + palavra_invertida
if palavra == palavra_invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")

"""
Exercício 9:
Utilizando um loop "while", encontre o menor número inteiro cujo quadrado seja maior do que 1000.
"""
numero = 1
while numero ** 2 <= 1000:
    numero += 1
print("O menor número inteiro cujo quadrado é maior que 1000 é:", numero)

"""
Exercício 10:
Utilizando um loop "for", imprima os elementos de uma lista em ordem inversa.
"""
lista = [1, 2, 3, 4, 5]
for indice in range(len(lista)-1, -1, -1):
    print(lista[indice])
