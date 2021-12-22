###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Fuga de Nova York II
# Nome: 
# RA: 
###################################################


'''
Dada uma matriz e a posição (x,y), realiza a 
verificação de é possível realizar a fuga da cidade
ou se é necessário o resgate aéreo.
'''
def fuga(matriz, x, y):
#   ...


# Leitura de dados

matriz = []    
linha = input()
while not(linha.isnumeric()):
  matriz.append(linha.split())
  linha = input()
n = int(linha)

# Verifica se é preciso realizar a fuga da cidade
# ou solicitar o resgate aéreo para cada posição
#   ...

