from .base_command import Command
from services.adapters.player_csv_adapter import PlayerCsvAdapter
from models.singletons.data_manager import get_data_manager

class SavePlayersCommand(Command):
    """
    Comando para invocar o Adapter e salvar os jogadores em um arquivo CSV.
    """
    def execute(self):
        # Obtém a única instância de dados
        data_manager = get_data_manager()
        
        # Cria o adaptador (pode ser qualquer tipo de Adapter que implemente DataPersistenceAdapter)
        adapter = PlayerCsvAdapter("players_report.csv")
        
        # O Comando invoca o método 'save_data' do adapter, passando a lista de Players.
        adapter.save_data(data_manager.players)