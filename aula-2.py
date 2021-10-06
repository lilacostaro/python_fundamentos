a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
potencia = a ** b
# print('soma: ' + str(soma))
# print('subtração:', subtracao)
# print('multiplicação:', multiplicacao)
# print('divisão: ' + str(divisao))
# print('resto: {}' .format(resto))
resultados = ( 'soma : {sum}. \nsubtração: {sub}. \nmultiplicação: {mult}. \ndivisão: {div}. \nresto: {res}. \npotencia {power}.' .format(res=resto, sum=soma, sub=subtracao, mult=multiplicacao, div=divisao, power=potencia))
print(resultados)