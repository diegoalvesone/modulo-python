"""
1 - Crie uma lista chamada "frutas" contendo as seguintes frutas:
maçã, banana, laranja, abacaxi e melancia. Em seguida, exiba a
lista completa na tela.
"""
frutas = ["maçã", "banana", "laranja", "abacaxi", "melancia"];
print(frutas);
print();

"""
2- Adicione a fruta "uva" à lista "frutas" utilizando o método
append(). Exiba a lista atualizada na tela.
"""
frutas.append("uva");
print(frutas);

"""
3- emova a fruta "banana" da lista "frutas" utilizando o método
remove(). Exiba a lista atualizada na tela.
"""
frutas.remove("banana");
print(frutas);

"""
4- Acesse o segundo elemento da lista "frutas" e armazene-o em
uma variável chamada "fruta_selecionada". Em seguida, exiba o
valor armazenado na variável.
"""
fruta_selecionada = frutas[1];
print(fruta_selecionada);

"""
5- Crie uma tupla chamada "cores" contendo as seguintes cores:
vermelho, azul, verde, amarelo e roxo. Em seguida, exiba a tupla
completa na tela
"""
cores = ("vermelho", "azul", "verde", "amarelo", "roxo");
print(cores);

"""
6- Acesse o terceiro elemento da tupla "cores" e armazene-o em
uma variável chamada "cor_selecionada". Em seguida, exiba o
valor armazenado na variável.
"""
cor_selecionada = cores[2];
print(cor_selecionada);

"""
7- Tente adicionar a cor "laranja" à tupla "cores" e observe o
resultado. Explique o motivo pelo qual ocorreu um erro fazendo
um comentário no código
"""
cores.append("laranja"); #Isso gerará um erro, pois as tuplas são imutáveis

"""
8- Crie um dicionário chamado "aluno" contendo as seguintes
informações: nome, idade e cidade. Utilize as chaves "nome",
"idade" e "cidade" para representar cada informação. Em seguida,
exiba o dicionário completo na tela.
"""
aluno = {
  'nome'  : 'Diego',
  'idade' : 31,
  'cidade': 'Poço Fundo'
}
print(aluno);
print();

"""
9- Acesse a idade do aluno no dicionário "aluno" e armazene-o em
uma variável chamada "idade_aluno". Em seguida, exiba o valor
armazenado na variável
"""
idade_aluno = aluno["idade"];
print(idade_aluno);
print();

"""
10- Adicione a informação do gênero do aluno ao dicionário
"aluno" utilizando a chave "gênero" e o valor correspondente. Exiba
o dicionário atualizado na tela
"""
aluno["genero"] = "Masculino";
print(aluno);
print();

"""
11- Remova a informação da cidade do dicionário "aluno"
utilizando o método pop() e a chave correspondente. Exiba o
dicionário atualizado na tela
"""
aluno.pop("cidade");
print(aluno);
print();