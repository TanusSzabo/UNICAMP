###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - O Porteiro do Castelo
# Nome: 
# RA: 
###################################################

# Leitura de dados

sequencia = [int(i) for i in input().split()]
N = len(sequencia)

for n in range(N):
    verificacao = True
    vetor = sequencia[n:N] + sequencia[0:n]
    """
    sequencia = [1°, 2°, 3°, ..., N-1°]  
    vetor = [n°, n+1°, ..., N-1°]  +  [1°, 2°, ..., n-1°] =  [n°, n+1°, ..., N-1°, 1°, 2°, ..., n-1°]
    """

    for i in range(1, N):
        if vetor[i] <= vetor[i-1]:
            verificacao = False
            break

    if verificacao == True:
        break

if verificacao == True:
    print('Klift, Kloft, Still, a porta se abriu')
else:
    print('Senha incorreta')