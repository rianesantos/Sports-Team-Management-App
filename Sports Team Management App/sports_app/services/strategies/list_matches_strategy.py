from .base_strategy import EventListStrategy
from models.models import Match

class ListMatchesStrategy(EventListStrategy):
    def list(self, events):
        matches = [event for event in events if isinstance(event, Match)]
        
        if not matches:
            print("\nNo matches recorded.")
            return
        print("\n---- List of Matches ----")
        for match in matches:
            print(match.details())
            print("-" * 100)
            