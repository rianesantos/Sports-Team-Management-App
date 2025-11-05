from .base_command import Command
import services.services as sv

class EditPlayerCommand(Command):
    def execute(self):
        sv.edit_player()