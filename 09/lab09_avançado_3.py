#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Jogos Olímpicos
# Nome: 
# RA: 
#####################################################

# Leitura da primeira linha
N, O, P, B = [int(x) for x in input().split()]

# Leitura e processamento das provas

rancking = {}
for i in range(N):
    prova, ouro, prata, bronze = input().split()
    rancking[ouro] =   [ rancking.get(ouro,   [0,[]])[0] + O, rancking.get(ouro,   [0,[]])[1] + [prova] ]
    rancking[prata] =  [ rancking.get(prata,  [0,[]])[0] + P, rancking.get(prata,  [0,[]])[1] ]
    rancking[bronze] = [ rancking.get(bronze, [0,[]])[0] + B, rancking.get(bronze, [0,[]])[1] ]

ponto_vitoria = max( [ rancking[prova][0] for prova in rancking ] )

# Impressão da saída

for pais in sorted(rancking):
    if rancking[pais][0] == ponto_vitoria:
        print(pais, rancking[pais][0])
        for prova in rancking[pais][1]:
            print(prova)