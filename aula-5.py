# Listas e Tuplas

############### listas ###################################
# consulta = str(input('Digite um animal: '))
# lista = [12, 31, 5, 78, 9]
animais = ['cachorro', 'gato', 'coelho', 'elefante', 'arara', 'lobo', 'porco', 'girrafa', 'leão', 'hiena']
# nova_lista = animais * 3

# animais[0] = 'macaco'
# print(animais)

# lista.sort()
# animais.sort()
# print(lista)
# print(animais)
# lista.reverse()
# animais.reverse()
# print(lista)
# print(animais)

# print(nova_lista)

# print(lista, animais)
# print(animais[1])

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
# print(min(animais))


# if consulta in animais:
#     print('{} está na lista'.format(consulta))
# else:
#     print('{} ainda não existe na lista,  será incluido!'.format(consulta))
#     animais.append(consulta)
#     print(animais)
#
# #animais.pop(1)
# animais.remove('elefante')
# print(animais)

######################### tuplas ###############################

tupla = (1, 15, 22, 14)
# tupla[0] = 31 não suportado

print(len(tupla))
print(len(animais))

tupla_animais = tuple(animais)
print(type(tupla_animais))
print(tupla_animais)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)
