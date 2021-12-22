###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Emparelhamento de Primers
# Nome: 
# RA: 
###################################################

# Leitura de dados

dna = input().lower()
primer = input()[-2:0:-1].replace('G', 'c').replace('T', 'a').replace('C', 'g').replace('A', 't')

# Verificação da ligação dos primers na fita

ligacoes = []
posicao = 0
while posicao > -1:
    posicao = dna.find(primer, posicao+1)
    if posicao > -1:
        ligacoes.append(posicao)

# Impressão da saída do programa

if ligacoes:
    for ligacao in ligacoes:
        print(f'Ligacao na posicao {ligacao}')
else:
    print('Nenhuma ligacao')