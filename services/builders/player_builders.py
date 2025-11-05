from abc import ABC, abstractmethod
from models.models import Player, Stats
from models.singletons.data_manager import get_data_manager 

class PlayerBuilderBase(ABC):

    @abstractmethod
    def get_basic_data(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass
        
    @abstractmethod
    def get_health_status(self):
        pass

    @abstractmethod
    def build_player(self):
        pass


class PlayerConcreteBuilder(PlayerBuilderBase):

    def __init__(self):
        self._reset()

    def _reset(self):
        self._name = None
        self._age = None
        self._position = None
        self._stats = None
        self._health = None

    def get_basic_data(self):
        print("\n--- New Player Data ---")
        try:
            self._name = input("Name: ")
            self._age = int(input("Age: "))
            self._position = input("Position: ")
        except ValueError:
             print("Erro: Idade deve ser um número.")
             self._age = -1 
        return self 

    def get_stats(self):
        print("\nPlayer Stats:")
        try:
            score = int(input("Goals Scored: "))
            games_played = int(input("Games Played: "))
            self._stats = Stats(score, games_played)
        except ValueError:
             print("Erro: Gols e Partidas devem ser números.")
             self._stats = None 
        return self

    def get_health_status(self):
        self._health = input("Health Status: ")
        return self
        
    def build_player(self):
        if self._name is None or self._stats is None:
             raise ValueError("Player basic data and stats are missing or invalid.")

        new_player = Player(
            Player.id_inicial, 
            self._name, 
            self._age, 
            self._position, 
            self._stats, 
            self._health
        )
    
        data_manager = get_data_manager()
        data_manager.players.append(new_player)
        print("\nPlayer registered successfully.")
        
        self._reset() 
        
        return new_player