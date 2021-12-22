Lab15 - Fuga de Nova York II

O jogo que você ajudou a testar foi um grande sucesso! Como jogos que trazem novidades e causam boas repercussões entre a imprensa especializada e entre os jogadores recebem investimentos, a empresa responsável pelo jogo resolveu criar um downloadable content (DLC). Os DLCs são conteúdos adicionais dos jogos já lançados, como expansões de novas localidades e novas missões.

Para o desenvolvimento do DLC, a empresa resolveu convidar você novamente (já que você foi um dos grandes responsáveis para o enorme sucesso do jogo) para testar as novas missões do jogo. A sua função durante o teste é a mesma: construir um programa para simular o comportamento de um usuário no jogo.

O objetivo do DLC é similar a versão original do jogo: indicar para cada uma das N equipes se elas conseguiram sair da cidade de Nova York ou se precisam de resgate aéreo. Porém, os movimentos originais foram alterados por novos movimentos:

    H: a equipe pode se movimentar para a direita ou para a esquerda
    V: a equipe pode se movimentar para cima ou para baixo
    T: a equipe pode se movimentar para a direita, para a esquerda, para cima ou para baixo
    N: a equipe não pode se movimentar

A primeira entrada do programa consiste no mapa do jogo com L linhas e C colunas, com cada posição da matriz indicando o movimento possível naquela posição. Na sequência, o seu programa deverá ler o valor N de equipes, seguido por N linhas, com o valor de x (0 ≤ x < L) e y (0 ≤ y < C), indicando a posição de linha e coluna de cada uma das equipes. Ao final, para cada equipe, o seu programa deverá indicar "Fuga da cidade realizada." caso seja possível sair da cidade por terra, ou "Resgate aereo solicitado." caso não seja possível.

Exemplos de entradas e saídas esperadas para o seu programa:
