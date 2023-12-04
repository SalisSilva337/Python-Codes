nome_aluno = input("Qual o seu nome: ")
idade_aluno = input("Qual a sua idade: ")
nota1_aluno = int(input("Qual a sua primeira nota: "))
nota2_aluno = int(input("Qual a sua segunda nota: "))
mediaa = int(nota1_aluno + nota2_aluno)/2


class Aluno:
    def __init__ (self,nome, idade, nota1, nota2):
        
        self.nome = nome_aluno
        self.idade = idade_aluno
        self.nota1 = nota1_aluno
        self.nota2 = nota2_aluno
        self.mediaa = mediaa       
    def media_aluno (self):
        if self.mediaa < 7:
            print("VOCÊ FOI REPROVADO!")
        else:
            print("VOCÊ FOI APROVADO!")

aluno_escola = Aluno(nome = nome_aluno, idade = idade_aluno, nota1 = nota1_aluno, nota2 = nota2_aluno)   
print("O Aluno",nome_aluno,"de idade", idade_aluno, "anos", "tem a media de ",mediaa, "\n", aluno_escola.media_aluno())




