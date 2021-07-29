import sys

def recursao(linha, coluna):
    global ovelhas_pasto, lobos_pasto

    try:
        if matriz[linha][coluna] == "#" or matriz[linha][coluna] == 1:
            return 0
        elif matriz[linha][coluna] == "k":
            ovelhas_pasto += 1
        elif matriz[linha][coluna] == "v":
            lobos_pasto += 1
    except IndexError:
        return

    matriz[linha][coluna] = 1
    recursao(linha - 1, coluna)
    recursao(linha, coluna + 1)
    recursao(linha + 1, coluna)
    recursao(linha, coluna - 1)

sys.setrecursionlimit(1000000)

ovelhas_vivas, lobos_vivos = 0, 0
linhas, colunas = map(int, input().split())
matriz = []
for linha in range(linhas):
    matriz.append(list(input()))

ovelhas_pasto, lobos_pasto = 0, 0
for linha in range(linhas):
    for coluna in range(colunas):
        if matriz[linha][coluna] != "#" or matriz[linha][coluna] != 1:
            ovelhas_pasto, lobos_pasto = 0, 0
            recursao(linha, coluna)
            if ovelhas_pasto > lobos_pasto:
                ovelhas_vivas += ovelhas_pasto
            else:
                lobos_vivos += lobos_pasto

print(ovelhas_vivas, lobos_vivos)
