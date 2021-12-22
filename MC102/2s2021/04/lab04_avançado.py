###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Avatar
# Nome: 
# RA: 
###################################################

# Inicialização das variáveis

# Elementos: agua = W, terra = E, fogo = F, ar = A
avatar = {'W':0, 'E':0, 'F':0, 'A':0}

# Leitura da sequência de treinamento
while True:
    elemento = input()
    if elemento == 'X':
        break
    treino = int(input())
    avatar[elemento] += treino
    # Letras minúsculas para não cair em um looping de replace()
    elemento_oposto = elemento.replace('W','f').replace('E','a').replace('F','w').replace('A','e')
    avatar[elemento_oposto.upper()] = max(avatar[elemento_oposto.upper()]-(treino/2) , 0)
    """ 'W'   'E'   'F'   'A'  elemento
         ↓     ↓     ↓     ↓   .replace()
        'f'   'a'   'w'   'e'  elemento oposto
         ↓     ↓     ↓     ↓   .upper()
        'F'   'W'   'W'   'A'                   """

# Impressão das informações de saída
print("Pontuacao Final")
print(f"Agua: {avatar['W']:.1f}")
print(f"Terra: {avatar['E']:.1f}")
print(f"Fogo: {avatar['F']:.1f}")
print(f"Ar: {avatar['A']:.1f}")

if min(avatar.values()) > 0:
    print("Treinamento realizado com sucesso.")

else:
    print("Realize mais treinamentos.")