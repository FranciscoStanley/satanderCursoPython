from datetime import date, datetime, time

data = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
hora = time(hour=13, minute=14, second=00)
print('{} às {}'.format(data, hora))

def trabalhando_com_date():

    data_atual = date.today()
    print(data_atual.strftime('%A-%d/%m/%Y'))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    dias_semana = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
    print(dias_semana[data_atual.weekday()])




if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_datetime()
