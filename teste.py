import random # biblioteca para gerar números aleatórios

# função que simula uma partida pela winrate
def simular_partida(winrate):
    sorteio = random.randint(1, 100)
    if sorteio > winrate:
        return 0
    else:
        return 1
           
# pede a winrate
winrate = int(input("Informe a winrate: "))


# simular draft rápido
vitorias = 0;
derrotas = 0;

while vitorias < 7 and derrotas <3:
    partida = simular_partida(winrate)
    if partida == 1:
        vitorias += 1 # venceu
    else:
        derrotas += 1 # perdeu
    
    if vitorias == 7:
        print("Você venceu o draft, e perdeu ", derrotas, "partidas")
    if derrotas == 3:
        print("Você perdeu o draft, e ganhou ", vitorias, "partidas")