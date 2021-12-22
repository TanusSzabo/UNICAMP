###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Emparelhamento de Primers
# Nome: 
# RA: 
###################################################

# Leitura de dados

dna = input()[1:-1]
primer = input()[-2:0:-1].replace('G', 'c').replace('T', 'a').replace('C', 'g').replace('A', 't')

# Verificação da ligação dos primers na fita

ligacoes = []
for i in range(len(dna)-len(primer)+1):
    if dna[i:i+len(primer)] == primer.upper():
        ligacoes.append(i+1)

# Impressão da saída do programa

if ligacoes:
    for ligacao in ligacoes:
        print(f'Ligacao na posicao {ligacao}')
else:
    print('Nenhuma ligacao')