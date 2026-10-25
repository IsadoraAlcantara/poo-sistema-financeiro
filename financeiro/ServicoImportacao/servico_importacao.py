from financeiro.conta import Conta

from financeiro.ServicoImportacao.criador_importador import (
    CriadorImportador,
    OpcoesBanco,
)
from financeiro.ServicoImportacao.formato_extrato import ExtratoBrutoDTO
from financeiro.receita import Receita
from financeiro.despesa import Despesa
from financeiro.categoria_receita import CategoriaReceita
from financeiro.categoria_despesa import CategoriaDespesa


class ServicoImportacao:

    def __init__(self, criador_importador: CriadorImportador) -> None:
        self._criador_importador = criador_importador

    def importar_para_conta(
        self, conta: Conta, caminho_arquivo: str, banco: OpcoesBanco
    ) -> ExtratoBrutoDTO:
        importador = self._criador_importador.criar(banco=banco)
        dto: ExtratoBrutoDTO = importador.importar_dto(caminho_arquivo)
        self._converter_e_adicionar_na_conta(dto, conta)

        return dto

    def _converter_e_adicionar_na_conta(
        self, dto: ExtratoBrutoDTO, conta: Conta
    ) -> None:
        """Converte cada TransacaoDTO em Receita ou Despesa."""
        cat_receita_padrao = CategoriaReceita(nome="Receita")
        cat_despesa_padrao = CategoriaDespesa(nome="Despesa", gasto_max=5000)

        for transacao in dto.transacoes:
            if transacao.valor >= 0:
                lancamento = Receita(
                    categoria=cat_receita_padrao,
                    valor=transacao.valor,
                    data=transacao.data,
                )
            else:
                lancamento = Despesa(
                    categoria=cat_despesa_padrao,
                    valor=abs(transacao.valor),
                    data=transacao.data,
                )

            conta.adicionar_lancamento(lancamento)


if __name__ == "__main__":
    from financeiro.ServicoImportacao.leitor import Leitor

    leitor = Leitor()
    criador_importador = CriadorImportador(leitor=leitor)
    servico_importacao = ServicoImportacao(criador_importador=criador_importador)
    minha_conta = Conta()

    print("\n" + "=" * 50)
    print("ESTADO INICIAL DA CONTA")
    print("=" * 50)
    print(f"Total de lançamentos processados : {len(minha_conta.lancamentos)}")
    print(f"Saldo consolidado da conta       : R$ {minha_conta.saldo:.2f}")
    print("=" * 50 + "\n")

    dto = servico_importacao.importar_para_conta(
        conta=minha_conta,
        caminho_arquivo="extrato_outubro.csv",
        banco=OpcoesBanco.INTER,
    )

    print("\n" + "=" * 50)
    print("TRANSAÇÕES BRUTAS (DTO)")
    print("=" * 50)
    for t in dto.transacoes:
        print(
            f"Categoria: {t.categoria:<20} | Data: {t.data} | Valor: R$ {t.valor:.2f}"
        )

    print("\n" + "=" * 50)
    print("ESTADO FINAL DA CONTA")
    print("=" * 50)
    print(f"Total de lançamentos processados : {len(minha_conta.lancamentos)}")
    print(f"Saldo consolidado da conta       : R$ {minha_conta.saldo:.2f}")
    for lancamento in minha_conta.lancamentos:
        print(
            f"Categoria: {lancamento.categoria.nome:<20} | Data: {lancamento.data} | Valor: R$ {lancamento.valor:.2f}"
        )
    print("=" * 50)
