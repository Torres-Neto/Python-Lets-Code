# estruturas condicionais

'''
idade = 18

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')
'''

"""
# Imagine que você queira imprimir "Aprovado(a)", caso o estudante tenha uma média superior a 7
# e "Reprovado(a)", caso a média seja inferior a 7.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 7.0:
    print('A média foi: {:.2f}. Você está "APROVADO"'.format(media))
elif media >= 5.0:
    print('A média foi: {:.2f}. Você irá para "RECUPERAÇÃO"'.format(media))
else:
    print('A média foi: {:.2f}. Você está "REPROVADO"'.format(media))
"""

media = 5
presenca = 50

if media >= 7 and presenca >= 70:
    print('Aprovado!')
else:
    print('Reprovado!')