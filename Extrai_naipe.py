def extrai_naipe(carta):
    for i in carta:
        if i == '♦' or i == '♥' or i == '♣' or i == '♠':
            return i