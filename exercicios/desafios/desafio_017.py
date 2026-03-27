from rich import print
from rich.panel import Panel
from rich import inspect

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    # Minha solução
    def tiqueta(self):
        etiq = Panel(f'{self.nome:^30}\n{30*"-"}\n'f'{f" R${self.preco:,.2f} ":.^30}',title='Produto', width=34)
        return print(etiq)

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precof = f" R${self.preco:,.2f} "
        conteudo += f"{precof.center(30, '.')}"
        etiq = Panel(conteudo, title="Produto", width=34)
        print(etiq)
    
p1 = Produto("iphone 17 Pro Max", 50000)
p2 = Produto("Notbook Gamer", 8000)
p3 = Produto("Mouse", 120)

p1.etiqueta()
p1.tiqueta()
# p2.etiqueta()
# p3.etiqueta()

inspect(p1)
