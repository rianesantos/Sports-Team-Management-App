from abc import ABC, abstractmethod

class EventListStrategy(ABC):
    @abstractmethod
    def list(self, events):
        pass