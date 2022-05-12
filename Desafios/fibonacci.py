'''1) A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz
de gerar a série até o n−ésimo termo.'''

termo = int(input('Digite o limite de serie de fibonacci desejada: '))
x1 = 1
x2 = 1
print(x1)
print(x2)
x3 = x1+x2

while (x3 <= termo):
    print(x3)
    x1 = x2
    x2 = x3
    x3 = x1 + x2
