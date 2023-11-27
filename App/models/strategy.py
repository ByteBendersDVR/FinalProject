from abc import abstractmethod
from App.database import db

class Strategy(db.Model):
    
    @abstractmethod
    def choose_strategy(self):
        pass
    
class FastestGraduation(Strategy):
    
    def choose_strategy(self):
        return super().choose_strategy()
    
class EasyCourses(Strategy):
    
    def choose_strategy(self):
        return super().choose_strategy()
    
class PrioritizeElectives(Strategy):
    
    def choose_strategy(self):
        return super().choose_strategy()