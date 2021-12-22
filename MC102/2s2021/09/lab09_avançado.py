#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Jogos Olímpicos
# Nome: 
# RA: 
#####################################################

# Leitura da primeira linha
N, O, P, B = [int(x) for x in input().split()]

# Leitura e processamento das provas

pontos = {}
rancking = {}
for i in range(N):
    prova, ouro, prata, bronze = input().split()
    rancking[prova] = [ouro, prata, bronze]
    pontos[ouro] = 0
    pontos[prata] = 0
    pontos[bronze] = 0

for prova in rancking:
    ouro, prata, bronze = rancking[prova]
    pontos[ouro] += O
    pontos[prata] += P
    pontos[bronze] += B

ponto_vitoria = max( pontos.values() )

# Impressão da saída

for pais in sorted(pontos):
    if pontos[pais] == ponto_vitoria:
        print(pais, pontos[pais])
        for prova in rancking:
            if pais == rancking[prova][0]:
                print(prova)