# Agora, vamos ver um novo recurso do Python: as bibliotecas. Elas possuem várias funções já prontas
# A biblioteca permite representar e manipular datas e horários
# Primeiro, vamos começar pelas datas
from datetime import date

data_atual = date.today()
# print(data_atual)

dataEspecifica = date(2025, 12, 25) # 25 de Dezembro de 2025
# print(dataEspecifica.day)
# print(dataEspecifica.month)

dataFormatada = data_atual.strftime("%d/%m/%Y") # Função que muda o formato da data. Para isso, a data é transformada em uma string
# print(dataFormatada)

# Vamos ver sobre as horas Mudar o import
from datetime import *

data_hora = datetime.now()
# print(data_hora)
# print(data_hora.time())

# Mudar o formato desta data e hora, deste datetime
dhFormatada = data_hora.strftime("%d/%m/%Y %H:%M:%S")
# print(dhFormatada)

# CONTINUAR A PARTIR DAQUI

outroFormato = data_atual.strftime("Hoje é %A, dia %d de %B de %Y")
# print(outroFormato)

# Para definir a hora em um datetime
novaDataHora = datetime(1963, 9, 13, 10, 20, 0)
# print(novaDataHora)

# Parse - Converter uma string para um data da biblioteca datetime
dataString = "2005-01-05" # Ano = 2005, Mês = 1, Dia = 5
dataObjeto = datetime.strptime(dataString, "%Y-%m-%d")
# print(dataObjeto) # ou dataObjeto.date

# Cálculos com datas

# Adicionar ou subtrair dias
data_futura = datetime.now() + timedelta(days=7)
data_futura2 = datetime.now() + timedelta(days=7, hours=6)
data_passada = datetime.now() - timedelta(days=30)

# print(data_futura)
# print(data_futura2)
# print(data_passada)

# Diferença entre datas
data1 = datetime(2022, 1, 10, 14, 0, 0)
data2 = datetime(2022, 1, 1)
# diferenca = data1 - data2
# print(diferenca) # ou diferenca.days

if data1 < data2:
    print("Data 1 é posterior a Data 2")
elif data1 > data2:
    print("É o contrário")
else:
    print("São iguais")



# MOMENTO DO EXERCÍCIO