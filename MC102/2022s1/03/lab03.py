###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - BikeMax
# Nome:
# RA:
###################################################

# Leitura de dados

sexo = input()        # M = masculino ou F = feminino
peso = int(input())   # kg
altura = int(input()) # cm

# Seleção do modelo recomendado

if sexo == 'M':
    if altura <= 165:
        if peso <= 70:
            modelo = 'LX-39'
        elif 70 < peso <= 100:
            modelo = 'LX-40'
        else:  # peso > 100
            modelo = 'CX-102'
            
    elif 165 < altura <= 190:
        if peso <= 80:
            modelo = 'BW-02'
        elif 80 < peso <= 100:
            modelo = 'MM-107'
        else:  # peso > 100
            modelo = 'CX-102'
            
    else:  # altura > 190
        if peso <= 100:
            modelo = 'MM-107'
        else:  # peso > 100
            modelo = 'CX-102'
            
            
else:   # sexo == 'F'
    if altura <= 140:
        modelo = 'LX-38'
            
    elif 140 < altura <= 155:
        if peso <= 90:
            modelo = 'BW-03'
        else:  # peso > 90
            modelo = 'CX-101'
            
    elif 155 < altura <= 170:
        if peso <= 70:
            modelo = 'BW-03'
        else:  # peso > 70
            modelo = 'CX-101'
            
    else:  # altura > 170
        if peso <= 90:
            modelo = 'BW-02'
        else:  # peso > 90
            modelo = 'CX-102'
            
            
# Impressão da resposta

print(modelo)