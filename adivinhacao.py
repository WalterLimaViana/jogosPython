print("**********************************")
print("Bem vindo ao jogo de adivinhação!!")
print("**********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

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
        print("Voce acertou!!!")
        break
    else:
        if(maior):
            print("Voce errou, o seu chute foi maior que o numero secreto!!!")
        elif(menor):
            print("Voce errou. O seu chute foi menor que o numero secreto!!!")
    rodada = rodada + 1
print("Fim de jogo")
