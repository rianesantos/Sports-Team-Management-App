from .base_strategy import EventListStrategy
from models.models import Match, Training

class ListAllEventesStrategy(EventListStrategy):
    def list(self, events):
        if not events:
            print("\nNo events recorded.")
            return
        print("\n---- Event List ----")
        for event in events:
            print(event.details())
            print("-" * 100)