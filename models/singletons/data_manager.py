from models.models import Account 

class DataManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls)
            cls._instance.players = []
            cls._instance.recruits = []
            cls._instance.events = []
            cls._instance.equipments = []
            cls._instance.posts = []
            cls._instance.polls = []     
            cls._instance.account = Account(0.0)
    
def get_data_manager(): 
        return DataManager()
        