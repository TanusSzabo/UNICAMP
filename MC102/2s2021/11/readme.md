Lab11 - Fuga de Nova York

Grande parte dos filmes de ação seguem uma mesma linha para o roteiro, que geralmente é dada a partir de uma ameaça contra a vida na terra que faz com que todo o mundo colabore para combater um inimigo em comum. Uma porção desses filmes abordam um possível ataque alienígena contra a terra. Para destacar o perigo, são exibidas imagens de grandes cidades do planeta sendo devastadas. Entretanto, algumas cidades acabam recebendo mais destaque que outras e tornam-se o palco principal do combate. A cidade de Nova York, em particular, foi utilizada em diversos filmes como cenário de diversas batalhas.

Nos filmes, independente da forma de vida alienígena que ataca Nova York, algo que permanece inalterado: a reação da população perante ao ataque, geralmente ficando desnorteada e sem saber como agir. Para isso, equipes de resgates são utilizadas para ajudar na evacuação da cidade evitando com que pessoas sejam feridas por conta do combate.

Com base nessa temática, uma grande empresa de tecnologia está desenvolvendo um jogo no qual o jogador deve auxiliar as equipes de resgate a evacuar a população de Nova York. Você foi encarregado de testar o jogo e fazer um programa que simule o comportamente de um usuário. Algumas restrições foram adicionadas ao jogo, por conta da destruição na cidade muitas ruas estão obstruídas. Dessa forma, a partir dos pontos em que as equipes se encontram é possível seguir em apenas uma dada direção. O jogador recebe inicialmente um mapa, dado por uma matriz com L linhas e C colunas. Posteriormente, o jogador recebe um número N indicando o número de equipes que precisam de ajuda. Em sequida as N coordenadas, uma para cada equipe de resgate, são fornecidas através de uma linha x (0 ≤ x < L) e uma coluna y (0 ≤ y < C) da matriz. Cada posição da matriz possui apenas uma direção em que é possível seguir em frente. As direções são representadas por uma letra, sendo elas:

    N: Norte
    S: Sul
    L: Leste
    O: Oeste

O jogador deve determinar, para cada equipe de resgate, se é possivel fugir de Nova York ou um helicóptero deve ser enviado para realizar o resgate por via aérea, uma vez que não existe uma saída disponível da cidade por vias terrestres. A fuga da cidade é caracterizada quando a equipe consegue sair do mapa da cidade. Em outras palavras, isso significa que uma posição fora dos limites da matriz é alcançada. Quando a fuga for possível, a direção em que ela ocorreu deve ser indicada por meio de uma das seguintes mensagens:

    Fuga pelo norte.
    Fuga pelo sul.
    Fuga pelo leste.
    Fuga pelo oeste.

Note que as fugas pelas direções norte, sul, leste e oeste indicam respectivamente a fuga pela parte superior, inferior, direita e esquerda da matriz. Caso a fuga não seja possível, a seguinte mensagem deve ser exibida:

Resgate aereo solicitado.

Por exemplo, considere o seguinte mapa:

	O N L S
	L N O S
	N N N S
	S S O L

Assumindo que temos apenas uma equipe de resgate que está localizada na posição (2,2) da matriz, então existe uma saída da cidade pelo norte seguindo as posições (2,2), (1,2), (1,1) e (0,1). Logo, seu programa deve exibir a seguinte saída:

	Fuga pelo norte.

Exemplos de entradas e saídas esperadas pelo seu programa:

