from rich import print
from rich.panel import Panel

print('Mauro Augusto [blue]Januário[/] da Paixão') # print

caixa = Panel("[yellow]Mauro Augusto J. da Paixão[/]", title="Mensagem", style="red", width=50) # Panel

print(caixa)