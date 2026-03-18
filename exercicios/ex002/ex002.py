# DECLARAÇÃO DE CLASSE
class MinhaClasse:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome='vazio', idade=0): # Método Construtor
        # Atributo de instânca
        self.nome= nome
        self.idade= idade

    # Métodos de Instância
    def aniversario(self):
        self.idade= self.idade + 1
    
    def __str__(self): # Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade!'
    


g1= MinhaClasse('Mauro', 40)         # Intanciei a classe
g1.aniversario()

for k in g1.__dict__.items():
    print(f'{k[g1.__dict__]}')

