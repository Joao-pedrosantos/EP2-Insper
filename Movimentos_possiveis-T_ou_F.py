def possui_movimentos_possiveis(baralho):
    i = 0
    while i < len(baralho):
        movip = lista_movimentos_possiveis(baralho,i)
        if len(movip) > 0:
            return True
        i += 1
    return False

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



def extrai_naipe(carta):
    for i in carta:
        if i == '♦' or i == '♥' or i == '♣' or i == '♠':
            return i

def extrai_valor(carta):
    numero = carta[0:len(carta)-1]
    return numero