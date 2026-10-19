from financeiro.conta import Conta
from financeiro.extrato import Extrato
from financeiro.ServicoImportacao.criador_importador import CriadorImportador, OpcoesBanco
# from financeiro.ServicoImportacao.exportador_extrato import ExportadorExtrato
from financeiro.ServicoImportacao.leitor import Leitor
from financeiro.ServicoImportacao.formato_extrato import ExtratoBrutoDTO
from financeiro.receita import Receita
from financeiro.despesa import Despesa
from financeiro.categoria_receita import CategoriaReceita, NomeCategoriaReceita
from financeiro.categoria_despesa import CategoriaDespesa, NomeCategoriaDespesa


class ServicoImportacao:
    """
    Serviço de aplicação que orquestra a importação:
    - Recebe as fábricas por injeção de dependência.
    - Converte TransacaoDTO do extrato bruto em Receita/Despesa.
    - Alimenta a Conta do domínio.
    """

    def __init__(self, criador_importador: CriadorImportador | None = None) -> None:
        # Injeção de dependência via construtor (com fallback padronizado)
        self._criador_importador = criador_importador or CriadorImportador()

    def importar_para_conta(
        self, 
        conta: Conta, 
        caminho_arquivo: str, 
        banco: OpcoesBanco
    ) -> ExtratoBrutoDTO:
        # 1. Instancia o importador do banco usando a fábrica injetada
        importador = self._criador_importador.criar(banco=banco)

        # 2. Lê o arquivo e obtém os dados brutos do DTO
        dto: ExtratoBrutoDTO = importador.importar(caminho_arquivo)

        # 3. Converte os DTOs em objetos ricos do domínio e adiciona na Conta
        self._converter_e_adicionar_na_conta(dto, conta)

        return dto

    def _converter_e_adicionar_na_conta(self, dto: ExtratoBrutoDTO, conta: Conta) -> None:
        """Converte cada TransacaoDTO em Receita ou Despesa."""
        cat_receita_padrao = CategoriaReceita(NomeCategoriaReceita.SALARIO)
        cat_despesa_padrao = CategoriaDespesa(NomeCategoriaDespesa.INTERNET, gasto_max=5000)

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
    # 1. Instanciação das dependências (Raiz de Composição)
    criador_importador = CriadorImportador()
    servico_importacao = ServicoImportacao(criador_importador=criador_importador)

    # 2. Instanciação da conta de domínio
    minha_conta = Conta()

    # 3. Execução do caso de uso
    dto_processado = servico_importacao.importar_para_conta(
        conta=minha_conta,
        caminho_arquivo="extrato_outubro.csv",
        banco=OpcoesBanco.INTER,
    )

    # 4. Exibição dos dados do DTO e o resultado na Conta
    print("\n" + "=" * 50)
    print("TRANSAÇÕES BRUTAS (DTO):")
    print("=" * 50)
    for t in dto_processado.transacoes:
        print(f"Data: {t.data} | Descrição: {t.descricao:<20} | Valor: R$ {t.valor:.2f}")

    print("\n" + "=" * 50)
    print("ESTADO FINAL DA CONTA:")
    print("=" * 50)
    print(f"Total de lançamentos processados : {len(minha_conta.lancamentos)}")
    print(f"Saldo consolidado da conta       : R$ {minha_conta.saldo:.2f}")
    print("=" * 50)