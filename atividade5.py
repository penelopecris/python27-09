# variaveis que guardam os valores de produto e tambem de desconto
valueProduct = float(input("Informe o valor do produto: "));
valueDiscount = float(input("Agora, informe o valor do desconto recebido:"));

# variavel que vai armazenar a conta de desconto 
discount = valueProduct*(valueDiscount/100);

# imprimindo o resultado na tela 
print("O valor do desconto foi de: ", discount)



