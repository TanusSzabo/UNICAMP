Lab04 - Avatar

Avatar: A Lenda de Aang (em inglês "Avatar: The Last Airbender") é uma série animada de televisão. No contexto da série, o mundo está divido em quatro nações: a tribo da água, reino da terra, nação do fogo e os nômades do ar. Cada uma das nações é representada por um elemento natural do qual levam o nome. Dobradores são pessoas que possuem a habilidade de manipular o elemento de sua nação. Entretanto, apenas o Avatar possui a capacidade de dominar a manipulação dos quatro elementos. Na série, para tornar-se um(a) dobrador(a), é necessário muito treino e esforço.

Uma startup no ramo de tecnologia gostaria de desenvolver um jogo baseado na série, de forma que o Avatar deve desenvolver uma sequência de treinamentos. O objetivo consiste em aprimorar as habilidades do Avatar nos quatro elementos: água, terra, fogo e ar. Inicialmente, a pontuação em cada um dos elementos do Avatar é zero. Para tornar o jogo mais competivo, foi estabelecida uma regra que para cada pontuação P adicionada para um elemento treinado pelo Avatar, o elemento oposto terá uma redução de P/2 pontos, sendo que os seguintes pares de elementos são considerados opostos:

    Água <-> Fogo
    Terra <-> Ar

Além disso, para evitar elementos com pontuação negativa, o mínimo de pontos que um elemento pode ter é zero. Dessa forma, caso o valor da redução P/2 seja maior que a pontuação do elemento a ser reduzido, então o mesmo passará a ter uma pontuação zero.

Sabendo que você possui habilidades com programação, a startup contratou você para criar um programa que contabilize a pontuação final do Avatar para cada um dos elementos.

Como entrada, seu programa receberá um sequência de treinamentos, cada um deles identificados por uma letra, indicando o elemento treinado, e uma pontuação P (número inteiro), indicando os pontos associados ao treinamento do elemento. Sendo que as seguintes letras indicam os respectivos elementos:

    W = Água (Water)
    F = Fogo (Fire)
    E = Terra (Earth)
    A = Ar (Air)

A letra X indica que a sequência de treinando foi finalizada e seu programa deve imprimir a pontuação final do Avatar para cada um dos elementos. Como saída, seu programa deve informar a pontuação para os elementos água, terra, fogo e ar. A mensagem de saída deve seguir o seguinte padrão:

	Pontuacao Final
	Agua: XX.X
	Terra: XX.X
	Fogo: XX.X
	Ar: XX.X

Note que a pontuação de cada elemento deve ser exibida com uma casa decimal. Por fim, caso o Avatar tenha aprendido a manipular todos os elementos, ou seja, a pontuação para cada um dos elementos foi maior que zero, o seu programa deve imprimir a seguinte mensagem:

	Treinamento realizado com sucesso.

Caso contrário, a seguinte mensagem deve ser exibida:

	Realize mais treinamentos.

Exemplos de entradas e saídas esperadas pelo seu programa:

Obs. pessoal: Esse lab foi escrito para aprender a usar o while, especificamente para criar o habito de ter programas que leem entradas até um comando de saída.
