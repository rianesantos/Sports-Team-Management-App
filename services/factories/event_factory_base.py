from abc import ABC, abstractmethod

class EventCreator(ABC):
    @abstractmethod
    def create_event(self, date, time, location):
        pass