def empilha(baralho,origem,fim):
    cartas = baralho
    cartas[fim] = baralho[origem]
    del cartas[origem]
    return cartas