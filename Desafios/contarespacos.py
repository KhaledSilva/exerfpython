'''4) Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
a)quantos espaços em branco existem na frase.
b)quantas vezes aparecem as vogais a, e, i, o, u.'''

frase = input('Digite uma frase! ')
espacos = 0
vogais = 0
for letra in frase:
    if (letra == ' '):
        espacos += 1
    elif ('AEIOU'.find(letra.upper()) >= 0):
        vogais += 1

print(f'Na frase informada, existem {espacos} espaços e {vogais} vogais! ')
