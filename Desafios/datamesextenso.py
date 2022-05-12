'''3) Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e
devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL
caso a data seja inválida.'''

data = '25/06/2020'
info = data.split('/')
dia = int(info[0])
mes = int(info[1])
ano = int(info[2])

''' 0 < dia < 31 
4, 6, 9, 11 = 30
2 ano bissexto ou não
29 ou 28'''

def validaData(d, m, a):
    #valida o dia
    if (dia<=0) or (dia>31):
        return False
    #valida mês com 30 dias

    meses30 = (4, 6, 9, 11)
    if (m in meses30):
        if (dia > 30):
            return False
    #valida fevereito e( anos bissextos

    if (m == 2):
        if (d > 28):
            if (a % 4 != 8):
                return False
            elif (a % 100 == 0) and (a % 1000 != 0):
                return False
    return True

if validaData(dia, mes, ano):
    mesExtenso = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','dezembro')
    novadata = info[0]+' de '+mesExtenso[mes-1]+' de ' +info[2]
    print(novadata)
else:
    print("Data Inválida! ")
