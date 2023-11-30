from App.models import CoursePlanGenerator, Strategy, FastestGraduation, EasyCourses, PrioritizeElectives
from App.database import db
from App.controllers.strategy import generateCoursePlan

# think this is how it should work
def setStrategy(planOption):
    if planOption == 1:
       CoursePlanGenerator.strategy = FastestGraduation()
    if planOption == 2:
       CoursePlanGenerator.strategy = EasyCourses()
    if planOption == 3:
       CoursePlanGenerator.strategy = PrioritizeElectives()

# not even sure if we need this
def generateCoursePlan(student, command, programme_id):
   """ call strategy's generateCoursePlan """
