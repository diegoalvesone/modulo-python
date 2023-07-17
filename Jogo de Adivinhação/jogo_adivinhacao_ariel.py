import random

#Sorteia um número inteiro entre 1 e 10
numeroSecreto = random.randint(1,10);

print("VAMOS JOGAR!\n\nEscolha a dificuldade:");
print("(1 - Fácil) (2 - Normal) (3 - Difícil)");
dificuldade = int(input("=> "));#Escolher a dificuldade digitando 1, 2 ou 3

#Validação:
#Para corrigir a escolha da dificuldade se o usuário não colocar um número de 1 até 3
while not (dificuldade >= 1 and dificuldade <= 3) :
  dificuldade = int(input("\nOpção inválida.\n =>Escolha a dificuldade: "));

#Configura a quantidade de vidas, dependendo da dificuldade
if dificuldade == 1:
  vidas = 5; #facil
  pontos = 10; #Quantos pontos ganha na dificuldade fácil
  tirarPontos = 2; #quantos pontos tira se errar
if dificuldade == 2 :
  vidas = 3; #normal
  pontos = 30;
  tirarPontos = 10;
if dificuldade == 3 :
  vidas = 1; #dificil;
  pontos = 50;
  tirarPontos = 50;


#Mostrar coraçõezinhos x quantidade a de vidas
coracoes = "❤" * vidas;

print("\n--------\nCOMEÇOU!")
print(coracoes + "\n");
palpite = int(input("Digite um número de 1 a 10 => "));


while palpite != numeroSecreto:

  vidas -= 1; #tira uma vida
  coracoes = coracoes[1:] + "🛇";
  #tira um coração do início e adiciona um novo X em cada erro
  pontos -= tirarPontos; #tira pontos a cada erro;



  if palpite != numeroSecreto:
    print("Você errou!");
    print(coracoes + "\n");
    if vidas == 0: #Se acabarem as vidas, acaba o jogo
      print("\n❌ GAME OVER ❌");
      print("A resposta era " + str(numeroSecreto) + ".");
      #srt() transforma int em string para concatenar
      break;
    if palpite > numeroSecreto :
      palpite = int(input("-----------\n=> Digite um número MENOR: "));
    elif  palpite < numeroSecreto :
      palpite = int(input("-----------\n=> Digite um número MAIOR: "));
    else:
      break; #Se o palpite está certo, parou a repetição

if palpite == numeroSecreto :
  print("\n⭐ PARABÉNS! ⭐\nVocê acertou!");
  print("Pontuação: " + str(pontos))

print("\n=====================\nObrigado por jogar!")