from rich import print
from rich.panel import Panel


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        etiq = Panel(f'{self.nome:^30}\n{29*"-"}\n'f'{f" R${self.preco:,.2f} ":-^29}',title='Produto', width=33)
        return print(etiq)
    
p1 = Produto("iphone 17 Pro Max", 50000)
p2 = Produto("Notbook Gamer", 8000)
p3 = Produto("Mouse", 120)

p1.etiqueta()
p2.etiqueta()
p3.etiqueta()
