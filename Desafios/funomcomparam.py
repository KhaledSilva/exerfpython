nome = input("Digite seu nome completo: ")
def nc (nome):
    nocomp = len(nome)
    pala = len(nome.split())
    return nocomp, pala


nocomp, pala = nc(nome)

print(f'Quantidade de caracteres: {nocomp}')
print(f'Quantidade de palavras: {pala}')

''' sem usar função
nc = str(input('Digite o seu nome completo: ')).strip()
pala = nc.split()

nc = len(nc)
pala = len(pala)
print('Quantidade de caracteres: ', nc)
print('Quantidade de palavras: ', pala)'''
