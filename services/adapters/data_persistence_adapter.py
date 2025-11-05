from abc import ABC, abstractmethod

class DataPersistenceAdapter(ABC):
    """
    Interface Alvo (Target Interface) para o padrão Adapter.
    Define o método que o nosso sistema usará para salvar dados.
    """
    @abstractmethod
    def save_data(self, data):
        """
        Salva os dados em um formato específico (CSV, JSON, etc.).
        """
        pass