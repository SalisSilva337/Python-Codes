menu = input("PRESSIONE QUALQUER TECLA PARA INICIAR \n")

while menu != 'sair':
    menu = input ("Selecione uma das opções a seguir: \n [cadastro] para cadastrar um novo aluno \n [notas] adicionar as notas do aluno e calcular a media das notas do aluno e ver aprovação \n [frequencia] ver a frequencia de aulas do aluno \n [resultado] ver a media e se o aluno foi aprovado \n")
    if menu ==  'cadastro':
        nome = input("digite o nome do aluno: ")
        idade = input("digite a idade do aluno: ")
        turno = input("digite o turno no qual o aluno irá estudar: ")

    elif menu ==  'notas':
        nota1= float(input("digite a primeira nota: "))
        nota2= float(input("digite a segunda nota: "))
        media = (nota1 + nota2)/2
        print(media)

    elif menu == 'frequencia': 
        frequencia = int(input("quantos dias o aluno frequentou o colegio: "))

    elif menu == 'resultado':    
        if media < 7:
            print("o aluno",nome,"de idade",idade,"anos do turno",turno,"possui a media de", media,"pontos")
            print("SUA MEDIA FOI DE",media,"\n VC FOI REPROVADO")
            a = input("Deseja realizar um trabalho extra pra haver um acrescimo na nota? [s]/[n] ")
            if a == 's':
                nota3 = 6.0
                media = (nota1 + nota2 + nota3)/3
                print ("o trabalho foi realizado com sucesso, o aluno",nome,"recebeu 6.0 pontos pelo trabalho")      
            else:
                print("O aluno", nome, "optou por nao realizar o trabalho, portanto ESTÁ REPROVADO")
        elif frequencia < 100:
            print("o aluno",nome,"de idade",idade,"anos do turno",turno,"possui a media de", media,"pontos")
            print("\n O aluno foi REPROVADO, devido a baixa frequência às aulas.")
        elif media >= 7 and frequencia > 101:
            print("o aluno",nome,"de idade",idade,"anos do turno",turno,"possui a media de", media,"pontos")
            print("SUA MEDIA FOI DE",media, "E SUA FREQUENCIA FOI ACIMA DE 100 DIAS DE AULA,PORTANTO, FOI APROVADO")

    

    