import random

def jogar():
    abertura_do_jogo()
    tema = pede_tema()
    #seleciona o tema escolhido, não aceita número inválido
    while (tema < 1 or tema > 2):
        print("Opção inválida!")
        tema = int(input("Escolha o tema: "))
    if (tema == 1):
        print("Você escolheu Nomes de Pessoas!")
        palavra_secreta = nomes_pessoas()
    elif (tema == 2):
        print("Você escolheu Nomes de Frutas")
        palavra_secreta = nomes_frutas()
    #coloca um underline para cada letra existente na palava secreta
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        print(letras_acertadas)

        chute = pede_chute()

        if( chute in  palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    pede_jogar_novamente()


# ---------------------------------------------- Codigos Completos --------------------------------------------------

def abertura_do_jogo():
    print("----------------------------------")
    print("***Bem vindos ao jogo da forca!***")
    print("----------------------------------")

def pede_tema():
    print("(1) Nomes de Pessoas (2) Nomes de Frutas")
    tema = int(input("Escolha o tema: "))
    return tema

def nomes_pessoas():
    arquivo_pessoas = open("pessoas.txt", "r")
    palavras = []

    for linha in arquivo_pessoas:
        linha = linha.strip()
        palavras.append(linha)

    arquivo_pessoas.close()

    numero = random.randrange(0, len(palavras)) #escolha aleatória de uma palavra em um intervalo de posição
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def nomes_frutas():
    arquivo_frutas = open("frutas.txt", "r")
    palavras = []

    for linha in arquivo_frutas:
        linha = linha.strip()
        palavras.append(linha)

    arquivo_frutas.close()

    numero = random.randrange(0, len(palavras)) #escolha aleatória de uma palavra em um intervalo de posição
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()  # strip tira os espaços
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0  # index pesquisa a localização da letra na palavra (?)
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = chute  # coloca o chute ja na posição certa
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def pede_jogar_novamente():
    # PARA JOGAR NOVAMENTE
    print("SIM (1) NAO (2)")
    resposta = int(input("Deseja jogar novamente? "))
    while (resposta < 1 or resposta > 2):
        print("SIM (1) NAO (2)")
        resposta = int(input("Deseja jogar novamente? "))
    if (resposta == 1):
        jogar()
    else:
        print("Jogo encerrado!")

if(__name__ == "__main__"):
    jogar()