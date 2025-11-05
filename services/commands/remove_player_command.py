from .base_command import Command
import services.services as sv

class RemovePlayerCommand(Command):
    def execute(self):
        sv.remove_player()