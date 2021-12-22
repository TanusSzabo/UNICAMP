Lab08 - O Sentido da Vida

Uma fita de DNA, ou cadeia de polinucleotídeos, é representada por uma extremidade inicial (chamada de extremidade 5'), uma sequência de caracteres que representam os nucleotídeos que formam a estrutura dessa cadeia, e a extremidade final (chamada de extremidade 3'). As letras possíveis são A, G, C, e T, que representam, respectivamente, as bases Adenina, Guanina, Citosina, e Timina. Computacionalmente, podemos representar uma fita com n nucleotídeos como uma string de n+2 posições (os caracteres 5 e 3 são usados para representar as extremidades iniciais e finais, respectivamete).

Em genética, um primer é uma sequência curta de nucleotídeos que é fundamental para o início da replicação de DNA. Assim como uma fita de DNA, um primer também é representado por uma extremidade inicial (5'), uma série de letras, e uma extremidade final (3').

Um primer se liga à fita de DNA por emparelhamento de bases complementares, sempre na direção oposta a da fita. As bases emparelham-se com as respectivas bases complementares: Adenina (A) com Timina (T), Citosina (C) com Guanina (G). Sequências de DNA (assim como os primers) devem ser sempre lidos no sentido 5' -> 3', também chamado de "o sentido da vida". Para verificar onde uma primer se liga numa fita de DNA, é necessário considerar a ordem reversa do primer, já que ambas as sequências são lidas no "sentido da vida". Ou seja, se o DNA for lido da esquerda para a direita, então o primer deverá ser lido da direita para esquerda.

Neste laboratório, dados uma fita de DNA e um primer, o seu programa deve indicar em quais posições o primer se liga a fita de DNA ou se não existem tais posições. Neste caso, a posição deve levar em conta apenas a sequência de nucleotídeos (ignorando os caracteres que representam as extremidades) e considerando a posição inicial do primer, assumindo que a primeira base do DNA é a posição 1.

Como exemplo, dada a fita 5ATAGTCTAGGATAGTCT3, o primer 5GAC3 se liga nas posições 4 e 14 (considerando a primeira base do primer).

	IMAGEM: dna_primer.jpg

Exemplos de entradas e saídas esperadas pelo seu programa:


Obs. pessoal: Lab usado para aprender a manipular e comparar strings
