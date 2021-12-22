###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - O Porteiro do Castelo
# Nome: 
# RA: 
###################################################

# Leitura de dados

sequencia = [int(i) for i in input().split()]
sequencia_comparacao = [max(0, sequencia[i-1]-sequencia[i]) for i in range(len(sequencia))]
sequencia_comparacao.remove(max(sequencia_comparacao))

if any(sequencia_comparacao):
    print('Senha incorreta')
else:
    print('Klift, Kloft, Still, a porta se abriu')