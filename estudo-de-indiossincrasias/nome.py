#o objetivo sera criar um programa que recebe e imprime o nome do usuario
#uso dos metodos .upper(), .lowwer(), replace() e len().

nome = input("write your name:")

#imprime o nome em letras maiusculas
print(nome.upper())

#imprime o nome em letras minusculas
print(nome.lower())

#imprime o nome sem os espaços
print(nome.replace(" ", ""))

#imprime o numero de caracteres do nome
print(len(nome))