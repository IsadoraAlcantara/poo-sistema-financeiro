from abc import ABC, abstractmethod


class Documento(ABC):

    @abstractmethod
    def adicionar_cabecalho(self, titulo: str) -> None:
        pass

    @abstractmethod
    def adicionar_corpo(self, dados: list[str]) -> None:
        pass

    @abstractmethod
    def adicionar_rodape(self, rodape: str) -> None:
        pass

    @abstractmethod
    def salvar(self, nome_arquivo) -> None:
        pass


class DocumentoPDF(Documento):

    def __init__(self):
        self.conteudo: list[str] = []

    def adicionar_cabecalho(self, titulo: str) -> None:
        divisor = "=" * 46
        self.conteudo.append(divisor)
        self.conteudo.append(titulo)
        self.conteudo.append(divisor)

    def adicionar_corpo(self, linhas: list[str]) -> None:
        for linha in linhas:
            self.conteudo.append(linha)

    def adicionar_rodape(self, texto: str) -> None:
        divisor_suave = "-" * 46
        divisor_forte = "=" * 46

        self.conteudo.append(divisor_suave)
        for info in texto.split(" | "):
            self.conteudo.append(info)
        self.conteudo.append(divisor_forte)

    def salvar(self, nome_arquivo: str) -> None:
        print(f"\n[Gerando Arquivo: {nome_arquivo}.pdf]")
        print("\n".join(self.conteudo))


class DocumentoCSV(Documento):

    def __init__(self):
        self.linhas_csv: list[str] = []

    def adicionar_cabecalho(self, titulo: str) -> None:
        self.linhas_csv.append(f"# {titulo}")
        self.linhas_csv.append("Métrica;Valor")

    def adicionar_corpo(self, linhas: list[str]) -> None:
        for linha in linhas:
            if ":" in linha:
                chave, valor = linha.split(":", 1)
                self.linhas_csv.append(f'"{chave.strip()}";"{valor.strip()}"')

    def adicionar_rodape(self, texto: str) -> None:
        for info in texto.split(" | "):
            if ":" in info:
                chave, valor = info.split(":", 1)
                self.linhas_csv.append(f'"{chave.strip()}";"{valor.strip()}"')

    def salvar(self, nome_arquivo: str) -> None:
        print(f"\n[Gerando Arquivo: {nome_arquivo}.csv]")
        print("\n".join(self.linhas_csv))


class DocumentoHTML(Documento):
    def __init__(self):
        self.tags: list[str] = []

    def adicionar_cabecalho(self, titulo: str) -> None:
        self.tags.append(f"<h2>{titulo}</h2>")
        self.tags.append("<table>")

    def adicionar_corpo(self, linhas: list[str]) -> None:
        for linha in linhas:
            if ":" in linha:
                chave, valor = linha.split(":", 1)
                self.tags.append(
                    f"  <tr><td><strong>{chave.strip()}</strong></td><td>{valor.strip()}</td></tr>"
                )

    def adicionar_rodape(self, texto: str) -> None:
        for info in texto.split(" | "):
            if ":" in info:
                chave, valor = info.split(":", 1)
                self.tags.append(
                    f'  <tr class="destaque"><td><strong>{chave.strip()}</strong></td><td>{valor.strip()}</td></tr>'
                )
        self.tags.append("</table>")

    def salvar(self, nome_arquivo: str) -> None:
        print(f"\n[Gerando Arquivo: {nome_arquivo}.html]")
        print("\n".join(self.tags))
