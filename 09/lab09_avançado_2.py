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
ouros = {}
for i in range(N):
    prova, ouro, prata, bronze = input().split()
    pontos[ouro] = pontos.get(ouro, 0) + O
    pontos[prata] = pontos.get(prata, 0) + P
    pontos[bronze] = pontos.get(bronze, 0) + B

    ouros[prova] = ouro

ponto_vitoria = max( pontos.values() )

# Impressão da saída

for pais in sorted(pontos):
    if pontos[pais] == ponto_vitoria:
        print(pais, pontos[pais])
        for prova in ouros:
            if pais == ouros[prova]:
                print(prova)