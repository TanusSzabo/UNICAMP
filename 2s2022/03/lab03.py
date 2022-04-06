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

if score < 300:
    resposta = "Cartao nao concedido"

elif 300 <= score < 600:
    if idade >= 30 and salario >= 3000 and saldo >= 7000:
        resposta = "Cartao concedido"
    else:
        resposta = "Cartao nao concedido"

else:
    if idade < 50 and salario < 2000 and saldo < 5000:
        resposta = "Cartao nao concedido"
    else:
        resposta = "Cartao concedido"

print(resposta)