
#Recrie o algoritmo de cálculo de média das notas, mas, desta vez, calcule a média ponderada, sabendo que a primeira nota possui peso 1, a segunda nota possui peso 2 e a terceira nota possui peso 3.
#Sabendo que a média MP é calculada como

#MP =         N1 * P1 + N2 * P2 + N3 * P3
#           _____________________________
    
#            (P1 + P2 + P3)

#Onde N são as notas e, P, de seus respectivos pesos.

def calculo_media_ponderada(nota1,nota2,nota3):
    media = ((nota1*1)+(nota2*2)+(nota3*3)/(1+2+3))
    media = round(media,2)
    print(f"A média ponderada das notas foi: {media}.")

print("\nCalculo de média ponderada de notas! *Digite apenas notas entre 0 e 10\n")

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
    
calculo_media_ponderada(nota1,nota2,nota3) 
