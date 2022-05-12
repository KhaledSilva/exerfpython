'''Faça um programa em python para identificar se uma string recebida é ou não um palindromo.'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
pajunta = ''.join(palavra)
inverso = ''
for letra in range(len(pajunta) - 1, -1, -1):
    inverso += pajunta[letra]
if inverso == pajunta:
    print('A string é um Palíndromo')
else:
    print('A string não é um Palíndromo')

'''exemplo prof de fatiamento
# recebe uma string
string = input('Digite uma string: ').upper()
# inverte a string e coloca em contrario
contrario = string[::-1]
print(contrario)
# compara a string recebida com a contraria... se igual (sem esoaços)
if (string.replace(' ', '') == contrario.replace(' ', '')):
    print('A string eh um palindromo')
else:
    print('A string nao eh um palíndromo')
'''
