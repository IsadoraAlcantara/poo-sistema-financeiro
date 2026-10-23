from financeiro.categoria import Categoria


class CategoriaReceita(Categoria):

    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def possui_limite(self) -> bool:
        return False
