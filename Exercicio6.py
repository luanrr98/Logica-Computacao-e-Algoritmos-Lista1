#Crie um algoritmo para calcular a média de duas notas digitadas pelo usuário, sendo que a segunda nota tem peso dois.
#Não irei usar uma função desta vez.
#Não especifica o intervalo de notas, não vou considerar apenas notas negativas

nota1 = float(input("Digite a primeira nota: "))
if nota1 < 0:
    print("Nota Inválida!!")
    exit() 
nota2 = float(input("Digite a segunda nota: "))
if nota2 < 0:
    print("Nota Inválida!!")
    exit() 

media = (nota1+nota2*2)/(1+2) #a nota1 tem peso 1
media= round(media,2)

print(f"A média das notas foi: {media}")