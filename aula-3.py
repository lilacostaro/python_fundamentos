nota1 = float(input('Primeiro Bimestre: '))
if nota1 > 10:
    nota1 = float(input('Você digitou a nota errada! Primeiro Bimestre: '))
nota2 = float(input('Segundo Bimestre: '))
if nota2 > 10:
    nota2 = float(input('Você digitou a nota errada! Segundo Bimestre: '))
nota3 = float(input('Terceiro Bimestre: '))
if nota3 > 10:
    nota3 = float(input('Você digitou a nota errada! Terceiro Bimestre: '))
nota4 = float(input('Quarto Bimestre: '))
if nota4 > 10:
    nota4 = float(input('Você digitou a nota errada! Quarto Bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7.00:
    print('Sua média é {} parabéns você foi aprovado!'.format(media))
elif media < 7 and media >= 5:
    print('Sua média é {}, você esta de recuperação!'.format(media))
else:
    print('Sua média é {}, infelizmente você reprovou!'.format(media))



# a = int(input('Entre com um valor: '))
# b = int(input('Entre com outro valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#     print('foi digitado um numero par')
# else:
#     print('nenhum número par foi digitado')

#a = int(input('Digite um numero: '))
# b = int(input('Digite outro numero: '))
# c = int(input('Digite mais um numero: '))
#
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
# print('Fim do programa!')

