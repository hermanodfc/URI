def fatias(tabuaBolos, tamanhoFatia, alvo):

    if tamanhoFatia == 0:
        return float('inf')

    fatias = 0
    for bolo in tabuaBolos:
        fatia = bolo // tamanhoFatia

        if fatia == 0:
            break

        fatias += fatia

        if fatias > alvo:
            break


    return fatias - alvo

def iniciarBuscaTamanhoFatia(tabuaBolos, faixaInicial, faixaFinal, alvo):

    if faixaFinal == faixaInicial:
        return faixaInicial

    if faixaInicial + 1 == faixaFinal:
        if fatias(tabuaBolos, faixaInicial, alvo) < 0:
            return faixaFinal
        else:
            return faixaInicial
            
    pontoMedio = (faixaInicial + faixaFinal) // 2
    posicao = fatias(tabuaBolos, pontoMedio, alvo)

    if posicao == 0:
        while(posicao == 0):
            pontoMedio += 1
            posicao = fatias(tabuaBolos, pontoMedio, alvo)
        return pontoMedio - 1

    if posicao > 0:
        return iniciarBuscaTamanhoFatia(tabuaBolos, pontoMedio, faixaFinal, alvo)
    else:
        return iniciarBuscaTamanhoFatia(tabuaBolos, faixaInicial, pontoMedio, alvo)

qtdFatiasEsperadas = int(input())
qtdBolos = int(input())

tabuaBolos = list(map(int, input().split()))
tabuaBolos.sort(reverse=True)

print(iniciarBuscaTamanhoFatia(tabuaBolos, 0, tabuaBolos[0], qtdFatiasEsperadas))
