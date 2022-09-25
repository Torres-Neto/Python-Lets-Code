
# MÉTODOS PARA LISTA
lista = [1, 3, 12, 8, 2]

# append
print('Antes do append ',lista)
lista.append(3)
print('Depois do append ',lista)

# insert
lista.insert(2, 10)
print('Depois do Insert: ',lista)

# extend
lista2 = [1, 2, 3]
lista.extend(lista2)
print('Depois do extend: ', lista)

# pop
lista.pop()
print('lista após o pop: ',lista)

lista.pop(0)
print('lista após o pop: ',lista)

# remove
lista.remove(3)
print('lista após o remove: ',lista)

# count
print('Quantidade de 2 na lista', lista.count(2))

# index
print('Qual o índice do elemento 12: ',lista.index(12))

# sort
lista.sort(reverse=True)
print(lista)




# FUNÇÕES PARA LISTAS

# len
print(len(lista))

# sum
print(sum(lista))

# max
print(max(lista))

# min
print((min(lista)))