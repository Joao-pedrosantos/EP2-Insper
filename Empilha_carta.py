def empilha(baralho,origem,fim):
    print("FIM: {0} - {1}".format(fim, baralho[fim]))
    baralho[fim] = baralho[origem]
    del baralho[origem]
    return cartas