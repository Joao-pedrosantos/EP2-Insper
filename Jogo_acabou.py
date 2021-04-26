def verifica_se_jogo_acabou(resultado):
    if len(resultado) == 0:
        print("Fim do jogo!")
        a = input(str("Quer jogar novamente? (s/n) "))
        return recomeca_jogo(a)