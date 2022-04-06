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

# Cálculo do tempo dormido
if h_1 < h_2:
    min_dormido = 60*(h_2-h_1) + (m_2-m_1)
else:
    min_dormido = 60*(h_2-(h_1-24)) + (m_2-m_1)

# Impressão da resposta

horas_minimas = 8
if min_dormido < 60*horas_minimas:
    print(False)
else:
    print(True)
