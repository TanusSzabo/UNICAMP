###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Fuga de Nova York
# Nome: 
# RA: 
###################################################

# Leitura da matriz

matriz = []
while True:
    entrada = input().split()
    if entrada[0].isnumeric():
        n_equipe = int(entrada[0])
        break
    else:
        matriz.append(entrada)

n, m = [ len(matriz), len(matriz[0]) ]

nova_york = [['norte']*(m+2)]        
for linha in matriz:
    nova_york.append( ['oeste'] + linha + ['leste'] )
nova_york.append(['sul']*(m+2))


# Leitura das coordenadas e início do processamento

def mudar(n, m, letra):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if nova_york[i][j] == '*':
                nova_york[i][j] = letra


for i in range(n_equipe):
    y, x = [int(k) for k in input().split()]
    x += 1
    y += 1
    while True:
        passo = nova_york[y][x]
        nova_york[y][x] = '*'
        if passo == 'N':
            y -= 1
        elif passo == 'S':
            y += 1
        elif passo == 'L':
            x += 1
        elif passo == 'O':
            x -= 1
            
        elif passo.islower():
            print(f'Fuga pelo {passo}.')
            mudar(n, m, passo)
            break
        
        else:
            print('Resgate aereo solicitado.')
            mudar(n, m, 'R')
            break