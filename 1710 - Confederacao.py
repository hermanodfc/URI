def numeroPlanetas(listaPlanos, listaPlanetas, plano, maximoPlanetas=[0]):

    if len(listaPlanos) == plano:
        nPlanetas = len(listaPlanetas)
        if(nPlanetas > maximoPlanetas[0]):
            maximoPlanetas[0] = nPlanetas
        return nPlanetas

    if maximoPlanetas[0] >= len(listaPlanetas):
        return len(listaPlanetas)

    A, B, C, D = listaPlanos[plano]
    plano += 1

    planetasF = []
    planetasB = []

    for j in range(len(listaPlanetas)):
        X, Y, Z = listaPlanetas[j]

        if (A * X + B * Y + C * Z - D > 0):
            planetasF.append(listaPlanetas[j])
        else:
            planetasB.append(listaPlanetas[j])

    return max(numeroPlanetas(listaPlanos, planetasF, plano), numeroPlanetas(listaPlanos, planetasB, plano))

nPlanos, nPlanetas = list(map(int, input().split()))

planos = []
planetas = []

for i in range(nPlanos):
    planos.append(list(map(int,input().split())))

for i in range(nPlanetas):
    planetas.append(list(map(int,input().split())))

print(numeroPlanetas(planos, planetas, 0))
