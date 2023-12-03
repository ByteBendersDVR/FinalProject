from abc import abstractmethod, ABC
from App.database import db

class Strategy(ABC):
    @abstractmethod
    def generateCoursePlan(self, programme):
        pass

# Sample subclass
class FastestGraduation(Strategy):
    def generateCoursePlan(self, programme):
        # Implementation specific to FastestGraduation
        pass

# Another subclass
class EasyCourses(Strategy):
    def generateCoursePlan(self, programme):
        # Implementation specific to EasyCourses
        pass

# Another subclass
class PrioritizeElectives(Strategy):
    def generateCoursePlan(self, programme):
        # Implementation specific to PrioritizeElectives
        pass