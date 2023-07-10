"""
1-Escreva um programa que solicite ao usuário dois números
inteiros e exiba a soma, subtração, multiplicação e divisão entre
esses números.
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

"""
2-Escreva um programa que solicite ao usuário uma temperatura
em graus Celsius e verifique se ela está acima do ponto de
ebulição da água (100°C). Caso positivo, exiba a mensagem "A
água está fervendo!".
"""
temperatura = float(input("Informe a temperatura em Graus Celsius: "));
if(temperatura > 100):
  print("A água está fervendo!")

"""
3-Escreva um programa que solicite ao usuário um número
inteiro e verifique se ele é par ou ímpar.
"""
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

"""
4-Escreva um programa que solicite uma senha ao usuário e
verifique se a senha está correta. Considere a senha correta como
"123456"
"""
senha = input("Digite a senha: ")

if senha == "123456":
    print("A senha está correta.")
else:
    print("A senha está incorreta.")

"""
5- Escreva um programa que solicite ao usuário uma idade e
verifique se ela está entre 18 e 30 anos (inclusive).
"""
idade = int(input("Digite a sua idade: "))

if idade >= 18 and idade <= 30:
    print("Você está na faixa etária desejada.")
else:
    print("Você não está na faixa etária desejada.")
    
"""
6- Escreva um programa que solicite ao usuário três números
inteiros e verifique se pelo menos um deles é positivo.
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > 0 or num2 > 0 or num3 > 0:
    print("Pelo menos um dos números é positivo.")
else:
    print("Nenhum dos números é positivo.")
    
"""
7- Escreva um programa que solicite ao usuário uma letra e
verifique se ela é uma vogal (a, e, i, o, u)
"""
letra = input("Digite uma letra: ")

if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("A letra digitada é uma vogal.")
else:
    print("A letra digitada não é uma vogal.")
    
"""
8- Escreva um programa que solicite ao usuário um número
inteiro e verifique se ele é positivo, negativo ou zero
"""
num = int(input("Digite um número: "))

if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
    
"""
9- Escreva um programa que solicite ao usuário três números e
verifique se eles estão em ordem crescente.
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 < num2 < num3:
    print("Os números estão em ordem crescente.")
else:
    print("Os números não estão em ordem crescente.")
    
"""
10- Escreva um programa que solicite ao usuário um número
inteiro e verifique se ele é um múltiplo de 3 e 5 ao mesmo tempo.
"""
num = int(input("Digite um número: "))

if num % 3 == 0 and num % 5 == 0:
    print("O número é um múltiplo de 3 e 5 ao mesmo tempo.")
else:
    print("O número não é um múltiplo de 3 e 5 ao mesmo tempo.")