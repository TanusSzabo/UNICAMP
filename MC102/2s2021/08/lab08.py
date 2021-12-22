###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Emparelhamento de Primers
# Nome: 
# RA: 
###################################################

# Leitura de dados

dna = input()[1:-1]
primer = input()[1:-1]

# Verificação da ligação dos primers na fita

ligacoes = []
for i in range(len(dna)-len(primer)+1):

    ligacao = True
    for j in range(len(primer)):
        primer_ligante = primer[-j-1].replace('G', 'c').replace('T', 'a').replace('C', 'g').replace('A', 't')
        dna_ligante = dna[i+j].lower()
        if dna_ligante != primer_ligante:
            ligacao = False
            break

    if ligacao:
        ligacoes.append(i+1)

# Impressão da saída do programa

if len(ligacoes) > 0:
    for ligacao in ligacoes:
        print('Ligacao na posicao', ligacao)
else:
    print('Nenhuma ligacao')