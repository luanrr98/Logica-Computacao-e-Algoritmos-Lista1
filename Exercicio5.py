#Um motorista deseja abastecer um valor X em reais, de combustível. 
#Escreva um algoritmo para ler o preço do litro do combustível e o valor que o motorista deseja abastecer. Em seguida, informe quantos litros foram abastecidos.

def abastecer(valor_litro,valor_abastecer):
    total_litro = valor_abastecer/valor_litro
    total_litro = round(total_litro,2)
    print(f"Foram abastecidos {total_litro} litro(s)")

print("------------------------------")
print("Valor da gasolina: 5 R$ litro")
print("------------------------------\n")

valor_litro = 5
valor_abastecer= float(input("Gostaria de abastecer qual valor: R$"))
abastecer(valor_litro,valor_abastecer)
