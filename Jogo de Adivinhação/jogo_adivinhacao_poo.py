import random

class JogoAdivinhacao:
    def __init__(self, limite_inferior: int, limite_superior: int, max_tentativas: int):
        self.limite_inferior = limite_inferior
        self.limite_superior = limite_superior
        self.max_tentativas = max_tentativas
        self.numero_secreto = random.randint(limite_inferior, limite_superior)
        self.tentativas = 0

    def jogar(self):
        print("Bem-vindo ao jogo de adivinhação de números!")
        print("Vamos personalizar o jogo!")

        print(f"\nOK! Estou pensando em um número entre {self.limite_inferior} e {self.limite_superior}.")
        print(f"Você tem no máximo {self.max_tentativas} tentativas.")

        while self.tentativas < self.max_tentativas:
            palpite = int(input("\nDigite o seu palpite: "))
            self.tentativas += 1

            if palpite < self.numero_secreto:
                print("Tente um número maior!")
            elif palpite > self.numero_secreto:
                print("Tente um número menor!")
            else:
                print(f"Parabéns! Você acertou o número em {self.tentativas} tentativas!")
                break

        if self.tentativas == self.max_tentativas:
            print(f"\nSuas tentativas acabaram! O número correto era {self.numero_secreto}.")

        self.jogar_novamente()

    def jogar_novamente(self):
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() == "s":
            self.__init__(self.limite_inferior, self.limite_superior, self.max_tentativas)
            self.jogar()
        else:
            print("\nObrigado por jogar! Até a próxima.")

limite_inferior = int(input("Digite o limite inferior do intervalo de números: "))
limite_superior = int(input("Digite o limite superior do intervalo de números: "))
max_tentativas = int(input("Digite o número máximo de tentativas: "))

jogo = JogoAdivinhacao(limite_inferior, limite_superior, max_tentativas)

jogo.jogar()