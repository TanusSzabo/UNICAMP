###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Fuga de Nova York
# Nome: 
# RA: 
###################################################

# Leitura da matriz
# DICA: o método isnumeric() pode ser útil para determinar o fim da leitura da matriz 

nova_iorque = []
while True:
    entrada = input().split()
    if entrada[0].isnumeric():
        n_equipe = int(entrada[0])
        break
    else:
        nova_iorque.append(entrada)
        

# Leitura das coordenadas e início do processamento

n = len(nova_iorque)
m = len(nova_iorque[0])

for i in range(n_equipe):
    equipe = [int(x) for x in input().split()]
    for i in range(n*m):
        if 0 <= equipe[0] < n and 0 <= equipe[1] < m:
            passo = nova_iorque[equipe[0]][equipe[1]]
            if passo == 'L':
                equipe[1] += 1
            if passo == 'N':
                equipe[0] -= 1
            if passo == 'O':
                equipe[1] -= 1
            if passo == 'S':
                equipe[0] += 1
        else:
            if equipe[1] >= m:
                print("Fuga pelo leste.")
            if equipe[0] < 0:
                print("Fuga pelo norte.")
            if equipe[1] < 0:
                print("Fuga pelo oeste.")
            if equipe[0] >= n:
                print("Fuga pelo sul.")
            break

        if i == n*m - 1:
            print("Resgate aereo solicitado.")