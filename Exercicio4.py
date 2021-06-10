#Crie um algoritmo que recebe um valor de temperatura em Celsius e o converte para Fahrenheit. 
#F = (C * 9/5)+32

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5)+32
    fahrenheit = round(fahrenheit,2)
    print("Fazendo a conversão...\n")
    print(f"{celsius}º celsius em fahrenheit é: {fahrenheit}ºF")

print("Conversor de Celsius para Fahrenheit")

celsius = float(input("Digite a temperatura em celsius: "))
celsius_to_fahrenheit(celsius)