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

n = len(matriz)
m = len(matriz[0])

for j in range(m):
    if matriz[4][j] == '+':
        rami_x = 0
        rami_y = 0
        while True:
            matriz[4+rami_y][j+rami_x] = '*'
            if 4+rami_y <= 0 or j+rami_x <= 0 or j+rami_x >= m-1:
                print(f'Bifurcacao {j}: Evento Nexus')
                break
            elif matriz[4+rami_y+1][j+rami_x] == '+':
                rami_y += 1
            elif matriz[4+rami_y-1][j+rami_x] == '+':
                rami_y -= 1
            elif matriz[4+rami_y][j+rami_x+1] == '+':
                rami_x += 1
            elif matriz[4+rami_y][j+rami_x-1] == '+':
                rami_x -= 1
            else:
                print(f'Bifurcacao {j}: Instavel')
                break
    
    if matriz[6][j] == '+':
        rami_x = 0
        rami_y = 0
        while True:
            matriz[6+rami_y][j+rami_x] = '*'
            if 6+rami_y >= n-1 or j+rami_x <= 0 or j+rami_x >= m-1:
                print(f'Bifurcacao {j}: Evento Nexus')
                break
            elif matriz[6+rami_y+1][j+rami_x] == '+':
                rami_y += 1
            elif matriz[6+rami_y-1][j+rami_x] == '+':
                rami_y -= 1
            elif matriz[6+rami_y][j+rami_x+1] == '+':
                rami_x += 1
            elif matriz[6+rami_y][j+rami_x-1] == '+':
                rami_x -= 1
            else:
                print(f'Bifurcacao {j}: Instavel')
                break