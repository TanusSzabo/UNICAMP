Lab14 - Linha do Tempo Sagrada II

Devido ao seu bom trabalho na última tarefa (Lab 10) que foi designada na Autoridade de Variância Temporal (AVT), você recebeu uma promoção. Junto com essa promoção você também foi transferido para um novo setor. Nesse setor são investigados casos mais graves em que podem ocorrer ramificações fora da linha do tempo sagrada.

Sua nova tarefa é criar um programa para determinar quantos Eventos Nexus são gerados a partir de uma ramificação na linha do tempo sagrada.

Semelhante ao Lab 10, a linha do tempo sagrada é representada pela linha 5 de uma matriz de tamanho 11 x 50 (com os índices começando em 0), uma sequência de caracteres # marca essa linha. Uma ramificação é representada por uma sequência de caracteres + partindo da linha 5.

Apenas para relembrar alguns pontos importantes da sua última tarefa que serão úteis nessa nova: as ramificações são identificadas pela coluna onde elas ocorreram. Além disso, as bordas da matriz indicam as fronteiras a partir da qual as ramificações se tornam permanentes e são chamadas de Evento Nexus.

Você pode assumir as seguintes características para o problema:

    A partir da linha do tempo sagrada (linha 5) ocorrem apenas bifurcações para o norte ou sul.
    Nenhuma ramificação acontece na primeira ou última coluna.
    Nenhuma ramificação acontece na primeira ou última linha.
    As ramificações, com exceção das geradas a partir da linha do tempo sagrada, podem ocorrer em todas as direções (norte, sul, leste, oeste, nordeste, noroeste, sudeste e sudoeste).
    Os diferentes ramos gerados a partir de uma linha do tempo nunca se encontram depois da ramificação.

Como entrada, seu programa receberá uma matriz com dimensões 11 x 50. Como saída, para cada ramificação i (onde i indica a coluna) criada a partir da linha do tempo sagrada, seu programa deve imprimir a quantidade X de Eventos Nexus gerados a partir desse ponto. As ramificações devem ser consideradas da esquerda para a direita e o seguinte formato deve ser utilizado:

	Ramificacao i: X Eventos Nexus.

Exemplos de entradas e saídas esperadas pelo seu programa:


