valor_produto = float(input("Digite o valor do produto: "))
valor_desconto = float(input("Digite o valor do desconto: "))

valor_do_produto = valor_produto - (valor_produto * valor_desconto / 100)
valor_final = round(valor_do_produto, 2)

print(f"O valor final do produto com desconto é: R$ {valor_final:.2f}")

if valor_produto >= 500 and valor_desconto >= 15:
    print("Parabéns! Você ganhou um cupom de desconto de 15% nessa compra!")
else:
    print("Você não ganhou o cupom de 15%. O produto precisa custar R$500 ou mais e o desconto informado precisa ser de pelo menos 15%.")
