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
    vacinas_dadas = min(vacinas_disponiveis, D1A)
    D2 += vacinas_dadas
    D2A += vacinas_dadas
    D1 -= vacinas_dadas
    D1A -= vacinas_dadas
    vacinas_disponiveis -= vacinas_dadas

    # Segunda Dose - Em Dia
    vacinas_dadas = min(vacinas_disponiveis, D1)
    D2 += vacinas_dadas
    D1 -= vacinas_dadas
    vacinas_disponiveis -= vacinas_dadas
    D1A = D1

    # Primeira Dose
    D1 += vacinas_disponiveis
    vacinas_disponiveis = 0


# Impressão da saída

print(f'Pessoas completamente imunizadas: {D2}')
print(f'Pessoas imunizadas apenas com uma dose: {D1}')
print(f'Pessoas que tomaram a segunda dose com atraso: {D2A}')
print(f'Pessoas esperando a segunda dose com atraso: {D1A}')