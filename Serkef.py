
from random import randint  # RANDON PARA RANDOMIZAR OS OBJETOS NO MAPA


def main ():
    while True:
        print('''             ============================================================
                       BEM-VINDO AO JOGO MINAS DO REI SALOMÃO'                             
             - O jogo e composto de 3 Cânius, 3 Elefantes, e 1 Diamante                   
             - Você vence se encontrar o Diamante 
                                                      
                                  --BOM JOGO--                                              
             =======================================================''')

        op = "0"
        op = str(input("1 - jogar\n2 - sair\n---> "))  # INFORMA AS OPÇÕES

        if op=="1":
            novo_jogo()  # INICIA O JOGO
        if op=="2":
            break


def novo_jogo ():
    # OBJETOS PRO MAPA
    objectsmap = ("C" , "C" , "C" , "D" , "E" , "E" , "E")

    # PREENCHIMENTO DAS STRINGS NO MAPA
    vetorvazio = []
    for j in range(25):
        vetorvazio.append(str(" "))

    # COLOCANDO OS OBJETOS NO MAPA E RANDOMIZANDO
    for elemento in objectsmap:
        vetorvazio[randint(0 , 19)] = elemento

    # CONSTRUÇÃO DO MAPA EM FORMATO DE MATRIZ
    mapmatriz = []
    for i in range(0 , 24 , 5):
        matrizline = []
        for j in range(5):
            matrizline.append(vetorvazio[i + j])
        mapmatriz.append(matrizline)

        # i= seria as colunas
        # j= seria as linhas

    inicio_partida(mapmatriz)  # INICIO DO JOGO


def inicio_partida (mapmatriz):
    # POSIÇÃO INICIAL DO JOGADOR

    posicao = [4 , 0]  # COLUNA 1 LINHA 4

    while True:

        jogador = verifica_cenario(posicao , mapmatriz)  # VERIFICA A POSIÇÃO NA MATRIZ
        if jogador == "0":  # ELE GIRA E TODA VEZ ELE PARA NO BREAK PARA EXIBIR O PRINT E AGUARDA O PROXIMO COMANDO
            break
        print(jogador)  # RETORNO DA POSIÇÃO

        # CHAMADA DO VETOR PRO WHILE

        novamatriz = (mapmatriz)  # ATRIBUIÇÃO DO VETOR
        novamatriz[posicao[0]][posicao[1]] = '0'  # POSIÇÃO EM QUE PARTE O JOGADOR
        for i in range(5):
            print("[" , end=" ")
            for j in range(5):
                if novamatriz[i][j]!="0" and novamatriz[i][j]!=" ":
                    print("  ," , end=" ")
                else:
                    print(novamatriz[i][j] , "," , end=" ")
            print("]" , end=" ")
            print("")
            print()

        # COMANDO DE MOVIMENTOS

        mov = str(input(" w = cima | a = esquerda | s = baixo | d = direita \n Insira o proxima jogada : "))

        if mov=="w" and posicao[0]!=0:  # POSIÇÃO INICIAL [LINHA=0,COLUNA=4] SENDO DIFERENTE DE "0" , ADICIONA -1 A LINHA
            posicao[0] -= 1
        if mov=="s" and posicao[0]!=4:  # SE BASEIA NO LIMITE DA MATRIZ [LINHA=4,COLUNA=0], ADICIONA +1 A LINHA
            posicao[0] += 1
        if mov=="a" and posicao[1]!=0:  # SE BASEIA NA LINHA 1 SENDO DIFERENTE DE '0' , ADICIONA -1 A COLUNA
            posicao[1] -= 1
        if mov=="d" and posicao[1]!=4:  # SE BASEIA NA LINHA 1 E NA COLUNA 4 , SENDO DIFERENTE ADICIONA +1 A COLUNA
            posicao[1] += 1


