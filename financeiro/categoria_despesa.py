from financeiro.categoria import Categoria


class NomeCategoriaDespesa:
    ALIMENTACAO = "alimentacao"
    TRANSPORTE = "transporte"
    LAZER = "lazer"
    AGUA = "agua"
    LUZ = "luz"
    INTERNET = "internet"
    ALUGUEL = "aluguel"


class CategoriaDespesa(Categoria):

    def __init__(self, nome: NomeCategoriaDespesa, gasto_max: int) -> None:
        super().__init__(nome)
        if gasto_max <= 0:
            raise ValueError("O gasto máximo de uma categoria deve ser maior que zero")
        self._gasto_max = gasto_max

    def alterar_gasto_max(self, novo_gasto_max: int) -> None:
        if novo_gasto_max <= 0:
            raise ValueError(
                "O gasto máximo de uma categoria deve ser maior que zero"
            )
        self._gasto_max = novo_gasto_max

    @property
    def gasto_max(self) -> int:
        return self._gasto_max

    def possui_limite(self) -> bool:
        return True


if __name__ == "__main__":
    cat_lazer = CategoriaDespesa(nome=NomeCategoriaDespesa.LAZER, gasto_max=200)
    print(f"Categoria: {cat_lazer.nome}, gasto max: {cat_lazer.gasto_max}")

    cat_lazer.alterar_gasto_max(500)
    print(f"Gasto máximo: {cat_lazer.gasto_max}")

    print(cat_lazer.possui_limite())
