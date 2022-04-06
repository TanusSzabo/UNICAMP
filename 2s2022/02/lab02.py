###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Fórmula 1
# Nome: 
# RA: 
###################################################

"""
  _______________________BOX________________________
  |                     t_pit                       |
  |   t_a = d_a/v_a     ↗ | ↘     t_b = d_b/v_b     |  t_total = t_a + t_pit + tb
  |→→→→→→→→→→→→→→→→→→→→↗  |  ↘→→→→→→→→→→→→→→→→→→→→→ |
  |_________________________________________________|
   _________________________________________________
  |                                                 |
  |            t (segundo colocado)                 |
  |→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→ |
  ----------------------PISTA------------------------
"""
# Leitura de dados
t = float(input())              # tempo necessário para que o segundo colocado na corrida chegue até a saída dos boxes, em segundos (valor real).
dist_a = int(input())           # distância entre a entrada dos boxes e o local do pit stop, em metros (valor inteiro).
vel_a = float(input())          # velocidade média para percorrer a distância entre a entrada dos boxes e o local do pit stop, em km/h (valor real).
t_pit_stop = float(input())     # tempo gasto para realizar o pit stop, em segundos (valor real).
dist_b = int(input())           # distância entre o local do pit stop e a saída dos boxes, em metros (valor inteiro).
vel_b = float(input())          # velocidade média para percorrer a distância entre o local do pit stop e a saída dos boxes, em km/h (valor real)
hoje_nao = False                # Variável em relação à chegada
kmh_para_ms = 1/3.6             # Conversão

# Cálculo do tempo total gasto para realizar o pit stop
t_parada = dist_a/(vel_a*kmh_para_ms) + t_pit_stop + dist_b/(vel_b*kmh_para_ms)  # Tempo da parada no pit stop

hoje_nao = t_parada < t    # Se o tempo de parada é menor que o tempo pro segundo ultrapassar

# Impressão da resposta
print(hoje_nao)