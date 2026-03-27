
class Livro:
    def __init__(self, titulo, paginas=0):
        self.titulo= titulo
        self.paginas= paginas
        

    
    def avancar_paginas(self):
        if self.paginas == 0:
            print(f":book:[blue]Você acabou de abrir o livro[/] '[red]{self.titulo}[/]'[blue]que tem [green]{self.paginas}[/] [blue]no total. Você agora está na página {self.paginas}")
        