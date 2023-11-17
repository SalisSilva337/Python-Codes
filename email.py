email = input("Digite o seu email: ")   

 
if email == "":
   print("email nao pode ser vazio")
elif email.find("@") < 0:
   print ("Deve conter @")
elif email.find("gmail.com") < 0 or email.find("hotmail.com") < 0 or email.find("outlook.com"):
   print ("Necessita de uma especificação de email")
elif len(email) <= 11:
   print ("Seu email é muito curto")
elif email[0].isnumeric():
   print ("Não pode iniciar com número")
else:
   print ("O email",email,"está correto!")