def verifica_cenario (posicao , mapmatriz):
    x = int(posicao[0])  # POSIÇÕES DE COMPARAÇÃO
    y = int(posicao[1])  # POSIÇÕES DE COMPARAÇÃO

    # x = LINHAS(Direita e Esquerda)
    # Y = COLUNAS(Emcima e Embaixo)

    # VERIFICADOR DE POSIÇÕES

    if mapmatriz[x][y]=="C":  # >VERIFICA O VETOR E IGUALA A STRING
        print('==========================================================')
        print('Você Perdeu, Caiu em um Câniun')  # >PRINT
        print("\n1 - voltar ao início\n2 - novo jogo\n---> ")  # -->OPÇÃO PRO USUARIO
        op = str(input(""))  # >FORÇA STRING E AGUARDA A DECISÃO
        if op=="1":
            inicio_partida(mapmatriz)  # >VOLTA PARA INICIO DO JOGO "RESTART"
        if op=="2":
            novo_jogo()  # >INICIA UM NOVO JOGO

    elif mapmatriz[x][y]=="E":  # >VERIFICA O VETOR E IGUALA A STRING
        print('==========================================================')
        print('Você Perdeu, Foi pisado por um elefante')  # >PRINT
        print("\n1 - voltar ao início\n2 - novo jogo\n---> ")  # PRINT DAS OPÇÕES
        op = str(input(""))  # >FORÇA STRING E AGUARDA A DECISÃO
        if op=="1":
            inicio_partida(mapmatriz)  # VOLTA A POSIÇÃO INICIAL "RESTART"
        if op=="2":
            novo_jogo()  # INICIA UM NOVO JOGO

    ##AQUI O JOGADOR VENCE
    if mapmatriz[x][y]=="D":  # IGUALA A POSIÇÃO NO MAPA COM A STRING
        print('===========================================================')  # PRINT DE ESPAÇO
        print("Você encontrou o Diamante , Parabéns !! \n Novo Jogo = 1 \n Sair= 2")  # OPÇÕES PRO USUÁRIO
        ganhou = str(input(""))  # FORÇA STRING E AGUARDA DECISÃO
        if ganhou=="1":
            novo_jogo()  # INICIA UM NOVO JOGO
        if ganhou=="2":
            quit()  # FINALIZA

    ## POSIÇÕES ADJACENTES
    # ACIMA
    if x - 1 > 0 and mapmatriz[x - 1][y]!=' ': #Se linha -1>0 e linha + 1 != ('')
        if mapmatriz[x - 1][y]=="E": #Iguala a string e retona a print
            print('========================================================')
            return " Está fedendo, Cuidado você está proximo do bixo grande"
        if mapmatriz[x - 1][y]=="C":# Iguala a string e retorna a print
            print('=======================================')
            return "Cuidado você está proximo de um câniun"
    # DIREITA
    if y + 1 < 4 and mapmatriz[x][y + 1]!=" ":# Se coluna 1 < 4 e linha + coluna +1 != ('')
        if mapmatriz[x][y + 1]=="E": #Iguala e retona a string
            print('=====================================================') #Print Vazia
            return "Está fedendo, Cuidado você está proximo do bixo grande"
        if mapmatriz[x][y + 1]=="C": #Iguala a string e retona a string
            print('=======================================')
            return "Cuidado você está proximo de um câniun"
    # ABAIXO
    if x + 1 < 4 and mapmatriz[x + 1][y]!=" ": # Se na linha de 1 a 4 , e, 1 e 4 + Y FOR != ('')
        if mapmatriz[x + 1][y]=="E": # Iguala a string e retona Elefante
            print('======================================================') #Print Vazia
            return "Está fedendo, Cuidado você está proximo do bixo grande"
        if mapmatriz[x + 1][y]=="C": #Iguala a string e retorna a print do elefante
            print('======================================') #Print Vazia
            return "Cuidado você está proximo de um câniun"
    # ESQUERDA
    if y - 1 > 0 and mapmatriz[x][y - 1]!=" ": #Se -1 < 0 e linhas + colunas -1 for != ('')
        if mapmatriz[x][y - 1]=="E": #iguala a string e retorna a print
            print('=======================================================') #Print Vazia
            return "Está fedendo, Cuidado você está proximo do bixo grande"
        if mapmatriz[x][y - 1]=="C": #Iguala a string e retorna a print
            print('======================================') #print Vazia
            return "Cuidado você está proximo de um câniun"
    else:
        print('===============================')
        print('O caminho está livre continue')
        print('===============================')


if __name__=="__main__":
    main()
