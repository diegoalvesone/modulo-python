#Exemplos de declaração de listas
listaNumeros = [1,2,3,4,5];
listaStrings = ["e", "f", "c", "d"];
listaMista   = [1, "a", 3.14, True];
print(listaNumeros);
print(listaStrings);
print(listaMista);

frutas = ["maça", "banana", "morango"];

#ACESSANDO A LISTA POR INDICES
print(frutas[0])

#ALTERANDO UM ITEM ESPECIFÍCO DA LISTA
frutas[1] = "laranja";

#IMPRIMINDO O TAMANHO DA LISTA
print("Tamanho 1: ", len(frutas))

#ADICIONANDO UM ITEM AO FINAL DA LISTA
frutas.append("Abacaxi");
print(frutas)

#IMPRIMINDO O TAMANHO DA LISTA
print("Tamanho 2: ",len(frutas))

#ACESSANDO SUBLISTAS
listaNova = [1, ["a", "b"]];
print(listaNova[1][0]);


#CONCATENANDO LISTAS
lista1 = [1,2,3];
lista2 = [4,5,6];

listaConcatenada = lista1 + lista2;
print(listaConcatenada);

#DECLARANDO UM VALOR REPETIDO NAS LISTAS
listaRepetida = [0] * 4;
print(listaRepetida);


#FATIAMENTO DE LISTAS
letras  = ["a", "b", "c", "d"];
sublista = letras[1:4];
print(sublista);

#ADICIONANDO UM ITEM AO FINAL DA LISTA
frutas = ["maça", "banana", "laranja"];
frutas.append("morango");
print(frutas);

#INSERINDO UM ITEM EM UM INDÍCE ESPECÍFICO DA LISTA
frutas.insert(1, "abacaxi");
print(frutas);
print();

#REMOVENDO UM ITEM DA LISTA COM O METODO REMOVE
frutaRemovida = frutas.remove("banana");

#REMOVENDO UM ITEM DA LISTA COM O METODO POP
frutaRemovida = frutas.pop(2);
print(frutas);
print(frutaRemovida);

#ORDENANDO UMA LISTA
frutas.sort();
print("Ordenando: ", frutas);


#EMBARALHANDO UMA LISTA
from random import shuffle

shuffle(frutas);
print(frutas);




