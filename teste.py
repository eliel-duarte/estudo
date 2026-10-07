import random, os

# pede a winrate
winrate = int(input("Informe a winrate: "))

# limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# função que simula uma partida pela winrate
def simular_partida(winrate):
    sorteio = random.randint(1, 100)
    if sorteio > winrate:
        return 0
    else:
        return 1
           
# simulador de ganha 7 ou perde 3
def simula_7():
    vitorias = 0
    derrotas = 0    
    while vitorias < 7 and derrotas <3:
        partida = simular_partida(winrate)
        if partida == 1:
            vitorias += 1 # venceu
        else:
            derrotas += 1 # perdeu
        
    return vitorias 

# simulador de ganha 4 ou perde 2
def simula_4():
    vitorias = 0
    derrotas = 0    
    while vitorias < 4 and derrotas < 2:
        partida = simular_partida(winrate)
        if partida == 1:
            vitorias += 1 # venceu
        else:
            derrotas += 1 # perdeu
        
    return vitorias  

# simula 3 partidas independent
def simula_3():
    vitorias = 0
    derrotas = 0
    for i in range(3):
        partida = simular_partida(winrate)
        if partida == 1:
            vitorias += 1 # venceu
        else:
            derrotas += 1 # perdeu

    return vitorias

limpar_tela()

#### Simular Draft Rápido ####
print("#### Simular Draft Rápido ####")
caixa = 0;
quant = 10000
for i in range(quant):    
    premio = [50, 100, 200, 300, 450, 650, 850, 950] # Draft Rápido
    caixa -= 750
    x = simula_7()
    caixa += premio[x]    

media = caixa / quant
print("média: ", media)

#### Simular Draft Duplo ####
print("#### Simular Draft Duplo ####")
caixa = 0;
quant = 10000
for i in range(quant):    
    premio = [50, 150, 800, 1000, 1300] # Draft Duplo
    caixa -= 900
    x = simula_4()
    caixa += premio[x]

media = caixa / quant
print("média: ", media)

#### Simular Draft Premium ####
print("#### Simular Draft Premium ####")
caixa = 0;
quant = 10000
for i in range(quant):    
    premio = [50, 100, 250, 1000, 1400,	1600, 1800, 2200] # Draft Rápido
    caixa -= 1500
    x = simula_7()
    caixa += premio[x]

media = caixa / quant
print("média: ", media)

#### Simular Draft Tradicional ####
print("#### Simular Draft Tradicional ####")
caixa = 0;
quant = 10000
for i in range(quant):    
    premio = [100, 250, 1000, 2500] # Draft Tradicional
    caixa -= 1500
    x = simula_3()
    caixa += premio[x]

media = caixa / quant
print("média: ", media)

#### Simular Draft Contender ####
print("#### Simular Draft Contender ####")
caixa = 0;
quant = 10000
for i in range(quant):    
    premio = [0, 0, 0, 1400, 2800, 3200, 4200, 7200] # Draft Contender
    caixa -= 3000
    x = simula_7()
    caixa += premio[x]

media = caixa / quant
print("média: ", media)
