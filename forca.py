def jogar():
    print("**********************************")
    print("***Bem vindo ao jogo da forca!!***")
    print("**********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f'A letra {letra} está na posição {index}.')
                #print("A letra {} está na posição {}.".format(letra, index))
            index = index + 1
        print("jogando...")

    print("Fim de jogo")
if(__name__ == "__main__"):
    jogar()