###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Fuga de Nova York
# Nome: 
# RA: 
###################################################

# Leitura da matriz

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
        matriz.append(entrada)
        

# Leitura das coordenadas e início do processamento

def Caminho(i, j, n, m):
    while 0 <= i < n and 0 <= j < m:
        matriz_fuga[i][j] = '#'
        passo = eval(matriz[i][j])
        i += passo[0]
        j += passo[1]
        if not (0 <= i < n):
            res = 'Fuga pelo ' + int(i/n)*'sul.' + (1-int(i/n))*'norte.'
        elif not (0 <= j < m):
            res = 'Fuga pelo ' + int(j/m)*'leste.' + (1-int(j/m))*'oeste.'
        elif matriz_fuga[i][j] == '#':
            res = 'Resgate aereo solicitado.'
            break
        
    for x in range(n):
        for y in range(m):
            if matriz_fuga[x][y] == '#':
                matriz_fuga[x][y] = res


n, m = [ len(matriz), len(matriz[0]) ]
matriz_fuga = []
for i in range(n):
    matriz_fuga.append(['*']*m)

for i in range(n):
    for j in range(m):
        if matriz_fuga[i][j] == '*':
            Caminho(i, j, n, m)

for i in range(n_equipe):
    y, x = [int(k) for k in input().split()]
    print(matriz_fuga[y][x])