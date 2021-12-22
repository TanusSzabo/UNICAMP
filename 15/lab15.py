###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Fuga de Nova York II
# Nome: 
# RA: 
###################################################


'''
Dada uma matriz e a posição (x,y), realiza a 
verificação de é possível realizar a fuga da cidade
ou se é necessário o resgate aéreo.
'''
def fuga(matriz, x, y):
    if x<0 or x>=len(matriz) or y<0 or y>=len(matriz[0]):
        return True
    
    elif matriz[x][y].islower():
        return False
    
    else:
        corre = False
        matriz[x][y] = matriz[x][y].lower()
        if matriz[x][y] == 't':
            for xi, yi in [[1,0], [0,1], [-1,0], [0,-1]]:
                corre = corre or fuga(matriz, x+xi, y+yi)
                if corre:
                    break
        if matriz[x][y] == 'v':
            for xi, yi in [[1,0], [-1,0]]:
                corre = corre or fuga(matriz, x+xi, y+yi)
                if corre:
                    break
        if matriz[x][y] == 'h':
            for xi, yi in [[0,1], [0,-1]]:
                corre = corre or fuga(matriz, x+xi, y+yi)
                if corre:
                    break
        
        return corre
            
            
def matriz_reset(matriz):
    n = len(matriz)
    m = len(matriz[0])
    for i in range(n):
        for j in range(m):
            matriz[i][j] = matriz[i][j].upper()
        

# Leitura de dados

matriz = []    
linha = input()
while not(linha.isnumeric()):
    matriz.append(linha.split())
    linha = input()
k = int(linha)

# Verifica se é preciso realizar a fuga da cidade
# ou solicitar o resgate aéreo para cada posição

for i in range(k):
    x, y = [int(l) for l in input().split()]
    if fuga(matriz, x, y):
        print('Fuga da cidade realizada.')
    else:
        print('Resgate aereo solicitado.')
        
    matriz_reset(matriz)