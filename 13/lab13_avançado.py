###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Ordenação de Panquecas
# Nome: 
# RA: 
###################################################

lista = [int(x) for x in input().split()]  # Leitura da lista
n = len(lista)       # Tamanho da lista 
flag_troca = False   # Flag para ver se foi realizado uma troca

for i in range(n):
    maximo = max( lista[:n-i] )    # valor máximo na lista cortando o final já organizado
    maximo_i = lista.index(maximo) # indice desse valor maximo
    if maximo_i == n-(i+1):        # Se o indice já for a posição de interesse
        continue                   # Passa pra próxima iteração

    flag_troca = True  # Se uma das vezes não passar pelo if anterior, significa que vai ter troca
    print(f'Posicionando a panqueca {maximo}')
    if maximo_i > 0:   # Se o máximo já tiver na posição 0, só faz a primeira troca
        # Inversão do começo da lista indo até o máximo + manter o final da lista depois do máximo
        # print(lista[maximo_i::-1], lista[maximo_i+1:])  # Se quiser ver os pedaços da lista
        lista = lista[maximo_i::-1] + lista[maximo_i+1:]
        lista_str = ' '.join(map(str, lista))
        print(f'Primeira inversao: {lista_str}')
    
    # Inversão do começo da lista indo até o n-i-1-tésimo item da lista + manter o final da lista depois do n-i-1-tésimo item
    # print(lista[-(i+1)::-1], lista[n-i:], lista[-(i+1)::-1] + lista[n-i:]) # Se quiser ver os pedaços da lista
    lista = lista[n-i-1::-1] + lista[n-i:]
    lista_str = ' '.join(map(str, lista))
    print(f'Segunda inversao: {lista_str}')

if not flag_troca:  # Se o flag_troca nunca virou True, então todos os máximos tavam na posição certa
    print('Panquecas ja ordenadas')