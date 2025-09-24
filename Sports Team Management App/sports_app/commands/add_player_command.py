from .base_command import Command
import services.services as sv

class AddPlayerCommand(Command):
    def execute(self):
        sv.add_player