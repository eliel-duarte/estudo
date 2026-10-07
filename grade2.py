LARGURA = 10
ALTURA = 20

tabuleiro = [["." for _ in range(LARGURA)] for _ in range(ALTURA)]

# Formato da peça: posições dos blocos em relação ao canto dela
peca = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Posição da peça no tabuleiro
posicao_linha = 0
posicao_coluna = 4


def desenhar():
    print("+" + "-" * (LARGURA * 2) + "+")

    for linha in range(ALTURA):
        conteudo = tabuleiro[linha].copy()

        for linha_peca, coluna_peca in peca:
            linha_atual = posicao_linha + linha_peca
            coluna_atual = posicao_coluna + coluna_peca

            if linha == linha_atual:
                conteudo[coluna_atual] = "O"

        print("| " + " ".join(conteudo) + "|")

    print("+" + "-" * (LARGURA * 2) + "+")


while True:
    desenhar()

    comando = input("Aperte Enter para descer ou digite q para sair: ")

    if comando.lower() == "q":
        break

    # A peça tem 2 blocos de altura, por isso usamos ALTURA - 2
    if posicao_linha < ALTURA - 2:
        posicao_linha += 1
