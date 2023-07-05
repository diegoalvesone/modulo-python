#1
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

#2
temperatura = float(input("Informe a temperatura em Graus Celsius: "));
if(temperatura > 100):
  print("A água está fervendo!")

#3
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#4
senha = input("Digite a senha: ")

if senha == "123456":
    print("A senha está correta.")
else:
    print("A senha está incorreta.")

#5
idade = int(input("Digite a sua idade: "))

if idade >= 18 and idade <= 30:
    print("Você está na faixa etária desejada.")
else:
    print("Você não está na faixa etária desejada.")
    
#6
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > 0 or num2 > 0 or num3 > 0:
    print("Pelo menos um dos números é positivo.")
else:
    print("Nenhum dos números é positivo.")
    
#7
letra = input("Digite uma letra: ")

if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("A letra digitada é uma vogal.")
else:
    print("A letra digitada não é uma vogal.")
    
#8
num = int(input("Digite um número: "))

if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
    
#9
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 < num2 < num3:
    print("Os números estão em ordem crescente.")
else:
    print("Os números não estão em ordem crescente.")
    
#10
num = int(input("Digite um número: "))

if num % 3 == 0 and num % 5 == 0:
    print("O número é um múltiplo de 3 e 5 ao mesmo tempo.")
else:
    print("O número não é um múltiplo de 3 e 5 ao mesmo tempo.")