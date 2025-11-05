import csv
from .data_persistence_adapter import DataPersistenceAdapter
from models.models import Player 

class PlayerCsvAdapter(DataPersistenceAdapter):
    """
    Adapter Concreto. Adapta a lista de objetos Player para 
    ser salva em um arquivo CSV.
    """
    def __init__(self, filepath="players_report.csv"):
        # Se você tiver uma pasta 'reports', pode usar "reports/players_data.csv"
        self._filepath = filepath

    def save_data(self, players_list):
        """
        Converte a lista de Players para o formato CSV e salva.
        """
        if not players_list:
            print("\n[Adapter]: Não há jogadores para salvar.")
            return

        try:
            with open(self._filepath, 'w', newline='', encoding='utf-8') as file:
                # O módulo 'csv' é o 'Adaptee' (o que estamos adaptando)
                writer = csv.writer(file)
                
                # Escreve o cabeçalho
                writer.writerow(["ID", "Nome", "Idade", "Posicao", "Saude", "Gols", "Jogos Jogados"])
                
                # Adapta os dados do objeto Player para linhas CSV
                for player in players_list:
                    writer.writerow([
                        player.id,
                        player.name,
                        player.age,
                        player.position,
                        player.health,
                        player.stats.score,
                        player.stats.games_played
                    ])
            print(f"\n[Adapter]: Jogadores salvos com sucesso em {self._filepath}")

        except IOError as e:
            print(f"\n[Erro do Adapter]: Falha ao escrever no arquivo {self._filepath}. Erro: {e}")
        except Exception as e:
            print(f"\n[Erro do Adapter]: Ocorreu um erro inesperado: {e}")