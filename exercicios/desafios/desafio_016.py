from rich import print
from rich import inspect

class Funcionario:  
    # Atributos de classe
    empresa = 'Sabor & Massa'

    def __init__(self, nome, setor, cargo):
        # Atributos de instância
        self.nome = nome
        self.setor= setor
        self.cargo= cargo

    # def apresentacao(self):
    #     return f'Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa Curso em vídeo!'

    # def apresentacao(self):
    #     return f'Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {Funcionario.empresa}!'
    
    def apresentacao(self):
        return f'Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {self.__class__.empresa}!'
    
c1= Funcionario('Maria', "Administração", 'Diretora')
print(c1.apresentacao())

c2= Funcionario('Mauro', 'Oftalmologia', 'Agente Administrativo')
print(c2.apresentacao())

inspect(c1, methods=True)
inspect(Funcionario)
inspect(Funcionario, all=True)