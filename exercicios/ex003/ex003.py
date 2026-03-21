from random import randint
from rich import print
from rich.table import Table

class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos!
    """
    def __init__(self,id,nome,saldo=0):
        tabela = Table(title='[blue]Banco do Brasil[/]')
        self.id= id
        self.titular= nome
        self.saldo= saldo
        tabela.add_column('ID')
        tabela.add_column('Titular')
        tabela.add_column('Saldo')
        tabela.add_row(self.id,self.titular,str(self.saldo))
        print(tabela)

    def __str__(self):
        return f'{10*"==="}\n>>>Dados da conta<<<\nID:{self.id}\nCliente: {self.titular}\nSaldo Atual: R${self.saldo:,.2f}\n{10*"==="}'
        
    def depositar(self,valor):
        self.saldo += valor
        return print (f'Depósito de R$ {valor:,.2f} realizado com sucesso!')

    def saque(self, valor):
        if valor > self.saldo:
            return print (f'Saque de R$ {valor:,.2f} [red]não autorizado[/] saldo insuficiente!\nSeu saldo é R$ {self.saldo:,.2f}')
        self.saldo -= valor
        

cliente= ContaBancaria(f'{randint(65,735)}','Mauro', 10000)
print(cliente)