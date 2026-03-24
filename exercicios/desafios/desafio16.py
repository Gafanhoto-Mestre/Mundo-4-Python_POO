from rich import print

class Funcionario():
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor= setor
        self.cargo= cargo

    def apresentacao(self):
        return print(f'Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa Curso em vídeo!')

c1= Funcionario('Maria', "Administração", 'Diretora')
print(c1.apresentacao())

c2= Funcionario('Mauro', 'Oftalmologia', 'Agente Administrativo')
print(c2.apresentacao())