'''Program 2 do Feirante
emprime as frutas do arquivo frutas.txt
'''


with open('fruta.txt', 'w') as arq:
    while True:
        fruta = input('Digite o nome da fruta <ou sair>: ')
        if fruta != 'sair':
            arq.write(fruta)
            arq.write('\n')
        else:
            break


