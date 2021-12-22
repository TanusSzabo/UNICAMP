###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Vacinação AstraZeneca
# Nome:
# RA:
###################################################

# Leitura dos dados

N = int(input())
vacinas = [int(input()) for i in range(N)]

# Listas dos números de vacinados com a primeira e segunda dose em cada mês e número de vacinas devolvidas em cada mês

D1 = []
D2 = []
X = []
intervalo = 3

# Processamento dos dados

for i in range(N):
    if i < intervalo:
        d2 = 0
    else:
        d2 = D1[i-intervalo]
    if i+intervalo < N:
        d1 = min(vacinas[i]-d2, vacinas[i+intervalo])
    else:
        d1 = vacinas[i] - d2
    x = vacinas[i] - d1 - d2
    D1.append(d1)
    D2.append(d2)
    X.append(x)

# Impressão do uso das vacinas mês a mês

for i in range(N):
    print(f'Mes {str(i+1)}:')
    print(f'Vacinados com a primeira dose: {D1[i]}')
    print(f'Vacinados com a segunda dose: {D2[i]}')
    print(f'Vacinas devolvidas: {X[i]}')

# Impressão do resumo final

print(f'Total:')
print(f'Vacinados apenas com a primeira dose: {sum(D1)-sum(D2)}')
print(f'Vacinados com as duas doses: {sum(D2)}')
print(f'Vacinas devolvidas: {sum(X)}')