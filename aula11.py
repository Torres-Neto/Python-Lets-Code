

# CRIAÇÃO DE FUNÇÕES

# Função inicial
def saudacao():
    print('Seja bem-vindo(a)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

# Função com parâmetros
"""
nome = input('Qual seu nome? ')
curso = input('O que você está cursando? ')
def saudacao(nome, curso):
    print('Seja bem-vindo(a)! ',nome)
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao(nome, curso)
"""

# Função com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 2)

print('O resultado da soma é: ', resultado)