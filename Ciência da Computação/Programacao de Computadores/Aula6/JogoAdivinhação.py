import random

num_secreto = random.randint(1,5)
tentativas = 0
maximo_tentativas = 3

print("----JOGO DA ADIVINHAÇÃO----")
print("Tente adivinhar o número entre 1 e 5")
print(f"Você tem {maximo_tentativas} tentativas.\n")

while tentativas < maximo_tentativas:
    try:
        jogada = int(input("Digite o número que você acha que estou pensando: "))
        tentativas = tentativas + 1

        if jogada == num_secreto:
            print("PARABÉNS VOCÊ ACERTOU NO NÚMERO")
            break
        else: 
            print("Voçê errou, tente novamente")


    except ValueError:
        print("Você digitou uma letra, tente novamente!")

print(f"O número que eu estava pensando era {num_secreto}!")