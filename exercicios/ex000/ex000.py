# DECLARAÇÃO DE CLASSE
class MinhaClasse:
    def __init__(self): # Método Construtor
        # Atributo de instânca
        self.nome= ''
        self.idade= 0

    # Métodos de Instância
    def aniversario(self):
        self.idade= self.idade + 1

    def msg(self):
        print(f'{self.nome} tem a idade de {self.idade} anos!')

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade!'

g1= MinhaClasse()  # Intanciei a classe
g1.nome= 'Mauro'   # Atributo da classe
g1.idade= 40       # Atributo da classe

g1.aniversario()        # Método de Instância
g1.msg()                # Método de Instância
print(g1.mensagem())    # Método de Instância