###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - O Porteiro do Castelo
# Nome: 
# RA: 
###################################################

# Leitura de dados

sequencia = [int(i) for i in input().split()]
N = len(sequencia)
n = sequencia.index(min(sequencia))
sequencia = sequencia[n:] + sequencia[:n]
verificacao = ( sequencia == sorted(sequencia) )

if verificacao:
    print('Klift, Kloft, Still, a porta se abriu')
else:
    print('Senha incorreta')