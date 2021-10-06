# criando laços de repetição e condicional
# for
# a = int(input('Entre com um numero'))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div + 1
#         print(div)
# if div == 2:
#     print('numero {} é primo'.format(a))
# else:
#     print('numero {} não é primo'.format(a))

# a = int(input('Entre com um valor: '))
# b = int(input('Entre com outro valor: '))
# for num in range(a, b+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div = div + 1
#             #print(div)
#     if div == 2:
#         print(num)

# while

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# nota = float(input('Entre com a nota: '))
# while nota > 10:
#     nota = float(input('Nota invalida! Entre com a nota correta: '))
#     print(nota)

nota1 = float(input('Primeiro Bimestre: '))
while nota1 > 10:
    nota1 = float(input('Você digitou a nota errada! Primeiro Bimestre: '))
nota2 = float(input('Segundo Bimestre: '))
while nota2 > 10:
    nota2 = float(input('Você digitou a nota errada! Segundo Bimestre: '))
nota3 = float(input('Terceiro Bimestre: '))
while nota3 > 10:
    nota3 = float(input('Você digitou a nota errada! Terceiro Bimestre: '))
nota4 = float(input('Quarto Bimestre: '))
while nota4 > 10:
    nota4 = float(input('Você digitou a nota errada! Quarto Bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7.00:
    print('Sua média é {} parabéns você foi aprovado!'.format(media))
elif media < 7 and media >= 5:
    print('Sua média é {}, você esta de recuperação!'.format(media))
else:
    print('Sua média é {}, infelizmente você reprovou!'.format(media))
