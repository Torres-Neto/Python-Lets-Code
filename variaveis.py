# 1. hashtag é a forma para se fazer comentário linha a linha.

"""
2. Utilizando  3 aspas é possível fazer um bloco de comentários.
Isso é um bloco de comentário
"""

idade = 26  #Criando uma variável
print(idade)

nome = 'Torres Neto'
print(nome)

altura = 1.73


'''
 Tipos de variáveis

 1. int: números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000
 2. float: números reais, ou seja, números com parte decimal: 1.0, -2.7, 3.14
 3. str: cadeias de caracteres, ou seja, dados textuais (string)
 4. bool: valores lógicos (booleanos): True ou False
'''

idade = 26
altura = 1.73
nome = 'Torres Neto'
estudando = True

print(type(idade))
print(type(altura))
print(type(nome))
print(type(estudando))


# Obtendo dados do usuário e salvando em variáveis

linguagem = input('Qual é a linguagem de programação que você está estudando? ')
print('A linguagem que você está estudando é', linguagem)