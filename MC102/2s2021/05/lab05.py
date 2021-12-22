######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Vacinação CoronaVac
# Nome:
# RA:
######################################################################

# Leitura do número de meses

N = int(input())

# Processamento de cada mês

D1 = 0
D2 = 0
D1A = 0
D2A = 0

for i in range(N):
    vacinas_disponiveis = int(input())

    # Segunda Dose - Atrasados
    if D1A > 0:
        if D1A >= vacinas_disponiveis:
            vacinas_dadas = vacinas_disponiveis
        else:
            vacinas_dadas = D1A
        D2A += vacinas_dadas
        D2  += vacinas_dadas
        D1A -= vacinas_dadas
        D1  -= vacinas_dadas
        vacinas_disponiveis -= vacinas_dadas

    # Segunda Dose - Em Dia
    if D1 > 0 and vacinas_disponiveis > 0:
        if D1 >= vacinas_disponiveis:
            vacinas_dadas = vacinas_disponiveis
        else:
            vacinas_dadas = D1
        D2 += vacinas_dadas
        D1 -= vacinas_dadas
        vacinas_disponiveis -= vacinas_dadas
        if D1 > 0:
            D1A += D1

    #Primeira Dose
    if  vacinas_disponiveis > 0:
        vacinas_dadas = vacinas_disponiveis
        D1 += vacinas_dadas
        vacinas_disponiveis -= vacinas_dadas


# Impressão da saída

print('Pessoas completamente imunizadas:', D2)
print('Pessoas imunizadas apenas com uma dose:', D1)
print('Pessoas que tomaram a segunda dose com atraso:', D2A)
print('Pessoas esperando a segunda dose com atraso:', D1A)