#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Linha do Tempo Sagrada
# Nome:
# RA:
#####################################################

# Leitura da matriz

matriz = []
for i in range(11):
    matriz.append(list(input()))

# Deteção dos eventos nexus

def tempo(matriz, n, m, x, y):
    matriz[y][x] = '*'
    nexus = False
    
    if not (0 < x < m-1 and 0 < y < n-1):
        nexus = True

    else:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 or j != 0) and matriz[y+i][x+j] == '+' and not nexus:
                    nexus = tempo(matriz, n, m, x+j, y+i)
        
    return nexus


n = len(matriz)
m = len(matriz[0])

for c in range(m):
    for l in [4, 6]:
        if matriz[l][c] == '+':
            if tempo(matriz, n, m, c, l):
                print(f'Bifurcacao {c}: Evento Nexus')

            else:
                print(f'Bifurcacao {c}: Instavel')