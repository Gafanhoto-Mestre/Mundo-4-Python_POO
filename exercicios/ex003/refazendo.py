class ContaBancaria:
    # Atributos de instancia
    def __init__(self,id, nome='', saldo=0):
        self.id= id
        self.titular= nome 
        self.saldo= saldo

    # Metodos de Atributo
    # def __str__(self): #Dunder A
    #     return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.'

    # def __getstate__(self):
    #     return f'Status da conta:\nID: {self.id}\nTitular: {self.titular}\nSaldo atual: {self.saldo}'
    
    def __repr__(self):
        return f'>>> Status da conta <<<\n ID: {self.id}\nTitular: {self.titular}\nSaldo atual: {self.saldo}'
    

c1 = ContaBancaria("55", "Mauro", 20000)
# print(c1.__getstate__())
