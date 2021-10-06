class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        a = float(input('Entre com a primeira nota de 0 a 10: '))
        print(a)
        if a > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif a < 0:
            raise InputError('Nota não pode ser menor que 0.')
        b = float(input('Entre com a segunda nota de 0 a 10: '))
        print(b)
        if b > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif b < 0:
            raise InputError('Nota não pode ser menor que 0.')
        c = float(input('Entre com a terceira nota de 0 a 10: '))
        print(c)
        if c > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif c < 0:
            raise InputError('Nota não pode ser menor que 0.')
        d = float(input('Entre com a segunda nota de 0 a 10: '))
        print(d)
        if d > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif d < 0:
            raise InputError('Nota não pode ser menor que 0.')
        media = (a + b + c + d) / 4
        print('A média das notas é: {}'.format(media))
        break

    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)