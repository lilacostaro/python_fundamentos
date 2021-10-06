# modulos e funçoes anonimas

from aula_7_televisao import Televisao
from aula_7_calculadora1 import Calculadora
from aula_8_contadordeletras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'cavalo', 'hipopotamo', 'cobra', 'coelho', 'preguiça', 'panda']
    total_letras = contador_letras(lista)
    total_letras2 = sum(total_letras)
    print('Total de letras em cada palavra da lista: {}'.format(total_letras))
    print('Total geral de letras na lista: {}'.format(total_letras2))
    print(teste())

