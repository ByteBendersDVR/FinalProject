from App.models import Strategy
from App.database import db 
from abc import abstractmethod

@abstractmethod
def generateCoursePlan(programme):
    pass