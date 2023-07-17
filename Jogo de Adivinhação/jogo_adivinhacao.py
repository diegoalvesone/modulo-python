import random

def adivinhacao():
    print("Bem-vindo ao jogo de adivinhação de números!")
    print("Vamos personalizar o jogo!")

    limite_inferior = int(input("Digite o limite inferior do intervalo de números: "))
    limite_superior = int(input("Digite o limite superior do intervalo de números: "))
    max_tentativas = int(input("Digite o número máximo de tentativas: "))

    numero_secreto = random.randint(limite_inferior, limite_superior)
    tentativas = 0

    print(f"\nOK! Estou pensando em um número entre {limite_inferior} e {limite_superior}.")
    print(f"Você tem no máximo {max_tentativas} tentativas.")

    while tentativas < max_tentativas:
        palpite = int(input("\nDigite o seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Tente um número maior!")
        elif palpite > numero_secreto:
            print("Tente um número menor!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            break

    if tentativas == max_tentativas:
        print(f"\nSuas tentativas acabaram! O número correto era {numero_secreto}.")

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        adivinhacao()
    else:
        print("\nObrigado por jogar! Até a próxima. ❤️❤️❤️")

adivinhacao()