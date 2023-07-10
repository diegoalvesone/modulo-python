tupla1  = (1,2,3,4,5);
tupla2  = ("a", "b", "c");
tupla3  = (1, "Hello", True);
tupla4  = 1,2,3,4;  
print(tupla1);
print(tupla2);

print(type(tupla3));
print(type(tupla4));

#ACESSANDO ITENS INDIVIDUALMENTE EM TUPLAS
print(tupla2[1]);

#EXEMPLO DE UMA FORMA ERRADA DE ACESSAR UM ITEM DA TUPLA
# print(tupla2(2));

#CONCEITO PRINCIPAL DE TUPLAS: "IMUTÁVEL!!"
# tupla2[1] = "d";

#FATIAMENTO DE ITENS NA TUPLA
print(tupla1[1:4]);

#CONCATENANDO TUPLAS
tupla5 = 1,2,3;
tupla6 = 4,5,6;
tupla7 = tupla5 + tupla6;

print("Concatenando tuplas: ", tupla7);
  
#CRIANDO VARIAVEIS NOVAS COM OS VALORES DE UMA TUPLA

a, b, c = tupla6;
a = tupla6[0];

print();
print("Valores das variáveis: ");
print(a);
print(b);
print(c);
