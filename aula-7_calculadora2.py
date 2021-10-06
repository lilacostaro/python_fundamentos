# Metodo e Função = tydo o que retorna valor é função o que não retorna é metodo

class Calculadora:
    #def __init__(self):
        #pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 4))
print(calculadora.divisao(100, 5))
print(calculadora.multiplicacao(15, 8))