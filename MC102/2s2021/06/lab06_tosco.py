###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - O Porteiro do Castelo
# Nome: 
# RA: 
###################################################

# Leitura de dados

sequencia = [int(i) for i in input().split()]
sequencia_organizada = sorted(sequencia)

sequencia = sequencia + sequencia   # Junta duas listas iguais para "conectar as pontas"
sequencia = ' '.join( [str(i) for i in sequencia] )   # transforma a lista em uma string 
sequencia_organizada = ' '.join( [str(i) for i in sequencia_organizada] )  # transforma a lista organizada numa string similar
# # Se quiser ver o ridiculo, descomenta essas duas linhas
# print(sequencia)
# print(sequencia_organizada)

if sequencia_organizada in sequencia:  # Se a string organizada estiver dentro do compilado de duas da normal
    print('Klift, Kloft, Still, a porta se abriu')
else:
    print('Senha incorreta')