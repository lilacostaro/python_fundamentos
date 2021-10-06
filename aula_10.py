# trabalhando com datas em Python

from datetime import date, time, datetime, timedelta

# Como recuperar a sata atual(Date)
# Como trabalhar com a data auterando a sua formatação
def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B,%d %Y')
    print(data_atual_str)
    print(type(data_atual_str))
    print(type(data_atual))

# Como gerar um horario(Time)
def trabalhando_com_time():
    horario = time(hour=15, minute=36, second=52)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

# Retornar data e hora atual (Datatime)
# Alterar formatação do Datatime
def trabalhando_com_datetime():
    data_hora_atual = datetime.now()
    print(data_hora_atual)
    tupla = ('', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    data_hora_atual_str = data_hora_atual.strftime('%d de {} de %Y ás %H:%M'.format(tupla[data_hora_atual.month]))
    print(data_hora_atual_str)
    print(data_hora_atual.strftime('%c'))
    print(data_hora_atual.weekday())
    tupla2 = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla2[data_hora_atual.weekday()])
    data_criada = datetime(2021, 10, 3, 22, 36, 45)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 22:45:30'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    # Realizar soma e subtração de data com TIMEDELTA
    nova_data = data_convertida + timedelta(days=365, hours=2, minutes=15, seconds=20)
    print(nova_data)



if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()