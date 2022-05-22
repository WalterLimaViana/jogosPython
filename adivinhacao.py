import random

def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de adivinhação!!")
    print("**********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    rodada = 1

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Intermediário (3) Díficil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 15
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format( rodada, total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Voce digitou", chute_str)
        chute = int(chute_str)
        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print(f'Voce acertou!!! Sua pontuação foi de {pontos} pontos.')
            break
        else:
            if(maior):
                print("Voce errou, o seu chute foi maior que o numero secreto!!!")
            elif(menor):
                print("Voce errou. O seu chute foi menor que o numero secreto!!!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            rodada = rodada + 1
    print(f'O número secreto é: {numero_secreto}')
    print("Fim de jogo")
if(__name__ == "__main__"): # essa função possibilita o arquivo adivinhacao ser executado individualmente
    jogar()