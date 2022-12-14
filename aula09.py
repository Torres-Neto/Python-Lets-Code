
# > LISTAS

#Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9, 9.7, 8.2]

# Criando Listas
lista = []
lista = list()
lista = [26, 'Walisson', 3.14, False]
lidaDeListas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

# Indexação
lista = [26, 'Walisson', 3.14, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1])

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[0:])
print(lista[2:6:2])


# Iterações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices

print('Comprimento da Lista: ',len(lista))

for i in range(len(lista)):
    print(lista[i])