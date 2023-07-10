#1 - Crie duas variáveis, nome e idade, e atribua a elas seus próprios valores. Em seguida, use a formatação de strings para imprimir a seguinte mensagem: "Olá, meu nome é [nome] e eu tenho [idade] anos."
nome = "Diego";
idade = 31;

print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.");

#2- Crie uma variável chamada frase e atribua a ela uma string. Em seguida, use a função len() para imprimir o comprimento da frase.
frase = "Eu amo Python";
print("Tamanho: ",len(frase));

#3- Crie duas variáveis, nome e sobrenome, e atribua a elas seus próprios valores. Concatene as variáveis para criar uma nova variável chamada nome_completo e imprima o resultado.
nome = "Diego";
sobreNome = "Alves";
nomeCompleto = nome + ' ' + sobreNome;
print(nomeCompleto);

#4- Crie uma variável chamada frase e atribua a ela uma string. Use o método upper() para imprimir a frase em letras maiúsculas.
print(frase.upper())

#5- Crie uma variável chamada frase e atribua a ela uma string contendo uma frase completa. Use o método split() para dividir a frase em uma lista de palavras e imprima o resultado.
print(frase.split())

#6- Crie uma variável chamada frase e atribua a ela uma string. Use o método replace() para substituir uma palavra específica na frase por outra palavra de sua escolha. Imprima a frase modificada.
frase = frase.replace("amo", "adoro")
print(frase)

#7-  Crie duas váriaveis, “numero1” e “numero2” e atribua valores númerico a elas, depois crie uma váriavel resultado e armazene o resultado da soma das váriaveis “numero1” e “numero2”. Ao final imprima o resultado.
num1 = 10;
num2 = 5;
soma = num1 + num2;

print(soma);

#8- Escreva um programa que solicite ao usuário que digite dois números inteiros e exiba a multiplicação desses números
num1 = int(input("Número 1: "));
num2 = int(input("Número 2: "));
print(f"Multiplicação: {num1 * num2}")