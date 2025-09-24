from .base_command import Command
import services.services as sv

class ListPlayersCommand(Command):
    def execute(self):
        sv.list_players()