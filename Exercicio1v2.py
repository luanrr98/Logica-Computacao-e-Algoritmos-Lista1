#Crie um algoritmo que receba, como entrada, o valor de três notas de um aluno - com valor entre 0 e 10, e, em seguida, informe a média entre elas. 
#Verificando se a nota está no intervalo

def calculo_media(nota1,nota2,nota3):
    media = (nota1+nota2+nota3)/3
    media = round(media,2)
    print(f"A média das notas foi: {media}.")

print("\nCalculo de média de notas! *Digite apenas notas entre 0 e 10\n")

nota1= float(input("Digite a primeira nota: "))
if nota1 >10 or nota1 <0:
    print("Nota inválida!")
    exit()
nota2= float(input("Digite a segunda nota: "))
if nota2 >10 or nota2 <0:
    print("Nota inválida!")
    exit()
nota3= float(input("Digite a terceira nota: "))
if nota3 >10 or nota3 <0:
    print("Nota inválida!")
    exit()
    
calculo_media(nota1,nota2,nota3) 
