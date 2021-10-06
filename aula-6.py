# organizando conjuntos e subconjuntos

# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(3)
# print(type(conjunto))
# print(conjunto)

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2)
conjunto_interseccao = conjunto.intersection(conjunto2)
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
conjunto_diferenca_simetrica = conjunto.symmetric_difference(conjunto2)

print('União: {}'.format(conjunto_uniao))
print('Intersecçaõ: {}'.format(conjunto_interseccao))
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))
print('Diferença Simetrica: {}'.format(conjunto_diferenca_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
conjunto_superset = conjunto_b.issuperset(conjunto_a)

print('A é um subcojunto de B? {}'.format(conjunto_subset))
print('B é um superconjunto de A? {}'.format(conjunto_superset))

animais = ['cachorro', 'gato', 'cachorro', 'gato', 'coelho', 'lobo']
print(animais)
conjunto_animais = set(animais)
print(conjunto_animais)
animais2 = list(conjunto_animais)
print(animais2)