from App.models import FastestGraduation, EasyCourses, PrioritizeElectives
from App.database import db
from App.controllers.strategy import generateCoursePlan

# think this is how it should work
def setStrategy(planOption):
   strategy = None

   if planOption == "fastest":
      strategy = FastestGraduation()
   if planOption == "easy":
      strategy = EasyCourses()
   if planOption == "electives":
      strategy = PrioritizeElectives()
   
   return strategy

