'''Duas funções: A primeira vai ler um valor de entrada e guardar em um arquivo (w) chamado numero.txt.
A segunda função vai abrir esse arquivo (r), ler o número e determinar se esse número é primo ou não.
Fazer a execução dessas duas funções.'''

def primo(numero):
    ehprimo = True
    i = 2
    while i < numero:
        if (numero % i) == 0:
            ehprimo = False
        i += 1
    return ehprimo

def guardar():
    n = input("Digite o numero: ")
    arq = open('numero.txt', 'w')
    arq.write(n)
    arq.close()

def ler():
    arq = open('numero.txt')
    n = int(arq.read())
    if primo(n):
        print(f'O numero {n} é primo! ')
    else:
        print(f'O numero {n} não é primo! ')

print("iniciando execução do programa... ")
print("Lendo e guardano o Número... ")
guardar()
print("Lendo e definindo se é primo... ")
ler()
print("Final de execução... ")
