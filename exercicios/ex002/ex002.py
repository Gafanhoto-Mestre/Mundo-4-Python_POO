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

    # Dunder Method
    def __getstate__(self):
        return f'ESTADO = Nome:{self.nome}, Idade: {self.idade}'

    # Dunder Method
    def __str__(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade!'
    
# ===================================================================================
g1= MinhaClasse('Mauro', 40)    # Intanciei a classe
g1.aniversario()                # Método de instância

print(g1)                   # retorna o return de uma função __str__
print(g1.__dict__)          # Dunder Attribut
print(g1.__getstate__())    # Methot - (PODE SER PERSONALIZADO)
print(g1.__class__)         # Dunder Attribut
print(g1.__doc__)           # Dunder Attribut


    
