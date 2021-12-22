Lab10 - Linha do Tempo Sagrada

Devido a suas habilidades como programador você foi chamado para trabalhar para a Autoridade de Variância Temporal (AVT). O trabalho da AVT é proteger a linha do tempo sagrada removendo ramificações que possam criar linhas do tempo paralelas. A linha do tempo sofre uma ramificação quando um evento ocorre de forma diferente do esperado, se essa ramificação tiver consequências significativas para os acontecimentos da linha do tempo ela cria uma nova linha temporal. Eventos que chegam a esse ponto são chamados de eventos nexus.

O sua primeira tarefa na AVT é criar um código para filtrar os eventos que causam bifurcação na linha do tempo sagrada e determinar quais desses eventos são eventos nexus.

A linha do tempo sagrada é representada pela linha 5 de uma matriz de tamanho 11 x 50 (com os índices começando em 0), uma sequência de caracteres # marca essa linha. Uma bifurcação na linha do tempo sagrada é representada por uma sequência de caracteres + partindo da linha 5. As bifurcações são identificadas pala coluna onde elas ocorreram e a borda da matriz indica a fronteira a partir da qual as bifurcações se tornam permanentes (eventos nexus).

Você pode assumir as seguintes características com relação à representação utilizada:

    No máximo uma bifurcação ocorre em cada coluna.
    Nenhuma bifurcação acontece na primeira ou última coluna (colunas 0 e 49, respectivamente).
    Duas linhas do tempo não se interceptam e não tem elementos adjacentes, com exceção do momento da bifurcação, quando a linha do tempo sagrada e a linha criada pela bifurcação são adjacentes.
    Uma linha do tempo não intercepta a si mesma e não tem elementos não consecutivos adjacentes.
    Toda expansão em uma linha do tempo ocorre sempre na vertical ou na horizontal.

Seu programa receberá a matriz 11 x 50 como entrada. Como saída, para cada bifurcação i, seu programa deve imprimir Bifurcacao i: seguido de Evento Nexus, quando a linha iniciada pela bifurcação se torna adjacente à borda da matriz, ou Instavel, quando a linha acabou antes de alcançar a borda da matriz.

Exemplos de entradas e saídas esperadas pelo seu programa:


Obs. pessoal: Lab usado para aprender sobre matrizes, a alteração dos valores dessa nas "ramificações" pode ser necessário para evitar o uso de muitos if elses emaranhados.
