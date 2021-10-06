#Utilizar exceções específicas
#Encadeamento de exceções

lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisão = 10 / 1
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero!')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
#Como lançar uma exceção genérica
except BaseException as ex:
    print('Erro desconhecido, Erro: {}'.format(ex))
#Else e Finally
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre Executa')
    print('fechando o arquivo')
    arquivo.close()


#Criação de exceções customizadas