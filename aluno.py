from class_aluno import Aluno

nome_aluno = input("Qual o seu nome: ")
idade_aluno = input("Qual a sua idade: ")
nota1_aluno = input("Qual a sua primeira nota: ")
nota2_aluno = input("Qual a sua segunda nota: ")

aluno_escola = Aluno()   
print("O Aluno",nome_aluno,"de idade", idade_aluno, "anos", aluno_escola.media_aluno())