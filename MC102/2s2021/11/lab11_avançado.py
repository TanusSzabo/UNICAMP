###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Fuga de Nova York
# Nome: 
# RA: 
###################################################

# Leitura da matriz
# DICA: o método isnumeric() pode ser útil para determinar o fim da leitura da matriz 

L = [ 0, 1]
N = [-1, 0]
O = [ 0,-1]
S = [ 1, 0]

matriz = []
while True:
    entrada = input().split()
    if entrada[0].isnumeric():
        n_equipe = int(entrada[0])
        break
    else:
        matriz.append([eval(k) for k in entrada])
        

# Leitura das coordenadas e início do processamento

n = len(matriz)
m = len(matriz[0])

for i in range(n_equipe):
    y, x = [int(k) for k in input().split()]
    caminho = []
    while 0 <= y < n and 0 <= x < m:
        passo = matriz[y][x]
        x += passo[1]
        y += passo[0]
        if x >= m:
            print("Fuga pelo leste.")
        if y < 0:
            print("Fuga pelo norte.")
        if x < 0:
            print("Fuga pelo oeste.")
        if y >= n:
            print("Fuga pelo sul.")
        if [x, y] in caminho:
            print("Resgate aereo solicitado.")
            break
        caminho.append([x, y])