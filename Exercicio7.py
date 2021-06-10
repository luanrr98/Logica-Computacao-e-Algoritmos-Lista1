#Crie um algoritmo que calcule a gorjeta a ser paga de uma conta de restaurante. 
#A gorjeta é calculada como sendo 10% do valor da conta, que deve ser informado pelo usuário

valor_conta = float(input("Digite o valor da conta: R$"))
valor_gorjeta = round(valor_conta*0.1, 2)
print(f"O valor da gorjeta é: R${valor_gorjeta}")