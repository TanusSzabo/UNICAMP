###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Noite de Sono
# Nome:
# RA:
###################################################

# Leitura de dados

h_1 = int(input()) # hora em que João foi dormir.
m_1 = int(input()) # minuto em que João foi dormir.
h_2 = int(input()) # hora em que o alarme irá despertar.
m_2 = int(input()) # minuto em que o alarme irá despertar.
min_minimos = 60*8
min_dormidos = 60*((24+h_2-h_1)%24) + (m_2-m_1)
print(  min_dormidos >= min_minimos  )