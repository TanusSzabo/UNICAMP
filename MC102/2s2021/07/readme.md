Lab07 - Vacinação AstraZeneca

Como a sua ajuda foi fundamental para distribuir as doses da CoronaVac, a prefeitura de Campinas pediu para você ajudar também na distribuição da vacina AstraZeneca.

A vacina da AstraZeneca é aplicada em duas doses com três meses de intervalo entre a aplicação da primeira e da segunda dose. Nos próximos meses a cidade vai receber um número limitado de doses, portanto um protocolo foi desenvolvido para garantir que todos que receberam a primeira dose irão receber a segunda dose, três meses depois. Em cada um desses meses, o seu programa deve determinar quantas pessoas receberão a primeira dose e quantas pessoas receberão a segunda dose da vacina. O protocolo é composto pelas seguintes regras:

    Primeiro, se existem pessoas que receberam a primeira dose há três meses elas são vacinadas com a segunda dose.
    Em seguida, são vacinadas pessoas com a primeira dose, apenas se for possível vaciná-las com a segunda dose três meses depois. Nos últimos três meses todas as vacinas restantes podem ser aplicadas como primeira dose.
    As vacinas que não forem aplicadas num mês devem ser devolvidas. Logo, essas vacinas não podem ser usadas nos próximos meses.

O seu programa deve receber como entrada um inteiro N (maior ou igual a 3) representando quantos meses devem ser analisados, seguido por N linhas com a quantidade de vacinas disponíveis em cada mês. Como saída, o programa deve responder para cada mês i quantas pessoas receberam a primeira dose (D1_i), quantas pessoas receberam a segunda dose (D2_i) e quantas vacinas foram devolvidas (X_i). Além disso, ele deve fornecer um resumo do número de pessoas vacinadas e do número de vacinas devolvidas. A saída deve estar no seguinte formato:

	Mes 1:
	Vacinados com a primeira dose: D1_1
	Vacinados com a segunda dose: D2_1
	Vacinas devolvidas: X_1
	...
	Mes n:
	Vacinados com a primeira dose: D1_n
	Vacinados com a segunda dose: D2_n
	Vacinas devolvidas: X_n
	Total:
	Vacinados apenas com a primeira dose: D1
	Vacinados com as duas doses: D2
	Vacinas devolvidas: X

Exemplos de entradas e saídas esperadas pelo seu programa:


Obs. pessoal: Esse lab foi feito para usar laços entrelaçados (for dentro de for)
