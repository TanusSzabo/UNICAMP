###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Avatar
# Nome: 
# RA: 
###################################################

# Inicialização das variáveis

water = 0
earth = 0
fire = 0
air = 0

# Leitura da sequência de treinamento

elemento = input()

while elemento != 'X':
    if elemento == 'W':
        treino = int(input())
        water += treino
        fire = max(fire-(treino/2) , 0)
    elif elemento == 'E':
        treino = int(input())
        earth += treino
        air = max(air-(treino/2) , 0)
    elif elemento == 'F':
        treino = int(input())
        fire += treino
        water = max(water-(treino/2) , 0)
    elif elemento == 'A':
        treino = int(input())
        air += treino
        earth = max(earth-(treino/2) , 0)

    elemento = input()


# Impressão das informações de saída

print("Pontuacao Final")
print("Agua: {:.1f}".format(water))
print("Terra: {:.1f}".format(earth))
print("Fogo: {:.1f}".format(fire))
print("Ar: {:.1f}".format(air))

if water*earth*fire*air > 0:
    print("Treinamento realizado com sucesso.")

else:
    print("Realize mais treinamentos.")