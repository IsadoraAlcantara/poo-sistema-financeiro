from abc import ABC, abstractmethod


class Categoria(ABC):

    def __init__(self, nome: str):
        self.nome = nome

    @abstractmethod
    def possui_limite(self) -> bool:
        pass