from random import randint
from rich import print
from rich.table import Table
from rich import inspect

class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos!
    """
    def __init__(self,id='',nome='',saldo=0):
        self.id= id
        self.titular= nome
        self.saldo= saldo

    def __str__(self):
        return f'{10*"==="}\n>>>Dados da conta<<<\n ID: {self.id}\n Cliente: {self.titular}\n Saldo Atual: R${self.saldo:,.2f}\n {10*"==="}'
      
    def __getstate__(self):
        return f'Dicionário personalizável!'

    def depositar(self,valor):
        self.saldo += valor
        return print (f'Depósito de R$ {valor:,.2f} realizado com sucesso!')

    def saque(self, valor):
        if valor > self.saldo:
            return print (f'Saque de R$ {valor:,.2f} [red]não autorizado[/] saldo insuficiente!\nSeu saldo é R$ {self.saldo:,.2f}')
        self.saldo -= valor

    def Tabela(self):
        tabela= Table(title='Minha primeira tabela')
        tabela.add_column('ID')
        tabela.add_column('Titular')
        tabela.add_column('Saldo')
        for v in lista:
            tabela.add_row(*v)
        return print(tabela)

    def App(self):
        global lista
        lista= []
        while True:
            identificador= f'{str(randint(500,1000))}'
            titular= str(input('Digite o nome: '))
            saldo= str(input('Digite o Saldo: '))
            cliente= ContaBancaria(identificador, titular, saldo)
            lista.append(cliente.__dict__.values())
            resp= input('Continuar? [s/n] ').upper()
            if resp in 'nN':
                break
        cliente.Tabela()
        inspect(cliente)
    
ContaBancaria().App()