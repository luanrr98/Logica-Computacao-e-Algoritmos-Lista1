#Crie um algoritmo que recebe o valor da altura e do peso de uma pessoa e retorna seu IMC. 
#IMC = peso / altura² 

def calculo_imc (peso,altura):
    imc = peso / altura**2
    imc = round(imc,2)
    print(f"Seu IMC é: {imc}")

print("\nCalculo DE IMC!\n")
peso = float(input("Digite o seu peso em KG: "))
altura = float(input("Digite a sua altura em metros: "))
calculo_imc(peso,altura)