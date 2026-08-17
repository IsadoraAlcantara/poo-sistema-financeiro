class Lancamento:

    def __init__(self, categoria: "Categoria", valor: int):
        self._categoria = categoria
        self._valor = valor

    def alterar_valor(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError("O valor de um lançamento não pode ser zero ou negativo")
        self._valor = novo_valor

    def alterar_categoria(self, nova_categoria):
            if nova_categoria.strip() == "":
                raise ValueError("O valor de um lançamento não pode ser zero ou negativo")
            self._valor = nova_categoria
    # refazer como uma classe em categoria