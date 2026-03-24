from rich import print
from rich.table import Table

tabela = Table(title='Tabela de preços')


lista = [['cebola', '40',],['Alface', '89'], ['Carne', '78'] ]

tabela.add_column('Nome')
tabela.add_column('Preço')
for l in lista:
    tabela.add_row(*l)
tabela.add_row()


print(tabela)