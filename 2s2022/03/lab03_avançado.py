###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cartões de Crédito
# Nome:
# RA:
###################################################


# Leitura de dados

score = float(input())
idade = float(input())
saldo = float(input())
salario = float(input())

# Verificação se o cartão de crédito será concedido ou não

resposta = "Cartao nao concedido"

if 300 <= score < 600 and idade >= 30 and salario >= 3000 and saldo >= 7000:
    resposta = "Cartao concedido"

elif score > 600 and not (idade < 50 and salario < 2000 and saldo < 5000):
    resposta = "Cartao concedido"

print(resposta)