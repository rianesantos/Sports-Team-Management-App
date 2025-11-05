from .event_factory_base import EventCreator
from models.models import Training
from models.singletons.data_manager import get_data_manager 

class TrainingFactory(EventCreator):
    
    def create_event(self, date, time, location):
        try:
            focus = input("Enter training objective: ")
            
            new_training = Training(date, time, location, focus)
            
            data_manager = get_data_manager()
            data_manager.events.append(new_training)
            
            print("\nTraining scheduled successfully.")
            return new_training
        
        except ValueError as e:
            print(f"\nError scheduling training: {e}")
            return None
            
        except Exception as e:
            print(f"\nAn unexpected error occurred during scheduling: {e}")
            return None