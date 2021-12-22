###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Busca em Imagens
# Nome: 
# RA: 
###################################################

def Flip_horizontal(imagem_original):
    imagem = []
    linhas = len(imagem_original)     # quantidade de linhas na imagem
    colunas = len(imagem_original[0]) # quantidade de colunas na imagem
    for i in range(linhas):           # para toda linha da imagem
        imagem.append( [imagem_original[i][j] for j in range(colunas-1, -1, -1)] )

    return(imagem)   # retorna a imagem
            
    
def Flip_vertical(imagem_original):
    imagem = []
    linhas = len(imagem_original)     # quantidade de linhas na imagem
    colunas = len(imagem_original[0]) # quantidade de colunas na imagem
    for i in range(linhas-1, -1, -1): # para toda linha indo de traz pra frente
        imagem.append( [imagem_original[i][j] for j in range(colunas)] )

    return(imagem)   # retorna a imagem


def Rotacao_90(imagem_original):
    imagem = []
    linhas = len(imagem_original)         # quantidade de linhas na imagem
    colunas = len(imagem_original[0])     # quantidade de colunas na imagem
    for j in range(colunas):              # para toda coluna da imagem
        imagem.append( [imagem_original[i][j] for i in range(linhas-1, -1, -1)] )

    return(imagem)   # retorna a imagem
    

def Contem(imagem_1, imagem_2):
    linhas_1 = len(imagem_1)          # quantidade de linhas na imagem 1
    colunas_1 = len(imagem_1[0])      # quantidade de colunas na imagem 1
    linhas_2 = len(imagem_2)          # quantidade de linhas na imagem 2
    colunas_2 = len(imagem_2[0])      # quantidade de colunas na imagem 2
    contem = False
    for i in range(linhas_1 - linhas_2 + 1):
        for j in range(colunas_1 - colunas_2 + 1):
            sub_imagem_1 = [ imagem_1[ii][j:j+colunas_2] for ii in range(i, i+linhas_2) ]
            contem = (sub_imagem_1 == imagem_2)
            if contem:
                return contem

    return contem


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
if Contem(A, B):
    print('Original: Contido')
else:
    print('Original: Nao contido')

if Contem(A, Flip_horizontal(B)):
    print('Flip horizontal: Contido')
else:
    print('Flip horizontal: Nao contido')

if Contem(A, Flip_vertical(B)):
    print('Flip vertical: Contido')
else:
    print('Flip vertical: Nao contido')

if Contem(A, Rotacao_90(B)):
    print('Rotacao 90: Contido')
else:
    print('Rotacao 90: Nao contido')

if Contem(A, Rotacao_90(Rotacao_90(B))):
    print('Rotacao 180: Contido')
else:
    print('Rotacao 180: Nao contido')