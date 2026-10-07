LARGURA = 10
ALTURA = 20

# Cada posição da lista representa uma linha do tabuleiro.
# Cada linha tem LARGURA posições, inicialmente vazias (0).
tabuleiro = [
    [0 for _ in range(LARGURA)]
    for _ in range(ALTURA)
]


def desenhar_tabuleiro(tabuleiro):
    print("+" + "--" * LARGURA + "+")

    for linha in tabuleiro:
        conteudo = ""

        for celula in linha:
            if celula == 0:
                conteudo += " ."
            else:
                conteudo += "[]"

        print("|" + conteudo + "|")

    print("+" + "--" * LARGURA + "+")


desenhar_tabuleiro(tabuleiro)
