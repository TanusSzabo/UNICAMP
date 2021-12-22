###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Ordenação de Panquecas
# Nome: Rubens Cortelazzi Roncato
# RA: 236292
###################################################
#Pensei em dar uma lista e transformar ela em uma lista de strings
# Após isso, eu acharia o maior valor e se tiver na primeira posição da lista
# Eu inverteria e guardaria ela em uma lista separada e não eu encontria onde ela
# está e trocaria com o que está na primeira posição e Depois inverteria e guardaria em uma lista.
#assim, eu iria passando e tirsnd daquela lista e colocando na outra

lista = [int(i) for i in input().split()] #código para leitura da entrada.

# Dada uma sequência de números de inteiros, gera
# uma string representando a pilha de panquecas
def str_panquecas(lista):
   return(" ".join(map(str, lista)))

lista_ordenada = sorted(lista)
if(lista_ordenada == lista):
    print("Panquecas ja ordenadas")
maiores = []
while(len(lista) != 1):#enquanto a lista de strings tiver com mais de um elemeto
    max_value = max(lista)
    maiores.insert(0,max_value)
    if(lista.index(max_value) == 0): #a posição do maior elemento está na primeira posição 
        print("Posicionando a panqueca", max_value)  
        lista = lista[:lista.index(max_value):-1]
        print("Segunda inversao:", str_panquecas(lista) +" "+ str_panquecas(maiores[0:])) 
    elif(lista.index(max_value)) == len(lista)-1:#se estiver na última posição que está sendo analisada
        lista.remove(max_value)
    else:#não está nem na primeira e nem na ulima posição
        print("Posicionando a panqueca", max_value)
        lista = lista[lista.index(max_value)::-1] + lista[lista.index(max_value)+1::]
        print("Primeira inversao:", str_panquecas(lista) +" "+ str_panquecas(maiores[1:]))
        lista = lista[:lista.index(max_value):-1]
        print("Segunda inversao:", str_panquecas(lista) +" "+ str_panquecas(maiores[0:])) 