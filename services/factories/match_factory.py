from .event_factory_base import EventCreator
from models.models import Match
from models.singletons.data_manager import get_data_manager 

class MatchFactory(EventCreator):
    def create_event(self, date, time, location):
        try:
            opponent = input("Enter opponent name: ")
            new_match = Match(date, time, opponent, location)
        
            data_manager = get_data_manager() 
            data_manager.events.append(new_match)
            
            print("\nMatch scheduled successfully.")
            return new_match
        
        except ValueError as e:
            print(f"\nError scheduling match: {e}")
            return None
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            return None