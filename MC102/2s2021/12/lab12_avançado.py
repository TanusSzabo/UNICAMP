###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Busca em Imagens
# Nome: 
# RA: 
###################################################

def imprimir_imagem(imagem):
    print("P2")    # Imprime o tipo da imagem
    print(len(imagem[0]), len(imagem))  # imprime as dimenções da imagem
    print("255")   # Imprime o valor maximo de pixel
    for i in range(len(imagem)):  # Para toda linha da matriz
        print(" ".join(str(x) for x in imagem[i]))  # imprime a linha toda


def Flip_horizontal(imagem):
    return [linha[::-1] for linha in imagem]
            
    
def Flip_vertical(imagem):
    return imagem[::-1]


def Rotacao_90(imagem):
    linhas = len(imagem)         # quantidade de linhas na imagem
    colunas = len(imagem[0])     # quantidade de colunas na imagem

    return [ [imagem[i][j] for i in range(linhas-1, -1, -1)] for j in range(colunas) ]
    

def Contem(imagem_1, imagem_2):
    linhas_1 = len(imagem_1)          # quantidade de linhas na imagem 1
    colunas_1 = len(imagem_1[0])      # quantidade de colunas na imagem 1
    linhas_2 = len(imagem_2)          # quantidade de linhas na imagem 2
    colunas_2 = len(imagem_2[0])      # quantidade de colunas na imagem 2
    for i in range(linhas_1 - linhas_2 + 1):
        for j in range(colunas_1 - colunas_2 + 1):
            sub_imagem_1 = [ linha[j:j+colunas_2] for linha in imagem_1[i:i+linhas_2] ]
            if sub_imagem_1 == imagem_2:
                return True

    return False

# leitura da imagem A
_ = input() #P2 - linha a ser ignorada

m_A, n_A = [int(x) for x in input().split()]

_ = input() #255 - linha a ser ignorada

A = []
for i in range(n_A):
    A.append( [int(x) for x in input().split()] )

# leitura da imagem B
_ = input() #P2 - linha a ser ignorada

m_B, n_B = [int(x) for x in input().split()]

_ = input() #255 - linha a ser ignorada

B = []
for i in range(n_B):
    B.append( [int(x) for x in input().split()] )


# Impressão
print(f'Original: {Contem(A, B)}')
print(f'Flip horizontal: {Contem(A, Flip_horizontal(B))}')
print(f'Flip vertical: {Contem(A, Flip_vertical(B))}')
print(f'Rotacao 90: {Contem(A, Rotacao_90(B))}')
print(f'Rotacao 180: {Contem(A, Rotacao_90(Rotacao_90(B)))}')