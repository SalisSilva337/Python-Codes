peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))
altura_metros = altura / 100  # Convertendo altura para metros
imc = peso / (altura_metros ** 2)

def categorizar_imc():
    f = open('file.txt', 'a')
    f.write("O SEU IMC DEU: \n")
    f.write("\n")

    if imc <= 18.5:
        f.write("Baixo Peso")
    elif 18.6 <= imc <= 24.9:
        f.write("Normal")
    elif 25 <= imc <= 29.9:
        f.write("Sobrepeso")
    else:
        f.write("Obesidade")

    f.close()

categorizar_imc()




     






