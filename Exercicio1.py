#Crie um algoritmo que receba, como entrada, o valor de três notas de um aluno - com valor entre 0 e 10, e, em seguida, informe a média entre elas. 
#Neste momento, não é necessário validar se a nota está dentro do intervalo válido!

def calculo_media(nota1,nota2,nota3):
    media = (nota1+nota2+nota3)/3
    media = round(media,2)
    print(f"A média das notas foi: {media}.")

print("\nCalculo de média de notas! *Digite apenas notas entre 0 e 10\n")
nota1= float(input("Digite a primeira nota: "))
nota2= float(input("Digite a segunda nota: "))
nota3= float(input("Digite a terceira nota: "))
    
calculo_media(nota1,nota2,nota3) 
