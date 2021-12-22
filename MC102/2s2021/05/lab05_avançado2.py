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
    vacinas = int(input())
    D2A += min(vacinas, D1A)
    D2  += min(vacinas, D1)
    D1A = D1  - min(vacinas, D1)
    D1  = D1A - min(vacinas, D1) + vacinas 

# Impressão da saída

print(f'Pessoas completamente imunizadas: {D2}')
print(f'Pessoas imunizadas apenas com uma dose: {D1}')
print(f'Pessoas que tomaram a segunda dose com atraso: {D2A}')
print(f'Pessoas esperando a segunda dose com atraso: {D1A}')