#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Linha do Tempo Sagrada II
# Nome:
# RA:
#####################################################

"""
Esta função recebe como parâmetro uma matriz, uma posição inicial 
de uma ramificação na matriz determinada pelos parâmetros linha 
e coluna. O retorno esperado para a função é um número inteiro 
indicando a quantidade de eventos nexus gerados pela ramificação.
"""
def eventos_nexus(matriz, n, m, x, y):
    matriz[y][x] = '*'
    nexus = 0
    
    if not (0 < x < m-1 and 0 < y < n-1):
        return 1

    else:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 or j != 0) and matriz[y+i][x+j] == '+':
                    nexus += eventos_nexus(matriz, n, m, x+j, y+i)
        
    return nexus

# Leitura da matriz

matriz = []
for i in range(11):
    matriz.append(list(input()))

n = len(matriz)
m = len(matriz[0])

for c in range(m):
    for l in [4, 6]:
        if matriz[l][c] == '+':
            nexus = eventos_nexus(matriz, n, m, c, l)
            print(f'Ramificacao {c}: {nexus} Eventos Nexus.')