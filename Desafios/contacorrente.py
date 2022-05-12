'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depositar e sacar.No construtor, saldo é opcional,
com valor default zero e os demais atributos são obrigatórios.
get_saldo, get_nome, get_conta'''

class ContaCorrente:
    #count = 0
    def __init__(self, nome, numero, saldo=0):
        self.__nome = nome
        self.__numero = numero
        self.__saldo = saldo
    def alterar_nome(self, nome_novo):
        self.__nome = nome_novo
    def depositar(self, valor=0):
        self.__saldo += valor
    def sacar(self, valor=0):
        self.__saldo -= valor
    def get_nome(self):
        return self.__nome
    def get_numero(self):
        return self.__numero
    def get_saldo(self):
        return self.__saldo
c1 = ContaCorrente('Naruto Uzumaki', 123456789, 2000)
c1.alterar_nome('Sasuke Uchiha')
c1.depositar(1000)
c1.sacar(500)

print('Nome do correntista: ', c1.get_nome())
print('Número da conta: ', c1.get_numero())
print('Saldo: ', c1.get_saldo())

#count = 5000 ai não precisa declarar nome no final da op usar contacorrente
