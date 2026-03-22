from rich import print
from rich.table import Table

tabela = Table(title='Tabela de preços')


tabela.add_column('Nome')
tabela.add_column('Preço')
tabela.add_row(*lista)


print(tabela)