from abc import ABC, abstractmethod
from datetime import datetime


class Poll:
    poll_id_counter = 0
    def __init__(self, title, description, opt1, opt2, opt3):
        if not all([title.strip(), description.strip(), opt1.strip(), opt2.strip()]):
            raise ValueError("Poll title, description, and the first two options cannot be empty.")
        
        Poll.poll_id_counter += 1
        self.__title = title
        self.__description = description
        self.__opt1 = opt1
        self.__opt2 = opt2
        self.__opt3 = opt3
    
    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def opt1(self):
        return self.__opt1

    @property
    def opt2(self):
        return self.__opt2

    @property
    def opt3(self):
        return self.__opt3


class Post:
    post_id_counter = 0
    def __init__(self, title, content, date_str):
        if not title.strip() or not content.strip():
            raise ValueError("Post title and content cannot be empty.")
        
        try:
            self.__date = datetime.strptime(date_str, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Invalid date format for the post. Use DD/MM/YYYY.")
            
        Post.post_id_counter += 1
        self.__title = title
        self.__content = content
    
    @property
    def date(self):
        return self.__date.strftime('%d/%m/%Y')
    
    @property
    def title(self):
        return self.__title

    @property
    def content(self):
        return self.__content


class Account:
    def __init__(self, balance):
        if not isinstance(balance, (int, float)):
            raise TypeError("Initial balance must be a number.")
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def add_income(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Income value must be a positive number.")
        self.__balance += value

    def add_expense(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Expense value must be a positive number.")
        if value > self.__balance:
            raise ValueError("Insufficient balance to cover the expense.")
        self.__balance -= value


class Recruit:
    recruit_id_counter = 0
    def __init__(self, name, age, pros, cons, position, observation):
        if not name.strip() or not position.strip():
            raise ValueError("Recruit name and position are mandatory.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Recruit age must be a positive integer.")
            
        Recruit.recruit_id_counter += 1
        self.__name = name
        self.__age = age
        self.__pros = pros
        self.__cons = cons
        self.__position = position
        self.__observation = observation
    
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def pros(self):
        return self.__pros

    @property
    def cons(self):
        return self.__cons

    @property
    def position(self):
        return self.__position

    @property
    def observation(self):
        return self.__observation


class Equipment:
    VALID_STATUSES = ["new", "used", "damaged", "under maintenance"]
    equipment_id_counter = 0
    def __init__(self, name, type, quantity, status, observation):
        if not name.strip() or not type.strip():
            raise ValueError("Equipment name and type are mandatory.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if status.lower() not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status. Use one of the following: {', '.join(self.VALID_STATUSES)}")
            
        Equipment.equipment_id_counter += 1
        self.__name = name
        self.__type = type
        self.__quantity = quantity
        self.__status = status
        self.__observation = observation
    
    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def quantity(self):
        return self.__quantity

    @property
    def status(self):
        return self.__status

    @property
    def observation(self):
        return self.__observation


class Stats:
    def __init__(self, score, games_played):
        self.score = score
        self.games_played = games_played

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Score must be a non-negative integer.")
        self.__score = value

    @property
    def games_played(self):
        return self.__games_played

    @games_played.setter
    def games_played(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Games played must be a non-negative integer.")
        self.__games_played = value


class Player:
    id_inicial = 0

    def __init__(self, id, name, age, position, stats, health):
        
        if not name.strip():
            raise ValueError("Player name cannot be empty.")
        if not isinstance(age, int) or not (15 <= age <= 45):
            raise ValueError("Player age must be a number between 15 and 45.")
        if not position.strip(): 
            raise ValueError("Player position cannot be empty.")
        if not isinstance(stats, Stats):
            raise TypeError("The 'stats' argument must be an object of the Stats class.")
            
        Player.id_inicial += 1
        self.__id = Player.id_inicial
        self.__name = name
        self.__age = age
        self.__position = position
        self.__stats = stats
        self.__health = health
    
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def stats(self):
        return self.__stats

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

class Event(ABC):
    event_id_counter = 0
    def __init__(self, date_str, time, location):
        if not location.strip():
            raise ValueError("The event location cannot be empty.")
        try:
            self._date = datetime.strptime(date_str, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Invalid date format for the event. Use DD/MM/YYYY.")
        
        Event.event_id_counter += 1
        self._id = Event.event_id_counter
        self._time = time
        self._location = location

    @property
    def date(self):
        return self._date.strftime('%d/%m/%Y')
    
    @property
    def id(self):
        return self._id

    @property
    def time(self):
        return self._time

    @property
    def location(self):
        return self._location
    
    @abstractmethod
    def details(self):
        pass

class Match(Event):
    def __init__(self, date, time, opponent, location):
        super().__init__(date, time, location)
        if not opponent.strip():
            raise ValueError("The opponent's name cannot be empty.")
        self.__opponent = opponent
        self.__result = None
    
    @property
    def opponent(self):
        return self.__opponent

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value

    def details(self):
        return (f"ID: {self.id} | Match vs {self.opponent} | "
                f"Date: {self.date} | Time: {self.time} | "
                f"Location: {self.location} | Result: {self.result or 'Not defined'}")


class Training(Event):
    def __init__(self, date, time, location, focus):
        super().__init__(date, time, location)
        if not focus.strip():
            raise ValueError("The training focus cannot be empty.")
        self.__focus = focus
    
    @property
    def focus(self):
        return self.__focus

    def details(self):
        return (f"ID: {self.id} | Training | Date: {self.date} | Time: {self.time} | "
                f"Location: {self.location} | Focus: {self.focus}")
        
# ... (código existente das outras classes) ...

class Tournament(Event):
    """
    Representa o Composite (Composto). Pode conter outros Eventos (folhas ou outros composites).
    Implementa a mesma interface Event.
    """
    def __init__(self, date_str, time, location, name):
        super().__init__(date_str, time, location) # Chama o construtor da classe base Event
        if not name.strip():
            raise ValueError("Tournament name cannot be empty.")
        self.__name = name
        self._children = [] # Lista para guardar os eventos filhos (Matches, Trainings, etc.)

    @property
    def name(self):
        return self.__name

    def add_event(self, event: Event):
        """ Adiciona um evento filho (Match, Training ou outro Tournament). """
        if isinstance(event, Event):
            self._children.append(event)
        else:
            print("[Composite Error]: Only Event objects can be added to a Tournament.")

    def remove_event(self, event: Event):
        """ Remove um evento filho. """
        if event in self._children:
            self._children.remove(event)

    def details(self):
        """
        Implementa o método details.
        Mostra os detalhes do torneio e DELEGA a chamada 'details' para todos os filhos.
        """
        tournament_details = (f"ID: {self.id} | Tournament: {self.name} | "
                              f"Date: {self.date} | Time: {self.time} | "
                              f"Location: {self.location}\nContains:")
        
        children_details = []
        if not self._children:
            children_details.append("  (No events scheduled in this tournament yet)")
        else:
            for child in self._children:
                # Delega a chamada para os filhos, adicionando indentação
                children_details.append(f"  -> {child.details()}") 
        
        return tournament_details + "\n" + "\n".join(children_details)

