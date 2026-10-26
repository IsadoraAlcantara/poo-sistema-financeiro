from financeiro.conta import Conta

from financeiro.ServicoImportacao.criador_importador import (
    CriadorImportador,
    OpcoesBanco,
)
from financeiro.extrato import Extrato
from financeiro.receita import Receita
from financeiro.despesa import Despesa
from financeiro.categoria_receita import CategoriaReceita
from financeiro.categoria_despesa import CategoriaDespesa


class ServicoImportacao:

    def __init__(self, criador_importador: CriadorImportador) -> None:
        self._criador_importador = criador_importador

    def importar_para_conta(
        self, conta: Conta, caminho_arquivo: str, banco: OpcoesBanco
    ) -> Extrato:
        importador = self._criador_importador.criar(banco=banco)
        extrato = importador.importar(caminho_arquivo=caminho_arquivo)

        cat_receita_padrao = CategoriaReceita(nome="Receita")
        cat_despesa_padrao = CategoriaDespesa(nome="Despesa", gasto_max=5000)

        for fechamentos in extrato.fechamentos_filtrados:
            for transacao in fechamentos.lancamentos:
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

        return extrato


if __name__ == "__main__":
    from financeiro.ServicoImportacao.leitor import Leitor

    leitor = Leitor()
    criador_importador = CriadorImportador(leitor=leitor)
    servico_importacao = ServicoImportacao(criador_importador=criador_importador)
    conta = Conta()

    print("\n" + "=" * 50)
    print("ESTADO INICIAL DA CONTA")
    print("=" * 50)
    print(f"Total de lançamentos processados : {len(conta.lancamentos)}")
    print(f"Saldo consolidado da conta       : R$ {conta.saldo:.2f}")
    print("=" * 50 + "\n")

    extrato = servico_importacao.importar_para_conta(
        conta=conta,
        caminho_arquivo="extrato_outubro.csv",
        banco=OpcoesBanco.INTER,
    )

    print("\n" + "=" * 50)
    print("TRANSAÇÕES BRUTAS (DTO)")
    print("=" * 50)
    for f in extrato.fechamentos_filtrados:
        for t in f.lancamentos:
            print(
                f"Categoria: {t.categoria:<20} | Data: {t.data} | Valor: R$ {t.valor:.2f}"
            )

    print("\n" + "=" * 50)
    print("ESTADO FINAL DA CONTA")
    print("=" * 50)
    print(f"Total de lançamentos processados : {len(conta.lancamentos)}")
    print(f"Saldo consolidado da conta       : R$ {conta.saldo:.2f}")
    for lancamento in conta.lancamentos:
        print(
            f"Categoria: {lancamento.categoria.nome:<20} | Data: {lancamento.data} | Valor: R$ {lancamento.valor:.2f}"
        )
    print("=" * 50)
