#Crie um algoritmo que calcule a área de um quadrado, sendo que o comprimento do lado é informado pelo usuário. 
#A área do quadrado é calculada elevando-se o lado ao quadrado.

def area_quadrado(lado):
    area = lado**2
    print(f"A Área do Quadrado é: {area}")

lado = float(input("Digite o valor do lado: "))
area_quadrado(lado)