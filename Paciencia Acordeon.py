def possui_movimentos_possiveis(baralho):
    i = 0
    while i < len(baralho):
        movip = lista_movimentos_possiveis(baralho,i)
        if len(movip) > 0:
            return True
        i += 1
    return False

def empilha(baralho,origem,fim):
    baralho[fim] = baralho[origem]
    del baralho[origem]
    return baralho

def lista_movimentos_possiveis(baralho,posicao):
    movi = []
    movimentos = 0
    controle_naipe = extrai_naipe(baralho[posicao])
    controle_valor = extrai_valor(baralho[posicao])
    
    if posicao == 0:
        return movi
    
    #testa no anterior
    teste1 = extrai_valor(baralho[posicao - 1])
    teste1_ant = extrai_naipe(baralho[posicao - 1])
    if teste1 == controle_valor:
        movimentos += 1
        movi.append(1)
    elif teste1_ant == controle_naipe:
        movimentos += 1
        movi.append(1)

    #testa no terceiro anterior
    if posicao - 3 >= 0:
        teste2 = extrai_naipe(baralho[posicao - 3])
        teste2_terc = extrai_valor(baralho[posicao - 3])
        if teste2 == controle_naipe:
            movimentos += 1
            movi.append(3)
        elif teste2_terc == controle_valor:
            movimentos += 1
            movi.append(3)
    
    return movi

def verifica_se_jogo_acabou(resultado):
    if len(resultado) == 0:
        print("Fim do jogo!")
        a = str(input("Quer jogar novamente? (s/n) "))
        return recomeca_jogo(a)

def recomeca_jogo():
    a = str(input("Quer jogar novamente? (s/n)"))
    if a == "s":
        return True
    else:
        print("Obrigado por jogar!")
        return False

def extrai_naipe(carta):
    for i in carta:
        if i == '♦' or i == '♥' or i == '♣' or i == '♠':
            return i

def extrai_valor(carta):
    numero = carta[0:len(carta)-1]
    return numero

def cria_baralho():
    import random

    baralho = []
    i = 2 
    while i < 11 :
        baralho.append('{0}♥'.format(i))
        baralho.append('{0}♠'.format(i))
        baralho.append('{0}♦'.format(i))
        baralho.append('{0}♣'.format(i))
        i += 1
    
    letras = ['A', 'J', 'K', 'Q']    

    for i in letras:
        baralho.append('{0}♣'.format(i))
        baralho.append('{0}♦'.format(i))
        baralho.append('{0}♠'.format(i))
        baralho.append('{0}♥'.format(i))
         
    random.shuffle(baralho)
    return baralho 

def mostra_baralho(baralho):
    i = 0
    print("Status atual do baralho:")
    while i < len(baralho):
        naipe = extrai_naipe(baralho[i])
        if naipe == "♣":
            cor = 32
        elif naipe == '♦':
            cor = 33
        elif naipe == '♠':
            cor = 34
        else:  
            cor = 31
        print("\033[1;37;40m{0} -\033[1;{1};40m {2}\033[1;37;40m".format(i + 1,cor,baralho[i]))
        i += 1

def mostra_movimentos_possiveis(baralho, posicao, movimentos):
    i = 0 
    while i < len(movimentos):
        carta = posicao - movimentos[i]
        print("{0} - {1}".format(i + 1, baralho[carta]))
        i += 1

def inicia_jogo():
    print("Bem vindo ao paciencia!")
    print("")
    print("Existem apenas dois movimentos possiveis: ")
    print("1 - Empilhar uma carta sobre a carta imediatamente anterior")
    print("2 - Empilhar uma carta sobre a terceira carta anterior")
    print("")
    print("Para que um movimento possa ser realizado basta que uma das duas condicoes abaixo seja atendida: ")
    print("1 - As duas cartas possuem o mesmo valor")
    print("2 - As duas cartas possuem o mesmo naipe")
    print("")
    print("Espero que goste!")
    print("")
    a = str(input("Pressione enter para jogar!"))

    baralho = cria_baralho()
    tenta_novamente = True
    while tenta_novamente:
        fim_de_jogo = False
        while not fim_de_jogo:
            mostra_baralho(baralho)
            tcarta = str(input("Escolha uma carta entre 1 e {0}: ".format(len(baralho))))
            if len(tcarta)>0:
                try:
                    carta = int(tcarta)
                except:
                    carta = 0
                if carta >= 1 and carta <= len(baralho):
                    movimentos = lista_movimentos_possiveis(baralho,carta-1)
                    if len(movimentos) == 0:
                        print("A carta {0} nao pode ser movida. ".format(baralho[carta-1]))
                    elif len(movimentos) == 1:
                        empilha(baralho,carta-1,carta - (1 + movimentos[0]))
                    else:
                        escolheu = False
                        while not escolheu:
                            print("Essa carta pode ter dois ou mais movimentos.")
                            mostra_movimentos_possiveis(baralho, carta - 1, movimentos)
                            escolha = int(input("Escolha qual quer fazer: "))
                            if escolha >= 1 and escolha <= len(movimentos):
                                empilha(baralho, carta - 1, carta - (1 + movimentos[escolha-1]))
                                escolheu = True
                            else:
                                print("Movimento invalido. Tente novamente")                    
                else: 
                    print("Carta fora do baralho")
                fim_de_jogo = not possui_movimentos_possiveis(baralho)
    if len(baralho) == 1:
        print("Parabens! Você conseguiu!! GG!")
    else:
        print('Boa tentativa! Mais sorte na proxima!')
    tenta_novamente = recomeca_jogo()
inicia_jogo()


