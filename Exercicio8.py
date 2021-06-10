#Crie um algoritmo que calcule o novo valor de um salário a partir de um valor percentual de reajuste. 
#O valor atual do salário e o valor percentual do reajuste devem ser informados pelo usuário como, por exemplo, 7,3%.

salario_atual =float(input("Digite o valor atual do salário: R$"))
reajuste = float(input("Digite o percentual de reajuste (apenas o valor): "))
valor_reajuste= round((salario_atual*reajuste)/100, 2)
novo_salario = salario_atual+valor_reajuste

print(f"O novo valor do salário é: {novo_salario}")