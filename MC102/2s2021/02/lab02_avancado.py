###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Fórmula 1
# Nome: 
# RA: 
###################################################

# Leitura de dados
t = float(input())              # tempo necessário para que o segundo colocado na corrida chegue até a saída dos boxes, em segundos (valor real).
dist_a = int(input())           # distância entre a entrada dos boxes e o local do pit stop, em metros (valor inteiro).
vel_a = float(input())/3.6      # velocidade média para percorrer a distância entre a entrada dos boxes e o local do pit stop, em m/s (valor real).
t_pit_stop = float(input())     # tempo gasto para realizar o pit stop, em segundos (valor real).
dist_b = int(input())           # distância entre o local do pit stop e a saída dos boxes, em metros (valor inteiro).
vel_b = float(input())/3.6      # velocidade média para percorrer a distância entre o local do pit stop e a saída dos boxes, em m/s (valor real)

# Cálculo do tempo total gasto para realizar o pit stop 
# Impressão da resposta
print(dist_a/vel_a + t_pit_stop + dist_b/vel_b  <  t)  # Tempo da parada no pit stop