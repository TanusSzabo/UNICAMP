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
    if ouro in pontos:
        pontos[ouro] += O
    else:
        pontos[ouro] = O

    if prata in pontos:
        pontos[prata] += P
    else:
        pontos[prata] = P

    if bronze in pontos:
        pontos[bronze] += B
    else:
        pontos[bronze] = B

    ouros[prova] = ouro

ponto_vitoria = max( pontos.values() )

# Impressão da saída

for pais in sorted(pontos):
    if pontos[pais] == ponto_vitoria:
        print(pais, pontos[pais])
        for prova in ouros:
            if pais == ouros[prova]:
                print(prova)