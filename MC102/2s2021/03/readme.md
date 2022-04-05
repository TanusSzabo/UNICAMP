Lab03 - Cartões de Crédito

Você começou a trabalhar no seu novo emprego em um grande banco. O seu chefe, que gosta de automatizar os processos burocráticos, pediu para que você fizesse um programa que, dadas as informações de score (pontuação) de crédito, idade, saldo da conta bancária e salário do cliente, decida se ele poderia ou não ganhar um novo cartão de crédito.

Para ajudar na criação do programa, o seu chefe criou um diagrama para a concessão do crédito. A figura abaixo mostra o diagrama criado pelo seu chefe.

![Alt text](arvore.jpg)

Por exemplo, um cliente com um score de 825 pontos, 40 anos de idade, salário de R$ 1.500,00 e saldo de R$ 1.000,00, não deve receber um novo cartão de crédito. Da mesma forma, um cliente com um score de 530 pontos, 30 anos de idade, salário de R$ 3.500,00 e saldo de R$ 8.000,00, pode receber um novo cartão de crédito.

A entrada do seu programa será composta por quatro linhas. As duas primeiras linhas contém valores inteiros, representando o score e a idade do cliente. As duas próximas linhas contém valores reais, indicando o saldo da conta e o salário do cliente.

	<Score>
	<Idade>
	<Saldo>
	<Salário>

A saída deverá imprimir se o cliente receberá ou não o cartão de crédito. Caso o cliente possa receber um novo cartão, a saída deverá ser:

	Cartao concedido

Caso contrário, a saída deverá ser:

	Cartao nao concedido

Exemplos de entradas e saídas esperadas pelo seu programa:

Obs pessoal: Lab feito para aprender as funções condicionais if, elif e else
