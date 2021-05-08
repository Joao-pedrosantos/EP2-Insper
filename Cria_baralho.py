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

