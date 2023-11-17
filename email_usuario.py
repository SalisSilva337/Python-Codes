nome = input("Digite o seu nome e sobrenome: ")
email_usuario = input("Digite o seu email: ") 
email_letra = email_usuario[0]
x=nome.split (" ")
print(x)
usuario_criado = x[0][0] + x[1][0] + x[2][0]


print("Parabéns",nome,"o usuario",usuario_criado,"foi criado com sucesso!")
print("Enviamos para",email_letra,"***email.com a sua senha de acesso")
