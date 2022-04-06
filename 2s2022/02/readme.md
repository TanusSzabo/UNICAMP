Lab02 - Fórmula 1

A Fórmula 1 é a mais popular modalidade de automobilismo do mundo. A competição consiste de uma série de corridas (chamadas de Grand Prix) que ocorrem em diferentes países. As corridas geralmente ocorrem em circuitos dedicados exclusivamente para esse propósito. Entretanto, em alguns casos, circuitos são criados fechando vias públicas especialmente para a competição. Esse é o caso do Circuito de Mônaco, cujo o competidor que obteve mais vitórias foi Ayrton Senna.

A vitória em uma corrida de Fórmula 1 depende de vários fatores, que vão desde a configuração mecânica e aerodinâmica dos carros até o desenvolvimento de estratégias para efetuar o melhor número de paradas (pit stops). Durante as paradas, os mecânicos das equipes podem fazer pequenos ajustes no carro, realizar a troca dos pneus e até mesmo substituir algumas partes danificadas dos carros. Para realizar um pit stop o pitolo deve atentar-se para algumas regras. O pit stop deve sempre ser feito em uma área dedicada exclusivamente para isso, chamada de boxes. Além disso, o piloto deve respeitar um limite máximo de velocidade ao entrar e sair dessa área. Caso contrário, o mesmo pode ser penalizado.

Nesta atividade, você deverá desenvolver um programa para verificar se um piloto que está em primeiro colocado em uma corrida continuará com a liderança após realizar um pit stop, considerando 6 valores que seu programa receberá na entrada (um valor por linha):

    t: tempo necessário para que o segundo colocado na corrida chegue até a saída dos boxes, em segundos (valor real).
    dist_a: distância entre a entrada dos boxes e o local do pit stop, em metros (valor inteiro).
    vel_a: velocidade média para percorrer a distância entre a entrada dos boxes e o local do pit stop, em km/h (valor real).
    t_pit_stop: tempo gasto para realizar o pit stop, em segundos (valor real).
    dist_b: distância entre o local do pit stop e a saída dos boxes, em metros (valor inteiro).
    vel_b: velocidade média para percorrer a distância entre o local do pit stop e a saída dos boxes, em km/h (valor real).

Por simplicidade, assumimos que o tempo t é obtido no momento em que o piloto que está em primero lugar entra na área dos boxes. O seu programa deve imprimir True, caso o piloto continue em primeiro lugar na corrida após realizar o seu pit stop (ou seja, chegue na saída dos boxes antes do segundo colocado), ou False, caso contrário.

Exemplos de entradas e saídas esperadas pelo seu programa:

Obs pessoal: lab feito para aprender a trabalhar com variáveis booleanas (Verdadeiro e Falso)
