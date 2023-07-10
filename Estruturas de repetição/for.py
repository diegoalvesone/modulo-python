#Exemplo 1: Impressão números 1 a 10

for numero in range(1, 11):
  print(numero)
  
# #Exemplo 2: Impressão de frutas de uma lista de frutas

frutas = ["maça", "laranja", "uva"];

for fruta in frutas:
  print(fruta);


#Exemplo 2.1
for fruta in frutas:
  if fruta == "laranja":
    continue;
  print(fruta);

#Exemplo 2.2

for fruta in frutas:
  if(fruta == "laranja"):
    print("Encontrou laranja!");
    break;
  print(fruta);
  
#Exemplo 3: Cálculo da média de uma lista de notas

notas = [7.5, 8.0, 6.5, 9.0, 7.0];    

soma = 0;

for nota in notas:
  soma += nota;

media = soma / len(notas);
print("A média é: ", media);



#Exemplo 4: Contando as vogais de uma string

palavra = "python";
vogais  = 0;

for letra in palavra:
  if letra in "aeiou":
    vogais += 1;
    
print(f"A palavra {palavra} possui {vogais} vogal");

#Exemplo 5:  Iteração sobre os itens de uma lista

lista = ["a", "b", "c", "d", "e"];

for indice in range(len(lista)):
  if indice == 0:
    lista[indice] = "z";
  print(f"O elemento no índice {indice} é {lista[indice]}");
  

#Exemplo 6: Iteração sobre um elemento número com incremento

for numero in range(2, 11, 2):
  print(numero);

#Exemplo 7: Iteração reversa sobre uma sequência
palavra = "python"
for letra in reversed(palavra):
  print(letra);
  
#Exemplo 8: Iteração sobre duas listas simultaneamente usando a função zip()

lista1 = [1,2,3];
lista2 = ["a", "b", "c"]
for elemento1, elemento2 in zip(lista1, lista2):
  print(elemento1, elemento2)
  
#Exemplo 9: Iteração com a função enumerate para acessar índice e elemento simultaneamente.

lista = ["a", "b", "c"]
for indice, elemento in enumerate(lista):
  print(f"O elemento no índice {indice} é {elemento}");
  
#Exemplo 10: Iteração sobre um dicionário para acessar chaves e valores.

dicionario = {
  "chave1": "valor1", 
  "chave2": "valor2", 
  "chave3" : "valor3"
}

for chave, valor in dicionario.items():
  print(chave, valor);