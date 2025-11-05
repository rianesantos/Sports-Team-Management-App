from .player_builders import PlayerConcreteBuilder

class PlayerDirector:

    def __init__(self, builder: PlayerConcreteBuilder):
        self._builder = builder

    def construct_full_player(self):

        return self._builder \
            .get_basic_data() \
            .get_stats() \
            .get_health_status() \
            .build_player()