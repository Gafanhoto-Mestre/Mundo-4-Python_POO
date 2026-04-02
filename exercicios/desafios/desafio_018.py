from rich import print
from rich.panel import Panel

class Churrasco:
    consumo_padrao = 0.400
    preco_kg = 82.40

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.convidados= quant

    def analisar(self):
        # consumo padrão de carne por pessoa: 400gr
        # Preço da carne R$ 82,40kg
        total_de_carne= (int(self.convidados) * self.consumo_padrao)
        custo_total= float(total_de_carne * self.preco_kg)
        custo_por_pessoa= custo_total / self.convidados
        resumo= Panel(f'Analisando [green]{self.titulo}[/] com [blue]{self.convidados} convidados[/]\nCada participante comerá {self.consumo_padrao}kg e cada Kg custa R${self.preco_kg:,.2f}\nRecomendo [blue]comprar {total_de_carne:.3f}Kg[/] de carne\nO custo total será de [green]R${custo_total:,.2f}[/]\nCada pessoa pagará [yellow]R${custo_por_pessoa:,.2f}[/] para participar.', title=f'{self.titulo}', width=70)
        return print(resumo)

c1= Churrasco('Churras no Bom ré', 15)
c1.analisar()