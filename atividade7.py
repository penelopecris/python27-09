# variavel para armazenar o valor dado pelo usuario
valueUser = float(input("Informe o valor: "))

#variaveis responsaveis pelas contas do código
fifty = int(valueUser/50);
ten = int(valueUser/10);
one = int(valueUser / 1);

# imprimindo o resultado para o usuario
print("Notas de 50 necessarias para pagar o valor: ",fifty)
print("Notas de 10 necessarias para pagar o valor: ",ten)
print("Notas de 1 necessarias para pagar o valor: ",one)

